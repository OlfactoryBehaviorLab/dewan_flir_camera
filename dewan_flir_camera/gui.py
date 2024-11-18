import sys

from ._classes.options import AcquisitionMode, AutoExposureMode
from ._ui import about, FLIR
from . import threads
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
        self.main_ui.s_per_trial_val.valueChanged.connect(self.trial_time_s_changed_callback)

        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(lambda: threads.update_ui(self))
        self.update_timer.start(100)  # Poll rate in ms



    @staticmethod
    def calc_max_fps(exposure_time_us):
        exposure_time_s = exposure_time_us / 100000
        if exposure_time_s and exposure_time_s > 0:
            return round(1 / exposure_time_s, 2)
        else:
            return -1

    @staticmethod
    def s_to_frames(seconds, FPS):
        return round(seconds * FPS)

    def get_trial_time_s(self):
        return round(float(self.main_ui.s_per_trial_val.value()) , 2)

    def update_exposure_time(self, time: int):
        self.main_ui.current_exposure_data.setText(str(time))

    def update_MAX_FPS(self, fps: int):
        self.main_ui.max_fps_data.setText(str(fps))

    def update_current_fps(self, fps: int):
        self.main_ui.current_fps_data.setText(str(fps))

    def update_trial_time_s(self, trial_time: float):
        self.main_ui.s_per_trial_data.setText(str(trial_time))

    def update_trial_time_frames(self, frames: int):
        self.main_ui.num_frames_data.setText(str(frames))

    def acquisition_mode_changed_callback(self):
        index = self.main_ui.acquisition_mode_data.currentIndex()
        acquisition_mode = AcquisitionMode(index)
        self.camera.set_acquisition_mode(acquisition_mode)

    def exposure_mode_changed_callback(self):
        index = self.main_ui.exposure_mode.currentIndex()
        exposure_mode = AutoExposureMode(index)
        self.camera.set_exposure_mode(exposure_mode)

        if index != 0:
            self.main_ui.exposure_apply.setEnabled(False)
            self.main_ui.exposure_value.setEnabled(False)
        else:
            self.main_ui.exposure_apply.setEnabled(True)
            self.main_ui.exposure_value.setEnabled(True)

    def exposure_apply_callback(self):
        new_value = self.main_ui.exposure_value.value()
        new_value = int(new_value)
        new_time = self.camera.set_exposure(new_value)  # Just incase the camera bounds the user's input
        self.main_ui.exposure_value.setValue(new_time)

    def trial_time_s_changed_callback(self):
        trial_time_s = self.get_trial_time_s()
        self.update_trial_time_s(trial_time_s)

    def start_button_callback(self):
        pass

    def stop_button_callback(self):
        pass

    def arm_button_callback(self):
        pass

    def capture_button_callback(self):
        self.camera.capture_single_frame()

    def open_action_callback(self):
        pass

    def save_action_callback(self):
        pass

    def save_as_action_callback(self):
        pass


def launch_gui(camera=None):
    if not camera:
        raise ValueError('A camera must be passed to the GUI!')

    sys.argv += ['-platform', 'windows:darkmode=2']

    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.setStyle('fusion')

    window = ControlWindow(camera)
    window.show()
    _ = app.exec()

