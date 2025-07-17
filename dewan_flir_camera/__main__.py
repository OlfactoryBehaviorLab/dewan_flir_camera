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

def create_dir_if_not_exist(path, default, logger):
    if path is None or len(str(path)) == 0:
        path = default

    if type(path) is not Path:
        path = Path(path)

    if not path.exists():
        try:
            path.mkdir(parents=True)
        except OSError:
            logger.error("Error creating directory %s. Reverting to default directory!", path)
            new_path = Path(default)
            new_path.mkdir(parents=True, exist_ok=True)
            return new_path
    return path

def create_session_dirs(config_values, logger):
    # Create save dir if needed
    save_dir = create_dir_if_not_exist(config_values["save_dir"], DEFAULT_SAVE_DIR, logger)
    _full_default_experiment = save_dir.joinpath(DEFAULT_EXPERIMENT_DIR)
    _dir_to_create = save_dir.joinpath(config_values["experiment"])
    experiment_dir = create_dir_if_not_exist(_dir_to_create, _full_default_experiment, logger)
    _full_default_mouse = experiment_dir.joinpath(DEFAULT_MOUSE_DIR)
    _dir_to_create = experiment_dir.joinpath(config_values["mouse"])
    mouse_dir = create_dir_if_not_exist(_dir_to_create, _full_default_mouse, logger)

    logger.debug("Save Dir: %s", mouse_dir)
    return mouse_dir

def main():
    logger = logging.getLogger(__name__)

    app = gui.instantiate_app(logger)
    config_values = gui.get_config(logger)
    mouse_dir = create_session_dirs(config_values, logger)

    with SpinSystem(logger) as system:
        camera = system.cameras[0]
        event_handler = ImageHandler("./images")
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
        camera.register_event_handler(event_handler)


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
