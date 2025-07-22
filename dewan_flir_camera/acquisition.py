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
        if image.IsIncomplete():
            self.logger.error("Image Incomplete!: %s", image.GetImageStatus())
        else:
            try:
                _image = self._image_processor.Convert(image, PySpin.PixelFormat_Mono8)
                _image_to_display = _image.GetNDArray()
                self.image_event_emitter.image_event_signal.emit(_image_to_display)
                #
                # _filename = f"image-{self.num_acquired_images}.jpg"
                # _file_path = self.save_dir.joinpath(_filename)
                # _image.Save(str(_file_path))
                # print(f'Saved image: {_file_path}')
                self.acquired_images += 1
                _image.Release()
            except Exception as se:
                self.logger("Error saving image")

    def reset(self):
        self.acquired_images = 0

    @property
    def num_acquired_images(self):
        return self.acquired_images


