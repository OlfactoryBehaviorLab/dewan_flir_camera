from ..UI import FLIR, about
from PySide6.QtWidgets import QApplication, QMainWindow

class ControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = FLIR.MainUI(self)
        self.main_ui.about_widget = about.Ui_about
