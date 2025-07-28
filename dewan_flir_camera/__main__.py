from PySpin import SpinnakerException
from pathlib import Path
from time import sleep

from dewan_flir_camera import gui
from spin_system import SpinSystem
from acquisition import ImageHandler
from options import AutoExposureMode, AcquisitionMode, AcquisitionState

import logging

logging.basicConfig(level=logging.DEBUG)

DEFAULT_FPS = 60
DEFAULT_SAVE_DIR = "/flir_recordings"
DEFAULT_EXPERIMENT_DIR = "default_experiment"
DEFAULT_MOUSE_DIR = "default_mouse"

def create_dir_if_not_exist(path, addition, default, logger):

    if path is None or len(str(path)) == 0:
        if addition is None:
            # Create default root dir
            path = default
    else:
        # Existing path is good, but we need to add an addition
        if addition is None or len(addition) == 0:
        # No addition, so use the default addition dir; otherwise, use what the user passed
            addition = default

    if type(path) is not Path:
        path = Path(path)

    if addition is not None:
        path = path.joinpath(addition)

    logger.debug("Creating: %s", path)
    try:
        path.mkdir(parents=True, exist_ok=True)
    except OSError:
        logger.error("Error creating directory %s. Reverting to default directory!", path)

    return path

def create_session_dirs(config_values, logger):
    # Create save dir if needed
    save_dir = create_dir_if_not_exist(config_values["save_dir"], None, DEFAULT_SAVE_DIR, logger)
    experiment_dir = create_dir_if_not_exist(save_dir, config_values["experiment"], DEFAULT_EXPERIMENT_DIR, logger)
    mouse_dir = create_dir_if_not_exist(experiment_dir, config_values["mouse"], DEFAULT_MOUSE_DIR, logger)

    logger.info("Save Dir: %s", mouse_dir)
    return mouse_dir

def main():
    logger = logging.getLogger(__name__)

    app = gui.instantiate_app(logger)
    config_values = gui.get_config(logger)
    mouse_dir = create_session_dirs(config_values, logger)
    image_dir = create_dir_if_not_exist(mouse_dir, "images", None, logger)
    with SpinSystem(logger) as system:
        camera = system.cameras[0]
        camera.init()
        camera.configure_hardware_trigger()
        # Default Parameters to match GUI defaults
        camera.ExposureAuto.SetValue(AutoExposureMode.OFF)  # Manual Mode
        camera.set_acquisition_mode(
            AcquisitionMode.CONTINUOUS
        )  # Continuous Acquisition
        camera.set_exposure(
            gui.ControlWindow.FPS_to_exposure(DEFAULT_FPS)
        )  # Set exposure to default FPS
        ui = gui.ControlWindow(camera, logger)
        event_handler = ImageHandler(image_dir, logger)
        event_handler.image_event_emitter.image_event_signal.connect(ui.display_image)
        camera.register_event_handler(event_handler)

        ui.show()
        _ = app.exec()

        # ui = gui.launch_gui(app, camera, logger)

        # while True:
        #     try:
        #         logger.info("Waiting for trigger!")
        #         camera.trigger_acquisition(AcquisitionState.BEGIN)
        #         event_handler.reset()
        #         wait_for_trigger(event_handler, logger)
        #         camera.trigger_acquisition(AcquisitionState.END)
        #     except KeyboardInterrupt:
        #         camera.trigger_acquisition(AcquisitionState.END)
        #         event_handler.reset()
        #         break


def wait_for_trigger(event_handler, logger, num_frames=100, wait_time_s=0.1):
    try:
        while True:
            logger.info("%s frames captured", event_handler.num_acquired_images)
            sleep(wait_time_s)
            if event_handler.num_acquired_images >= num_frames:
                return
    except SpinnakerException as se:
        print("Error while acquiring images!")
        print(se)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
