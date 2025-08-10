import logging

import numpy as np
from PySide6.QtCore import QTimer, Slot, QRunnable, Signal
import cv2

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
        # gui.logger.debug("Polling Camera")
        # gui.logger.debug(data)
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
    def __init__(self, save_path: str, FPS: int, width: int, height: int):
        super().__init__()
        self.save_path: str = save_path
        self.logger = logging.getLogger(__name__)
        self.video_writer = cv2.VideoWriter(
            self.save_path,
            cv2.VideoWriter.fourcc(*"avc1"),
            FPS,
            (width, height),
            False
        )
        self.is_done: bool = False
        self.frame_buffer: list = []
        self.frame_counter = 0
        self.timer = QTimer()

    @Slot()
    def add_to_buffer(self, image: np.ndarray):
        self.frame_buffer.append(image)

    @Slot()
    def run(self):
        self.logger.info("Thread for %s started!", self.save_path)
        self.timer.timeout.connect(self.timer_callback)

    @Slot()
    def start(self):
        self.timer.start(250)

    @Slot()
    def stop(self):
        self.is_done = True

    def timer_callback(self):
        self.flush_buffer() # Save the images in the buffer
        if self.is_done: # If we're done end the timer
            self.timer.stop()
            self.video_writer.release()
            self.frame_buffer = []

    def flush_buffer(self):
        num_frames = len(self.frame_buffer)
        self.logger.debug("Flushing buffer! %d new frames to flush", num_frames - self.frame_counter)
        for i in range(self.frame_counter, num_frames):
            _image = self.frame_buffer[i].astype('uint8')
            _image_umat = cv2.UMat(cv2.UMat(_image))
            self.video_writer.write(_image_umat)
            self.frame_counter += 1