from PySide6.QtCore import QTimer, Slot


@Slot()
def update_ui(gui):
    # get camera data here
    data = gui.camera.poll()
    # gui.logger.debug("Polling Camera")
    # gui.logger.debug(data)
    max_fps = gui.calc_max_fps(data["exposure_time"])
    trial_time_s = gui.get_trial_time_s()
    trial_time_frames = gui.s_to_frames(trial_time_s, max_fps)
    gui.update_exposure_time(data["exposure_time"])
    gui.update_MAX_FPS(max_fps)
    gui.update_trial_time_frames(trial_time_frames)
