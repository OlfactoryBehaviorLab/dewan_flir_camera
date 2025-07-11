import PySpin
from PySpin import SpinnakerException
from time import sleep

from _classes.spin_system import SpinSystem
from _classes.acquisition import ImageHandler


def main():
    with SpinSystem() as system:
        camera = system.cameras[0]
        event_handler = ImageHandler("./images")

        camera.init()

        camera.configure_trigger()
        camera.ExposureAuto.SetValue(PySpin.ExposureAuto_Continuous)
        camera.configure_acquisition_mode(PySpin.AcquisitionMode_Continuous)
        camera.register_event_handler(event_handler)

        while True:
            try:
                print("Waiting for trigger!")
                camera.BeginAcquisition()
                event_handler.reset()
                wait_for_trigger(event_handler)
                camera.EndAcquisition()
            except KeyboardInterrupt:
                camera.EndAcquisition()
                break

        camera.deinit()
        del camera


def wait_for_trigger(event_handler, num_frames=100, wait_time_s=0.1):
    try:
        while True:
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
