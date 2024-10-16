from _classes.cam import Cam
from _classes.spin_system import SpinSystem

def main():
    with SpinSystem() as system:

        system.cameras[0].init()

        system.cameras[0].configure_trigger()
        print(system.cameras[0].ExposureTime.GetValue())

        system.cameras[0].deinit()


if __name__ == "__main__":
    main()