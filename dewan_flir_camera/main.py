import PySpin
from PySpin import SpinnakerException
from time import sleep

from . import gui
from ._classes.spin_system import SpinSystem
from ._classes.acquisition import ImageHandler


def main():
    gui.launch_gui(None)
    with SpinSystem() as system:
        system.get_interfaces()
        system.get_cameras()

        if system.num_cams == 0 or system.num_interfaces == 0:
            print('No suitable cameras or interfaces found! Exiting!')
            return

        camera = system.cameras[0]
        event_handler = ImageHandler('./images')
        camera.init()

        camera.configure_trigger()
        camera.ExposureAuto.SetValue(PySpin.ExposureAuto_Continuous)
        camera.configure_acquisition_mode(PySpin.AcquisitionMode_Continuous)
        # camera.register_event_handler(event_handler)
        window = gui.launch_gui(camera)

        camera.deinit()
        del camera



def wait_for_trigger(event_handler, num_frames=100, wait_time_s=0.1):
    try:
        while True:
            sleep(wait_time_s)
            if event_handler.num_acquired_images >= num_frames:
                return
    except SpinnakerException as se:
        print('Error while acquiring images!')
        print(se)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()