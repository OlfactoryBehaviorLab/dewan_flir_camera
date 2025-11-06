"""Main entry point for dewan_flir_camera module"""

import datetime
import logging
from pathlib import Path
from typing import Optional
from dewan_flir_camera import gui
from dewan_flir_camera.spin_system import SpinSystem
from dewan_flir_camera.acquisition import ImageHandler, VideoAcquisition
from dewan_flir_camera.options import AutoExposureMode, AcquisitionMode, TriggerAction

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Some sane defaults
DEFAULT_FPS = 30
DEFAULT_TRIAL_TIME_S = 10
DEFAULT_SAVE_DIR = "D:/flir_recordings"
DEFAULT_EXPERIMENT_DIR = "default_experiment"
DEFAULT_MOUSE_DIR = "default_mouse"


def create_dir_if_not_exist(
    default: str, root_path: Optional[str | Path], addition: Optional[str]
) -> Path:
    """Creates directory if it doesn't exist

    This function will create a directory or directory tree with a user-supplied addition. If the user does not
    supply the path/addition, a user-supplied default will be used.

    Parameters
    ----------
    default : str
        Default value to use if path or addition are not provided
    root_path : str or Path (optional)
        Path to directory or directory tree to create
    addition : str (optional)
        Value to append to end of path

    Returns
    -------
    Path
        Finalize path that was constructed from the parameters and created on disk

    """
    if root_path is None or len(str(root_path)) == 0:
        if addition is None:
            # Create default root dir
            root_path = default
    else:
        # Existing path is good, but we need to add an addition
        if addition is None or len(addition) == 0:
            # No addition, so use the default addition dir; otherwise, use what the user passed
            addition = default

    if type(root_path) is not Path:
        root_path = Path(root_path)

    if addition is not None:
        root_path = root_path.joinpath(addition)

    try:
        logger.debug("Attempting to creating: %s", root_path)
        root_path.mkdir(parents=True, exist_ok=True)
    except OSError:
        logger.error(
            "Error creating directory %s. Reverting to default directory!", root_path
        )

    return root_path


def create_session_dirs(config_values: dict) -> tuple[Path, str]:
    """Creates directories from user-supplied paths and names

    Parameters
    ----------
    config_values : dict
        Dictionary of user-supplied animal name, experiment name, and save path

    Returns
    -------
    tuple[Path, str]
        Returns tuple containing the full save path for this animal-experiment combination and
        the stem of the save directory

    """
    # Create save dir if needed
    save_dir = create_dir_if_not_exist(
        DEFAULT_SAVE_DIR, config_values["save_dir"], None
    )
    experiment_dir = create_dir_if_not_exist(
        DEFAULT_EXPERIMENT_DIR, save_dir, config_values["experiment"]
    )
    experiment_stem = experiment_dir.stem
    mouse_dir = create_dir_if_not_exist(
        DEFAULT_MOUSE_DIR, experiment_dir, config_values["mouse"]
    )

    formatted_date = datetime.datetime.today().strftime("%m-%d-%Y-%H-%M-%S")

    save_dir = create_dir_if_not_exist(
        formatted_date, mouse_dir, None
    )
    mouse_stem = mouse_dir.stem

    file_stem = f"{mouse_stem}-{experiment_stem}"
    logger.info("Save Dir: %s", save_dir)
    return save_dir, file_stem


def initialize(camera, UI: gui.ControlWindow):
    """ Sets defaults for camera object and main UI

    Parameters
    ----------
    camera : Camera
        Camera object to configure with defaults
    UI : gui.ControlWindow
        Main UI to configure based on the camera defaults

       """
    # === DEFAULT CAMERA CONFIGURATION === #
    camera.set_acquisition_mode(AcquisitionMode.MULTI)  # Multiframe/Burst Acquisition
    camera.configure_hardware_trigger(TriggerAction.CONTINUOUS)  # Configure hardware trigger
    camera.ExposureAuto.SetValue(AutoExposureMode.OFF)  # Manual Exposure Mode
    camera.set_exposure(
        gui.ControlWindow.FPS_to_exposure(DEFAULT_FPS)
    )  # Set exposure to default FPS
    num_burst_frames = DEFAULT_FPS * DEFAULT_TRIAL_TIME_S
    camera.set_num_burst_frames(num_burst_frames)

    # === DEFAULT GUI CONFIGURATION === #
    # The other camera fields are automatically updated by the timer
    # This is the only one we need to pull from the camera #TODO: make this dynamically updated as well
    UI.main_ui.exposure_value.setValue(int(camera.exposure))
    UI.main_ui.acquisition_mode_data.setCurrentIndex(AcquisitionMode.MULTI)
    UI.main_ui.exposure_mode.setCurrentIndex(AutoExposureMode.OFF)
    UI.main_ui.s_per_trial_val.setValue(DEFAULT_TRIAL_TIME_S)
    UI.update_exposure_time(int(camera.exposure))
    UI.update_MAX_FPS(DEFAULT_FPS)
    UI.update_trial_time_s(DEFAULT_TRIAL_TIME_S)


def main():
    # Create QApplication
    app = gui.instantiate_app()
    # Launch Experiment Configuration Dialog
    config_values = gui.get_config(DEFAULT_SAVE_DIR)

    # Create and get directories
    mouse_dir, file_stem = create_session_dirs(config_values)
    image_dir = create_dir_if_not_exist("images", mouse_dir, "images")

    with SpinSystem() as system:
        camera = system.cameras[0]
        camera.init()

        video_acquisition_handler = VideoAcquisition(
            camera, mouse_dir, file_stem
        )

        ui = gui.ControlWindow(camera, video_acquisition_handler)
        initialize(camera, ui)

        event_handler = ImageHandler(image_dir)
        video_acquisition_handler.event_handler = event_handler
        system.video_acquisition_handler = video_acquisition_handler

        # Give the system access to this so it can gracefully shut down if needed
        event_handler.image_event_emitter.image_display_signal.connect(ui.display_image)
        event_handler.image_event_emitter.image_record_signal.connect(
            video_acquisition_handler.add_new_frame
        )
        camera.register_event_handler(event_handler)

        ui.show()
        _ = app.exec()


if __name__ == "__main__":
    main()
