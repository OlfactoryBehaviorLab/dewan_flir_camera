import sys

from pathlib import Path

import numpy as np
from PySide6.QtGui import QImage, QPixmap

from dewan_flir_camera.options import (
    AcquisitionMode,
    AutoExposureMode,
    AcquisitionState,
)
from dewan_flir_camera.ui import about, FLIR, config
from dewan_flir_camera import threads, cam
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene
from PySide6.QtCore import Slot, QTimer

DEFAULT_DIR = './'

class ControlWindow(QMainWindow):
    def __init__(self, camera, logger):
        super().__init__()
        self.logger = logger
        self.camera: cam.Cam = camera
        self.main_ui = FLIR.MainUI(self)
        self.main_ui.about_widget = about.About()

        self.scene = QGraphicsScene()
        self.main_ui.viewport.setScene(self.scene)

        self.main_ui.actionAbout.triggered.connect(self.main_ui.about_widget.show)
        self.main_ui.actionOpen.triggered.connect(self.open_action_callback)
        self.main_ui.actionSave.triggered.connect(self.save_action_callback)
        self.main_ui.actionSave_As.triggered.connect(self.save_as_action_callback)
        self.main_ui.actionExit.triggered.connect(self.close)

        self.main_ui.start_button.clicked.connect(self.start_button_callback)
        self.main_ui.arm_button.clicked.connect(self.arm_button_callback)
        self.main_ui.capture_button.clicked.connect(self.capture_button_callback)

        self.main_ui.acquisition_mode_data.currentTextChanged.connect(
            self.acquisition_mode_changed_callback
        )
        self.main_ui.exposure_mode.currentTextChanged.connect(
            self.exposure_mode_changed_callback
        )
        self.main_ui.exposure_apply.clicked.connect(self.exposure_apply_callback)
        self.main_ui.s_per_trial_val.valueChanged.connect(
            self.trial_time_s_changed_callback
        )

        # Update GUI to reflect default parameters set in __main__
        self.update_trial_time_s(self.main_ui.s_per_trial_val.value())
        self.update_trial_time_frames(
            self.s_to_frames(
                self.main_ui.s_per_trial_val.value(),
                int(self.main_ui.max_fps_data.text()),
            )
        )
        # The other camera fields are automatically updated by the timer
        # This is the only one we need to pull from the camera
        self.main_ui.exposure_value.setValue(int(self.camera.get_exposure()))
        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(lambda: threads.update_ui(self))
        self.update_timer.start(100)  # Poll rate in ms

    @staticmethod
    def calc_max_fps(exposure_time_us):
        exposure_time_s = exposure_time_us / 1000000
        if exposure_time_s and exposure_time_s > 0:
            return round(1 / exposure_time_s, 2)
        else:
            return -1

    @staticmethod
    def s_to_frames(seconds, FPS):
        return round(seconds * FPS)

    @staticmethod
    def FPS_to_exposure(FPS: int) -> int:
        """
        Converts FPS to exposure time (uS per frame) using 1/FPS * 1E6us/s
        :param FPS: (int) FPS to convert to uS
        :return: (int) exposure time in uS
        """
        return int(round((1 / FPS) * 1e6, 1))

    def get_trial_time_s(self):
        return round(float(self.main_ui.s_per_trial_val.value()), 2)

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
            self.logger.debug("Exposure mode set to %s: index %s", exposure_mode, index)
            self.main_ui.exposure_apply.setEnabled(True)
            self.main_ui.exposure_value.setEnabled(True)

    def exposure_apply_callback(self):
        new_value = self.main_ui.exposure_value.value()
        new_value = int(new_value)
        new_time = self.camera.set_exposure(
            new_value
        )  # Just incase the camera bounds the user's input
        try:
            self.main_ui.exposure_value.setValue(new_time)
        except (TypeError, ValueError) as ve:
            self.logger.error("%s is not a valid value for setValue!", new_time)

    def trial_time_s_changed_callback(self):
        trial_time_s = self.get_trial_time_s()
        self.update_trial_time_s(trial_time_s)
        max_fps = self.calc_max_fps(self.camera.exposure)
        num_burst_frames = self.s_to_frames(trial_time_s, max_fps)
        self.camera.set_num_burst_frames(num_burst_frames)

    def start_button_callback(self):
        current_state = self.camera.acquisition_state

        if (
            current_state == AcquisitionState.BEGIN
            and self.camera.trigger_acquisition(AcquisitionState.END)
            == AcquisitionState.END
        ):
            self.main_ui.start_button.setText("START ACQUISITION")
            self.main_ui.start_button.setStyleSheet(
                "QPushButton{\n"
                "background-color: rgb(0, 85, 0);\n"
                "color:rgb(255,255,255);\n"
                "}\n"
                "QPushButton::hover{\n"
                "background-color: rgb(0, 85, 0);\n"
                "    border-color: rgb(60, 231, 195);\n"
                "    border-style: outset;\n"
                "    color: rgb(255,255,255);\n"
                "    border-width: 2px;\n"
                "    border-radius: 12px;\n"
                "    padding: 6px;\n"
                "}\n"
                "QPushButton::pressed{\n"
                "background-color: rgb(0, 60, 0);\n"
                "color:rgb(255,255,255);\n"
                "}"
            )
        if (
            current_state == AcquisitionState.END
            and self.camera.trigger_acquisition(AcquisitionState.BEGIN)
            == AcquisitionState.BEGIN
        ):
            self.main_ui.start_button.setText("END ACQUISITION")
            self.main_ui.start_button.setStyleSheet(
                "QPushButton{\n"
                "background-color: rgb(170, 0, 0);\n"
                "color:rgb(255,255,255);\n"
                "}\n"
                "QPushButton::hover{\n"
                "background-color: rgb(170, 0, 0);\n"
                "    border-color: rgb(60, 231, 195);\n"
                "    border-style: outset;\n"
                "    color: rgb(255,255,255);\n"
                "    border-width: 2px;\n"
                "    border-radius: 12px;\n"
                "    padding: 6px;\n"
                "}\n"
                "QPushButton::pressed{\n"
                "background-color: rgb(150, 0, 0);\n"
                "color:rgb(255,255,255);\n"
                "}"
            )

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

    @Slot(np.ndarray)
    def display_image(self, image):
        try:
            q_image = QImage(image, image.shape[1], image.shape[0],
                             QImage.Format.Format_Grayscale8)
            pixmap = QPixmap().fromImage(q_image)
            self.scene.clear()
            self.scene.addPixmap(pixmap)
            self.main_ui.viewport.fitInView(pixmap.rect())
        except Exception as e:
            self.logger.error(e)


