import logging
import pathlib
import time

import numpy as np
from PySide6.QtCore import QTimer, Slot, QRunnable, Signal, QObject
import cv2

OPENH264_LIB_PATH = "./lib/openh264-1.8.0/openh264-1.8.0-win64.dll"

class UpdateTimer(QTimer):
    def __init__(self, gui):
        super().__init__()
        self.timer = QTimer(gui)
        self.timer.timeout.connect(lambda: self.update_ui(gui))
        self.timer.start(100)

    @Slot()
    def update_ui(self, gui):
        # get camera data here
        data = gui.camera.poll()
        max_fps = gui.calc_max_fps(data["exposure_time"])
        trial_time_s = gui.get_trial_time_s()
        trial_time_frames = gui.s_to_frames(trial_time_s, max_fps)
        gui.update_exposure_time(data["exposure_time"])
        gui.update_MAX_FPS(max_fps)
        gui.update_trial_time_frames(trial_time_frames)


class VideoStreamer(QTimer):
    def __init__(self, video_acquisition_handler):
        super().__init__()
        self.timeout.connect(video_acquisition_handler.check_done)


class VideoStreamWorker(QRunnable):

    def __init__(self, save_path: pathlib.Path, FPS: int, width: int, height: int, logger):
        import os
        from pathlib import Path
        os.environ["OPENH264_LIBRARY"] = str(Path(OPENH264_LIB_PATH).absolute())

        super().__init__()
        self.save_path: pathlib.Path = save_path
        self.logger = logging.getLogger(__name__)
        self.video_writer = cv2.VideoWriter(
            str(self.save_path), cv2.VideoWriter.fourcc(*"avc1"), FPS, (width, height), False
        )
        self.is_done: bool = False
        self.force_stop: bool = False
        self.exit_thread: bool = False
        self.frame_buffer: list = []
        self.frame_counter: int = 0
        self.setAutoDelete(True)

    @Slot()
    def add_to_buffer(self, image: np.ndarray):
        self.frame_buffer.append(image)

    @Slot()
    def run(self):
        self.logger.info("Thread for %s started!", self.save_path)
        # Let's just use this
        while not self.exit_thread:
            self.timer_callback()
            time.sleep(0.5)

        self.logger.info("Thread for %s ended!", self.save_path)

    @Slot(bool)
    def stop(self, force_stop):
        self.is_done = True
        self.force_stop = force_stop

    def timer_callback(self):
        self.flush_buffer()  # Save the images in the buffer
        if self.is_done:  # If we're done release the writer
            self.video_writer.release()
            self.frame_buffer = []
            self.exit_thread = True

            if self.force_stop:
                new_path = self.save_path.with_stem(self.save_path.stem + "-INCOMPLETE")
                self.save_path.replace(new_path)

    def flush_buffer(self):
        num_frames = len(self.frame_buffer)
        self.logger.debug(
            f"Flushing buffer! {num_frames - self.frame_counter} new frames to flush"
        )
        for i in range(self.frame_counter, num_frames):
            _image = self.frame_buffer[i].astype("uint8")
            _image_umat = cv2.UMat(cv2.UMat(_image))
            self.video_writer.write(_image_umat)
            self.frame_counter += 1
