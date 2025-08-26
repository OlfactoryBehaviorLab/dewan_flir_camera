import logging
from pathlib import Path

from dewan_flir_camera import gui
from dewan_flir_camera.spin_system import SpinSystem
from dewan_flir_camera.acquisition import ImageHandler, VideoAcquisition
from dewan_flir_camera.options import AutoExposureMode, AcquisitionMode

logging.basicConfig(level=logging.DEBUG)

DEFAULT_FPS = 60
DEFAULT_TRIAL_TIME_S = 10
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
        logger.error(
            "Error creating directory %s. Reverting to default directory!", path
        )

    return path


def create_session_dirs(config_values, logger) -> tuple[Path, str]:
    # Create save dir if needed
    save_dir = create_dir_if_not_exist(
        config_values["save_dir"], None, DEFAULT_SAVE_DIR, logger
    )
    experiment_dir = create_dir_if_not_exist(
        save_dir, config_values["experiment"], DEFAULT_EXPERIMENT_DIR, logger
    )
    experiment_stem = experiment_dir.stem
    mouse_dir = create_dir_if_not_exist(
        experiment_dir, config_values["mouse"], DEFAULT_MOUSE_DIR, logger
    )
    mouse_stem = mouse_dir.stem

    file_stem = f"{mouse_stem}-{experiment_stem}"
    logger.info("Save Dir: %s", mouse_dir)
    return mouse_dir, file_stem


def initialize(camera, UI: gui.ControlWindow):
    # === DEFAULT CAMERA CONFIGURATION === #
    camera.configure_hardware_trigger() # Configure hardware trigger
    camera.ExposureAuto.SetValue(AutoExposureMode.OFF)  # Manual Exposure Mode
    camera.set_exposure(
        gui.ControlWindow.FPS_to_exposure(DEFAULT_FPS)
    )  # Set exposure to default FPS
    camera.set_acquisition_mode(
        AcquisitionMode.MULTI
    )  # Multiframe/Burst Acquisition
    num_burst_frames = DEFAULT_FPS * DEFAULT_TRIAL_TIME_S
    camera.set_num_burst_frames(num_burst_frames)

    # === DEFAULT GUI CONFIGURATION === #
    # The other camera fields are automatically updated by the timer
    # This is the only one we need to pull from the camera
    UI.main_ui.exposure_value.setValue(
        int(camera.get_exposure())
    )
    UI.main_ui.acquisition_mode_data.setCurrentIndex(
        AcquisitionMode.MULTI
    )
    UI.main_ui.exposure_mode.setCurrentIndex(
        AutoExposureMode.OFF
    )
    UI.main_ui.s_per_trial_val.setValue(DEFAULT_TRIAL_TIME_S)
    UI.update_exposure_time(int(camera.get_exposure()))
    UI.update_MAX_FPS(DEFAULT_FPS)
    UI.update_trial_time_s(DEFAULT_TRIAL_TIME_S)


def main():
    logger = logging.getLogger(__name__)

    app = gui.instantiate_app(logger)
    config_values = gui.get_config(logger)
    mouse_dir, file_stem = create_session_dirs(config_values, logger)
    image_dir = create_dir_if_not_exist(mouse_dir, "images", None, logger)
    with SpinSystem(logger) as system:
        camera = system.cameras[0]
        camera.init()

        video_acquisition_handler = VideoAcquisition(
            camera, logger, mouse_dir, file_stem
        )

        ui = gui.ControlWindow(camera, logger, video_acquisition_handler)
        initialize(camera, ui)

        event_handler = ImageHandler(image_dir, logger)
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
