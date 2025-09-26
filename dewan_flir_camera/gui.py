import logging
import sys
from pathlib import Path
import numpy as np
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from dewan_flir_camera import cam

from dewan_flir_camera import threads
from dewan_flir_camera.options import (
    AcquisitionMode,
    AutoExposureMode,
    AcquisitionState,
)
from dewan_flir_camera.ui import (
    about,
    FLIR,
    config,
)

from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QFileDialog, QWidget, QDialog

DEFAULT_DIR = "./"

logger = logging.getLogger(__name__)

class ControlWindow(QMainWindow):
    def __init__(self, camera, video_acquisition_handler):
        super().__init__()
        self.camera: cam.Cam = camera
        self.video_acquisition_handler = video_acquisition_handler

        self.main_ui: FLIR.MainUI = FLIR.MainUI(self)
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
        self.main_ui.trigger_button.clicked.connect(self.trigger_button_callback)

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
        self.main_ui.trigger_source_selection.currentIndexChanged.connect(
            self.trigger_selection_changed_callback
        )

        # Update GUI to reflect default parameters set in __main__
        self.update_trial_time_s(self.main_ui.s_per_trial_val.value())
        self.update_trial_time_frames(
            self.s_to_frames(
                self.main_ui.s_per_trial_val.value(),
                int(self.main_ui.max_fps_data.text()),
            )
        )

        self.update_timer = threads.UpdateTimer(self)

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
        logger.debug("Acquisition mode changed to: %s", acquisition_mode)

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
        logger.debug("Exposure mode set to %s: index %s", exposure_mode, index)

    def exposure_apply_callback(self):
        new_value = self.main_ui.exposure_value.value()
        new_value = int(new_value)
        new_time = self.camera.set_exposure(
            new_value
        )  # Just incase the camera bounds the user's input
        try:
            self.main_ui.exposure_value.setValue(new_time)
            logger.debug("Exposure value set to %s", new_value)
        except (TypeError, ValueError):
            logger.error("%s is not a valid value for setValue!", new_time)

    def trial_time_s_changed_callback(self):
        trial_time_s = self.get_trial_time_s()
        self.update_trial_time_s(trial_time_s)
        max_fps = self.calc_max_fps(self.camera.exposure)
        num_burst_frames = self.s_to_frames(trial_time_s, max_fps)
        self.camera.set_num_burst_frames(num_burst_frames)

    def trigger_selection_changed_callback(self):
        logger.debug("Trigger selection changed callback")

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
        current_arm_state = self.camera.armed

        if current_arm_state:
            self.camera.armed = False
            self.set_gui_state(True)
            self.main_ui.arm_button.setText("ARM TRIGGER")
            self.video_acquisition_handler.end_experiment_video_acquisition()
        else:
            self.camera.armed = True
            self.set_gui_state(False)
            self.main_ui.arm_button.setText("TRIGGER ARMED")
            self.video_acquisition_handler.start_experiment_video_acquisition()

    def trigger_button_callback(self):
        self.camera.capture_single_frame()

    def open_action_callback(self):
        pass

    def save_action_callback(self):
        pass

    def save_as_action_callback(self):
        pass

    def set_gui_state(self, state: bool):
        self.main_ui.start_button.setEnabled(state)
        self.main_ui.trigger_button.setEnabled(state)
        self.main_ui.exposure_apply.setEnabled(state)
        self.main_ui.exposure_mode.setEnabled(state)
        self.main_ui.acquisition_mode.setEnabled(state)
        self.main_ui.s_per_trial.setEnabled(state)
        self.main_ui.exposure_value.setEnabled(state)

    @Slot(np.ndarray)
    def display_image(self, image):
        try:
            q_image = QImage(
                image, image.shape[1], image.shape[0], QImage.Format.Format_Grayscale8
            )
            pixmap = QPixmap().fromImage(q_image)
            self.scene.clear()
            self.scene.addPixmap(pixmap)
            self.main_ui.viewport.fitInView(pixmap.rect())
        except Exception as e:
            logger.error(e)


class ConfigDialog:
    def __init__(self, default_save_dir: str):
        self.config_ui = config.Ui_config_wizard()
        # self.config_ui.mouse_ID_field.textEdited.connect(self.verify_ID)
        # self.config_ui.experiment_type_field.textEdited.connect(self.verify_exp)
        # self.config_ui.save_path_field.textEdited.connect(self.verify_user_path)
        self.DEFAULT_SAVE_DIR = default_save_dir
        self.config_ui.open_dir_button.clicked.connect(self.get_save_dir)

    def get_save_dir(self):
        save_dir = QFileDialog.getExistingDirectory(
            self.config_ui,
            "Select save directory",
            self.DEFAULT_SAVE_DIR,
            QFileDialog.Option.ShowDirsOnly
        )

        if save_dir is not None and len(save_dir) > 0:
            self.config_ui.save_path_field.setText(save_dir)
        else:
            self.config_ui.save_path_field.setText(self.DEFAULT_SAVE_DIR)


    def get_experiment_config(self) -> dict:
        config_return = self.config_ui.exec()
        if config_return == 1:
            configuration = {
                "mouse": self.config_ui.mouse_ID_field.text(),
                "experiment": self.config_ui.experiment_type_field.text(),
                "save_dir": self.config_ui.save_path_field.text(),
            }
        else:
            logger.error("Configuration UI returned 0! Setting default values")
            configuration = {
                "mouse": '9999',
                "experiment": "none_specified",
                "save_dir": Path(DEFAULT_DIR),
            }
        logger.debug("Configuration UI returned %s", configuration)
        return configuration

    def verify_ID(self):
        logger.debug("Verifying ID: %s", self.config_ui.mouse_ID_field)

    def verify_exp(self):
        logger.debug(
            "Verifying Experiment: %s", self.config_ui.experiment_type_field
        )

    def verify_user_path(self):
        logger.debug("Verifying Path: %s", self.config_ui.save_path_field)


def instantiate_app():
    sys.argv += ["-platform", "windows:darkmode=2"]
    if logger:
        logger.debug("Instantiating QApplication")
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.setStyle("fusion")

    return app


def get_config(logger, default_save_dir: str):
    # Blocking get config values
    config_dialog = ConfigDialog(logger, default_save_dir)
    return config_dialog.get_experiment_config()


def launch_gui(app: QApplication, camera, logger):
    if not camera:
        raise ValueError("A camera must be passed to the GUI!")

    window = ControlWindow(camera, logger)
    window.show()
    _ = app.exec()
