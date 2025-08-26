from pathlib import Path
from time import sleep
from typing import Union

import PySpin
import numpy as np
from PySpin import ImageEventHandler, ImageProcessor
from PySide6.QtCore import Signal, QObject, QThreadPool

from dewan_flir_camera.cam import Cam
from dewan_flir_camera.options import AcquisitionState
from dewan_flir_camera.threads import VideoStreamer, VideoStreamWorker


class ImageHandler(ImageEventHandler):
    class ImageEventEmitter(QObject):
        image_display_signal = Signal(np.ndarray)
        image_record_signal = Signal(np.ndarray)

        def __init__(self):
            super().__init__()

    def __init__(self, save_dir: Union[str, Path], logger):
        super().__init__()
        self.logger = logger
        self.save_dir = save_dir
        self.acquired_images = 0

        self.do_save = False  # Causes a huge delay for image acquisition
        self.display = True
        self.record = True

        self._image_processor: PySpin.ImageProcessor = []
        self.image_event_emitter = self.ImageEventEmitter()
        self._init_image_processor()
        self._init_save_dir()

    def _init_save_dir(self):
        if not self.save_dir.exists():
            self.save_dir.mkdir(exist_ok=True)

    def _init_image_processor(self):
        self._image_processor = ImageProcessor()
        self._image_processor.SetColorProcessing(
            PySpin.SPINNAKER_COLOR_PROCESSING_ALGORITHM_HQ_LINEAR
        )

    def OnImageEvent(self, image):
        if image.IsIncomplete():
            self.logger.error("Image Incomplete!: %s", image.GetImageStatus())
        else:
            try:
                _image = self._image_processor.Convert(image, PySpin.PixelFormat_Mono8)
                image_ndarray = _image.GetNDArray()
                _image.Release()
                if self.display:
                    self.image_event_emitter.image_display_signal.emit(image_ndarray)
                if self.record:
                    self.image_event_emitter.image_record_signal.emit(image_ndarray)
                if self.do_save:
                    self.save_image(_image)

                self.acquired_images += 1
            except Exception as se:
                self.logger.error("Error saving image: %s", se)

    def save_image(self, image):
        _filename = f"image-{self.num_acquired_images}.jpg"
        _file_path = self.save_dir.joinpath(_filename)
        image.Save(str(_file_path))

    def reset(self):
        self.acquired_images = 0

    @property
    def num_acquired_images(self):
        return self.acquired_images


class VideoAcquisition:
    class VideoAcquisitionEmitter(QObject):
        add_to_buffer = Signal(np.ndarray)
        done = Signal(bool)
        start = Signal()

        def __init__(self):
            super().__init__()

    def __init__(self, cam, logger, path, file_stem):
        self.camera: Cam = cam
        self.logger: logger = logger
        self.path: Path = path
        self.file_stem: str = file_stem
        self.video_acquisition_emitter = self.VideoAcquisitionEmitter()
        self.threadpool = QThreadPool()
        self.stream_timer = VideoStreamer(self)
        self.no_more_frames: bool = False
        self.num_received_frames: int = 0
        self.last_num_received_frames: int = 0
        self.cycles_w_no_frames: int = 0
        self.num_videos_saved: int = 0
        self.current_worker: VideoStreamWorker = None
        self.event_handler: ImageEventHandler = None

    def start_experiment_video_acquisition(self):
        self.init_new_stream_worker()
        self.camera.trigger_acquisition(AcquisitionState.BEGIN)
        self.stream_timer.start(1000)  # start the stream timer

    def end_experiment_video_acquisition(self):
        self.camera.trigger_acquisition(AcquisitionState.END)
        self.stream_timer.stop()

    def init_new_stream_worker(self):
        filename = f"{self.file_stem}-trial-{self.num_videos_saved + 1}.mp4"
        save_path = self.path.joinpath(filename)
        fps = self.camera.current_FPS
        width, height = self.camera.frame_size
        self.current_worker = VideoStreamWorker(
            save_path, fps, width, height, self.logger
        )
        self.video_acquisition_emitter.add_to_buffer.connect(
            self.current_worker.add_to_buffer
        )
        self.video_acquisition_emitter.done.connect(self.current_worker.stop)
        # ImageEvent -> emits image_record_signal -> VideoAcquisition.add_new_frame -> emits add_to_bufer -> VideoStreamWorker.add_to_buffer
        self.threadpool.start(self.current_worker)

    def add_new_frame(self, image):
        self.video_acquisition_emitter.add_to_buffer.emit(image)
        self.num_received_frames += 1

    def reset_acquisition(self):
        self.end_experiment_video_acquisition()
        sleep(0.1)
        self.event_handler.reset()
        self.start_experiment_video_acquisition()

    def check_done(self):
        frame_num_target = self.camera.num_burst_frames
        self.logger.debug(
            "Checking if video acquisition done!  %s\\%s Frames received",
            len(self.current_worker.frame_buffer),
            frame_num_target,
        )

        if 0 < self.num_received_frames == self.last_num_received_frames:
            if self.cycles_w_no_frames >= 3:
                self.no_more_frames = True
            self.cycles_w_no_frames += 1
        else:
            self.last_num_received_frames = self.num_received_frames

        if self.no_more_frames:
            # We aren't receiving frames anymore, so lets save
            if self.num_received_frames >= frame_num_target:
                # We received what we expected
                self.logger.info(
                    "Video acquisition finished for trial %d!", self.num_videos_saved
                )
                self.video_acquisition_emitter.done.emit(False)
            else:
                # We did ont receive what we expected
                self.logger.warning(
                    "Did not receive the expected number of frames for trial %d, but no more have been received! Force saving...",
                    self.num_videos_saved
                )
                self.video_acquisition_emitter.done.emit(True)
            self.num_videos_saved += 1
            self.reset_acquisition_counters()
            self.reset_acquisition()


    def reset_acquisition_counters(self):
        self.num_received_frames = 0
        self.last_num_received_frames = 0
        self.cycles_w_no_frames = 0
        self.no_more_frames =  0

    def shutdown(self):
        self.logger.info("Shutting down all threads!")
        self.stream_timer.stop()
        self.stream_timer = []
        self.video_acquisition_emitter.done.emit(True)
        self.threadpool = []
