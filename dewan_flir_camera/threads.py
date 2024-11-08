from PySide6.QtCore import QTimer, Slot


@Slot()
def update_ui(gui):
    import numpy as np
    # get camera data here
    data = {
        'exposure_time': np.random.randint(100000),
        'fps': np.random.randint(300),
    }

    gui.update_exposure_time(data['exposure_time'])
    gui.update_current_fps(data['fps'])
    max_fps = gui._calc_max_fps(data['exposure_time'])
    gui.update_MAX_FPS(max_fps)
    # TODO: get trial_time_s value and multiply it by FPS to get frames.