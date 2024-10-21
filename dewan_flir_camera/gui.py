import sys

import about
import FLIR
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer, Slot


class ControlWindow(QMainWindow):
    def __init__(self, camera):
        super().__init__()
        self.camera = camera
        self.main_ui = FLIR.MainUI(self)
        self.main_ui.about_widget = about.About()

        self.main_ui.actionAbout.triggered.connect(self.main_ui.about_widget.show)
        self.main_ui.actionOpen.triggered.connect(self.open_action_callback)
        self.main_ui.actionSave.triggered.connect(self.save_action_callback)
        self.main_ui.actionSave_As.triggered.connect(self.save_as_action_callback)

        self.main_ui.start_button.clicked.connect(self.start_button_callback)
        self.main_ui.stop_button.clicked.connect(self.stop_button_callback)
        self.main_ui.arm_button.clicked.connect(self.arm_button_callback)
        self.main_ui.capture_button.clicked.connect(self.capture_button_callback)

        self.main_ui.acquisition_mode_data.currentTextChanged.connect(self.acquisition_mode_changed_callback)
        self.main_ui.exposure_mode.currentTextChanged.connect(self.exposure_mode_changed_callback)
        self.main_ui.exposure_apply.clicked.connect(self.exposure_apply_callback)
        self.main_ui.s_per_trial_val.valueChanged.connect(self.exposure_apply_callback)

        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_ui)
        self.update_timer.start(100)

    @Slot()
    def update_ui(self):
        import numpy as np
        # get camera data here
        data = {
            'exposure_time': np.random.randint(100000),
            'fps': np.random.randint(300),
        }

        self.update_exposure_time(data['exposure_time'])
        self.update_current_fps(data['fps'])
        max_fps = self._calc_max_fps(data['exposure_time'])
        self.update_MAX_FPS(max_fps)
        # TODO: get trial_time_s value and multiply it by FPS to get frames.


    @staticmethod
    def _calc_max_fps(exposure_time_us):
        exposure_time_s = exposure_time_us / 100000
        return round(1 / exposure_time_s)

    def update_exposure_time(self, time: int):
        self.main_ui.current_exposure_data.setText(str(time))

    def update_MAX_FPS(self, fps: int):
        self.main_ui.max_fps_data.setText(str(fps))

    def update_current_fps(self, fps: int):
        self.main_ui.current_fps_data.setText(str(fps))

    def update_trial_time_s(self, trial_time: int):
        self.main_ui.s_per_trial_data.setText(str(trial_time))

    def update_trial_time_frames(self, frames):
        self.main_ui.num_frames_data.setText(str(frames))

    def acquisition_mode_changed_callback(self):
        pass

    def exposure_mode_changed_callback(self):
        pass

    def exposure_apply_callback(self):
        pass

    def start_button_callback(self):
        pass

    def stop_button_callback(self):
        pass

    def arm_button_callback(self):
        pass

    def capture_button_callback(self):
        pass

    def open_action_callback(self):
        pass

    def save_action_callback(self):
        pass

    def save_as_action_callback(self):
        pass


def launch_gui(camera):
    sys.argv += ['-platform', 'windows:darkmode=2']

    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.setStyle('fusion')

    window = ControlWindow(camera)
    window.show()
    app.exec()