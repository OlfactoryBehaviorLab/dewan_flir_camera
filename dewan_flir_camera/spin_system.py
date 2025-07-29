import logging
import PySpin
from dewan_flir_camera._generics import SpinnakerObject, CameraError
from dewan_flir_camera.cam import Cam
from dewan_flir_camera.interface import Interface


class SpinSystem(SpinnakerObject):
    def __init__(self, logger: logging.Logger):
        self.system: PySpin.System = []
        self.logger: logging.Logger = logger
        self.version = []
        self._interface_list: PySpin.InterfaceList = []
        self.num_interfaces: int = 0
        self._camera_list: PySpin.CameraList = []
        self.num_cams: int = 0

        # Lists to hold the pointers so enumerate and for loops don't complain
        self.camera_list = []
        self.interface_list = []

        # List to hold our wrapper classes so they will be cleaned up properly
        self.cameras: list[Cam] = []
        self.interfaces = []

        self._initialize_system()
        super().__init__(self.system, self.logger)

    def __enter__(self):
        if self.system:
            return self
        else:
            raise CameraError("Unable to initialize SpinSystem!")

    def __exit__(self, exc_type, exc_val, tb):
        self.logger.debug("Hit context manager exit")
        self._cleanup()
        super().__exit__(exc_type, exc_val, tb)

    def __str__(self):
        return f"Spinnaker System"

    def _initialize_system(self):
        try:
            self.logger.info("Initializing Spinnaker System")
            self.system = PySpin.System.GetInstance()
            self.version = self.system.GetLibraryVersion()
            self._interface_list = self.system.GetInterfaces()
            self.num_interfaces = self._interface_list.GetSize()
            self._camera_list = self.system.GetCameras()
            self.num_cams = self._camera_list.GetSize()
            self.camera_list = list(self._camera_list)

            if self.num_cams == 0 or self.num_interfaces == 0:
                # No cameras or interfaces to initialize
                self._cleanup()
            else:
                self._instantiate_interface_wrappers()
                self._instantiate_camera_wrappers()
                self.logger.info(
                    "System Initialized! %s camera(s) found on %s interface(s)",
                    self.num_cams,
                    self.num_interfaces,
                )
        except PySpin.SpinnakerException as ex:
            # Unexpected error, cleanup and raise our general exception
            self._cleanup()
            raise CameraError("Error initializing system!") from ex

    def _cleanup(self):
        ## Clean up our classes if we leave the scope of this system
        for camera in self.cameras:
            camera.deinit()
        for interface in self.interfaces:
            interface.deinit()

        ## Clear lists that reference the pointers
        self.camera_list = []
        self.interface_list = []

        if self._camera_list:
            self._camera_list.Clear()
        if self._interface_list:
            self._interface_list.Clear()
        if self.system:
            self.system.ReleaseInstance()

        self.system = []

    def _instantiate_camera_wrappers(self):
        self.logger.info("Instantiating Camera Wrappers")
        for i, cam in enumerate(self.camera_list):
            new_cam = Cam(cam, self.logger, i)
            self.cameras.append(new_cam)
        del cam

    def _instantiate_interface_wrappers(self):
        self.logger.info("Instantiating Interface Wrappers")
        for i, interface in enumerate(self._interface_list):
            new_cam = Interface(interface, self.logger, i)
            self.interfaces.append(new_cam)
        del interface
