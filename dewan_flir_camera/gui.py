import sys
from PySide6.QtWidgets import QApplication
from _ui.control import ControlWindow


def launch_gui():
    sys.argv += ['-platform', 'windows:darkmode=2']

    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.setStyle('fusion')

    window = ControlWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    launch_gui()
