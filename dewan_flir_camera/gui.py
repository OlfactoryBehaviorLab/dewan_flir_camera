from _ui import about, FLIR
from PySide6.QtWidgets import QMainWindow, QApplication

class ControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_ui = FLIR.MainUI(self)
        self.main_ui.about_widget = about.About()
        self.main_ui.about_widget.hide()


def launch_gui():
    app = QApplication.instance()
    if not app:
        app = QApplication([])

    window = ControlWindow()
    window.show()
    window.main_ui.about_widget.show()
    app.exec()




if __name__ == "__main__":
    launch_gui()
