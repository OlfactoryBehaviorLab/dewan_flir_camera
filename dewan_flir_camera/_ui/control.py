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