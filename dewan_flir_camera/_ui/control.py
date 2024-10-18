import about, FLIR
from PySide6.QtWidgets import QMainWindow

class ControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = FLIR.MainUI(self)
        self.main_ui.about_widget = about.About()
        self.main_ui.about_widget.hide()
