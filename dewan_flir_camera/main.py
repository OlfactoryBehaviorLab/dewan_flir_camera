from _classes.cam import Cam
from _classes.interface import Interface
from _classes.spin_system import SpinSystem

def main():
    with SpinSystem() as system:
        for i, cam in enumerate(system.camera_list):
            with Cam(cam, i) as camera:
                print(camera)

        del cam



if __name__ == "__main__":
    main()