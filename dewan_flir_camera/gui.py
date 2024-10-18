from _ui.control import ControlWindow

from PySide6.QtWidgets import QApplication

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
