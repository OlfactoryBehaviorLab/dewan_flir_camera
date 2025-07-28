from pathlib import Path
from typing import Union

import PySpin
import numpy as np
from PySpin import ImageEventHandler, ImageProcessor, SpinnakerException
from PySide6.QtCore import Signal, QObject

class ImageHandler(ImageEventHandler):
    class ImageEventEmitter(QObject):
        image_event_signal = Signal(np.ndarray)
        def __init__(self):
            super().__init__()
    def __init__(self, save_dir: Union[str, Path], logger):
        super().__init__()
        self.logger = logger
        self.save_dir = save_dir
        self.acquired_images = 0
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
        import time
        start_time = time.time()
        if image.IsIncomplete():
            self.logger.error("Image Incomplete!: %s", image.GetImageStatus())
        else:
            try:
                convert_time_start = time.time()
                _image = self._image_processor.Convert(image, PySpin.PixelFormat_Mono8)
                convert_end_time = time.time()
                self.logger.debug("Image Event @ %s, delay: %s", start_time, convert_time_start-start_time)
                self.logger.debug("Convert image @ %s, duration: %s", convert_time_start, convert_end_time-convert_time_start)
                nd_array_time_start = time.time()
                _image_to_display = _image.GetNDArray()
                nd_array_time_end = time.time()
                self.logger.debug("Convert to ndarray @ %s, duration: %s", nd_array_time_start, nd_array_time_end-nd_array_time_start)
                self.logger.debug("Emit signal @ %s", time.time())
                self.image_event_emitter.image_event_signal.emit(_image_to_display)
                _filename = f"image-{self.num_acquired_images}.jpg"
                _file_path = self.save_dir.joinpath(_filename)
                _image.Save(str(_file_path))
                self.acquired_images += 1
                _image.Release()
            except Exception as se:
                self.logger("Error saving image")

    def reset(self):
        self.acquired_images = 0

    @property
    def num_acquired_images(self):
        return self.acquired_images


