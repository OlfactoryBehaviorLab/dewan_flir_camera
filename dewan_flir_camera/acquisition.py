from pathlib import Path
from time import sleep
from typing import Union

import PySpin
import numpy as np
from PySpin import ImageEventHandler, ImageProcessor
from PySide6.QtCore import Signal, QObject, QThreadPool

from cam import Cam
from gui import ControlWindow
from options import AcquisitionState, VideoType
from threads import VideoStreamer, VideoStreamWorker


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

        self.do_save = True
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
                if self.do_save:
                    self.save_image(_image)
                if self.display:
                    self.image_event_emitter.image_display_signal.emit(image_ndarray)
                if self.record:
                    self.image_event_emitter.image_record_signal.emit(image_ndarray)

                self.acquired_images += 1
                _image.Release()
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
        done = Signal()
        start = Signal()
        def __init__(self):
            super().__init__()

    def __init__(self, cam, logger, path, file_stem):
        self.camera: Cam = cam
        self.logger: logger = logger
        self.path: Path = path
        self.file_stem: str = file_stem
        self.video_type = VideoType.H264_MP4
        self.video_options = []
        self.num_received_frames = 0
        self.num_videos_saved = 0
        self.video_acquisition_emitter = self.VideoAcquisitionEmitter()
        self.stream_timer = VideoStreamer(self)
        self.threadpool = QThreadPool()
        self.current_worker: VideoStreamWorker = None
        self.event_handler = None

    def start_experiment_video_acquisition(self):
        self.init_new_stream_worker()
        self.camera.trigger_acquisition(AcquisitionState.BEGIN)
        self.stream_timer.start(1000)  # start the stream timer
        self.video_acquisition_emitter.start.emit()

    def end_experiment_video_acquisition(self):
        self.camera.trigger_acquisition(AcquisitionState.END)
        self.stream_timer.stop()

    def init_new_stream_worker(self):
        filename = f"{self.file_stem}-trial-{self.num_videos_saved + 1}.mp4"
        save_path = str(self.path.joinpath(filename))
        fps = self.camera.current_FPS
        width, height = self.camera.frame_size
        self.current_worker = VideoStreamWorker(save_path, fps, width, height)
        self.video_acquisition_emitter.add_to_buffer.connect(self.current_worker.add_to_buffer)
        self.video_acquisition_emitter.done.connect(self.current_worker.stop)
        self.video_acquisition_emitter.start.connect(self.current_worker.start)
        # ImageEvent -> emits image_record_signal -> VideoAcquisition.add_new_frame -> emits add_to_bufer -> VideoStreamWorker.add_to_buffer
        self.threadpool.start(self.current_worker)

    def add_new_frame(self, image):
        self.video_acquisition_emitter.add_to_buffer.emit(image)
        self.num_received_frames += 1


    def reset_acquisition(self):
        self.end_experiment_video_acquisition()
        self.event_handler.reset()
        sleep(0.1)
        self.start_experiment_video_acquisition()

    def check_done(self):
        frame_num_target = self.camera.num_burst_frames
        self.logger.debug("Checking if video acquisition done! Num Frames in buffer: %s\nNum Target Frames: %s", len(self.current_worker.frame_buffer), frame_num_target)
        if self.num_received_frames >= frame_num_target:
            self.logger.info(
                "Video acquisition finished for trial %d!", self.num_videos_saved
            )
            self.video_acquisition_emitter.done.emit()
            self.num_videos_saved += 1
            self.num_received_frames = 0
            self.reset_acquisition()
            