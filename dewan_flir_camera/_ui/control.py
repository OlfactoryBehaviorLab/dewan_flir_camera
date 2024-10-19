import about
import FLIR
from PySide6.QtWidgets import QMainWindow


class ControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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

    def update_exposure_time(self, time: int):
        self.main_ui.current_exposure_data.setText(time)

    def update_MAX_FPS(self, fps: int):
        self.main_ui.max_fps_data.setText(fps)

    def update_current_fps(self, fps: int):
        self.main_ui.current_fps_data.setText(fps)

    def update_trial_time_s(self, trial_time: int):
        self.main_ui.s_per_trial_data.setText(trial_time)

    def update_trial_time_frames(self, frames):
        self.main_ui.num_frames_data.setText(frames)

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
