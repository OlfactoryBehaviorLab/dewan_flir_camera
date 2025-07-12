from PySpin import SpinnakerException
from time import sleep

from dewan_flir_camera import gui
from spin_system import SpinSystem
from acquisition import ImageHandler
from options import AutoExposureMode, AcquisitionMode, AcquisitionState

import logging
logging.basicConfig(level=logging.DEBUG)

def main():
    logger = logging.getLogger(__name__)

    with SpinSystem(logger) as system:
        camera = system.cameras[0]
        event_handler = ImageHandler('./images')
        camera.init()
        camera.configure_hardware_trigger()
        camera.ExposureAuto.SetValue(AutoExposureMode.CONTINUOUS)
        camera.set_acquisition_mode(AcquisitionMode.CONTINUOUS)
        camera.register_event_handler(event_handler)
        ui = gui.launch_gui(camera, logger)

        while True:
            try:
                logger.info("Waiting for trigger!")
                camera.trigger_acquisition(AcquisitionState.BEGIN)
                event_handler.reset()
                wait_for_trigger(event_handler, logger)
                camera.trigger_acquisition(AcquisitionState.END)
            except KeyboardInterrupt:
                camera.trigger_acquisition(AcquisitionState.END)
                event_handler.reset()
                break


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
