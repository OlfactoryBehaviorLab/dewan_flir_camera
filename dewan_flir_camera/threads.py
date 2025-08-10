import logging

import numpy as np
from PySide6.QtCore import QTimer, Slot, QRunnable, Signal


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
    error = Signal()
    finished = Signal()
    progress = Signal()
    def __init__(self, save_path: str):
        super().__init__()
        self.save_path: str = save_path
        self.logger = logging.getLogger(__name__)
        self.is_done: bool = False
        self.frame_buffer: list = []
        self.video_writer = []
        self.frame_counter = 0

    @Slot()
    def add_to_buffer(self, image: np.ndarray):
        self.frame_buffer.append(image)

    @Slot()
    def run(self):
        self.logger.info("Thread for %s started!", self.save_path)

    @Slot()
    def stop(self):
        self.is_done = True

    def flush_buffer(self):
        num_frames = len(self.frame_buffer)
        for i in range(self.frame_counter, num_frames):
            pass
        self.frame_counter += num_frames