class ConfigDialog:
    def __init__(self, logger):
        self.logger = logger
        self.config_ui = config.Ui_config_wizard()
        # self.config_ui.mouse_ID_field.textEdited.connect(self.verify_ID)
        # self.config_ui.experiment_type_field.textEdited.connect(self.verify_exp)
        # self.config_ui.save_path_field.textEdited.connect(self.verify_user_path)

    def get_experiment_config(self) -> dict:
        config_return = self.config_ui.exec()
        if config_return == 1:
            configuration = {
                'mouse': self.config_ui.mouse_ID_field.text(),
                'experiment': self.config_ui.experiment_type_field.text(),
                'save_dir': self.config_ui.save_path_field.text(),
            }
        else:
            self.logger.error("Configuration UI returned 0! Setting default values")
            configuration = {
                'mouse': 1,
                'experiment': 'none_specified',
                'save_dir': Path(DEFAULT_DIR)
            }
        self.logger.debug("Configuration UI returned %s", configuration)
        return configuration

    def verify_ID(self):
        self.logger.debug("Verifying ID: %s", self.config_ui.mouse_ID_field)

    def verify_exp(self):
        self.logger.debug("Verifying Experiment: %s", self.config_ui.experiment_type_field)

    def verify_user_path(self):
        self.logger.debug("Verifying Path: %s", self.config_ui.save_path_field)


def instantiate_app(logger=None):
    sys.argv += ["-platform", "windows:darkmode=2"]

    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.setStyle("fusion")

    return app

def get_config(logger):
    # Blocking get config values
    config_dialog = ConfigDialog(logger)
    return config_dialog.get_experiment_config()


def launch_gui(app: QApplication, camera=None, logger=None):
    if not camera:
        raise ValueError("A camera must be passed to the GUI!")

    window = ControlWindow(camera, logger)
    window.show()
    _ = app.exec()
