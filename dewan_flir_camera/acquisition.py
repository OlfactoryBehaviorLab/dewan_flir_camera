from pathlib import Path
from time import sleep
from typing import Union

import PySpin
import numpy as np
from PySpin import ImageEventHandler, ImageProcessor
from PySide6.QtCore import Signal, QObject

from gui import ControlWindow
from options import AcquisitionState, VideoType
from threads import VideoStreamer


class ImageHandler(ImageEventHandler):
    class ImageEventEmitter(QObject):
        image_event_signal = Signal(np.ndarray)

        def __init__(self):
            super().__init__()

    def __init__(self, save_dir: Union[str, Path], logger, video_acquisition_handler):
        super().__init__()
        self.logger = logger
        self.save_dir = save_dir
        self.acquired_images = 0

        self.do_save = True
        self.display = True
        self.record = True

        self.video_processor: VideoAcquisition = video_acquisition_handler
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
                    self.image_event_emitter.image_event_signal.emit(image_ndarray)
                if self.record:
                    self.video_processor.add_new_frame(_image)

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
    def __init__(self, cam, logger, path, file_stem):
        self.camera = cam
        self.logger: logger = logger
        self.path: Path = path
        self.file_stem: str = file_stem
        self.video_type = VideoType.H264_MP4
        self.video_options = []
        self.num_received_frames = 0
        self.num_videos_saved = 0
        self.stream_timer = VideoStreamer(self)
        self.video_writer = PySpin.SpinVideo()

        self.event_handler = None
        self.frame_buffer: list = []

    def start_experiment_video_acquisition(self):
        self.set_video_writer_options()
        self.camera.trigger_acquisition(AcquisitionState.BEGIN)
        self.stream_timer.start(1000)  # start the stream timer

    def end_experiment_video_acquisition(self):
        self.camera.trigger_acquisition(AcquisitionState.END)
        self.stream_timer.stop()

    def add_new_frame(self, image):
        self.frame_buffer.append(image)
        self.num_received_frames += 1

    def reset_acquisition(self):
        self.camera.trigger_acquisition(AcquisitionState.END)
        self.event_handler.reset()
        sleep(0.01)
        self.camera.trigger_acquisition(AcquisitionState.BEGIN)


    def check_done(self):
        frame_num_target = self.camera.num_burst_frames
        # self.logger.debug("Checking if video acquisition done! Num Frames in buffer: %s\nNum Target Frames: %s", len(self.frame_buffer), frame_num_target)
        if self.num_received_frames >= frame_num_target:
            self.logger.info(
                "Video acquisition finished for trial %d!", self.num_videos_saved
            )
            self.save_buffer()
            self.num_videos_saved += 1
            self.num_received_frames = 0
            self.reset_acquisition()
            