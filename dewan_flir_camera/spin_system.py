import logging
import PySpin
from dewan_flir_camera._generics import SpinnakerObject, GenericSpinnakerError
from dewan_flir_camera.cam import Cam
from dewan_flir_camera.interface import Interface

logger = logging.getLogger(__name__)

class SpinSystem(SpinnakerObject):
    """SpinSystem container for all enumerated cameras and interfaces

    Implements a context manager to properly deinitialize and delete system pointers once the context is exited

    """
    def __init__(self):
        self.system: PySpin.System = []
        self.version = []
        self._interface_list: PySpin.InterfaceList = []
        self.num_interfaces: int = 0
        self._camera_list: PySpin.CameraList = []
        self.num_cams: int = 0
        self.video_acquisition_handler = None
        # Lists to hold the pointers so enumerate and for loops don't complain
        self.camera_list = []
        self.interface_list = []

        # List to hold our wrapper classes so they will be cleaned up properly
        self.cameras: list[Cam] = []
        self.interfaces = []

        self._initialize_system()
        super().__init__(self.system)

    def _initialize_system(self):
        """Internal SpinSystem initialization method

        Populates system information, enumerates interface and camera pointers and instantiates wrappers for each
        found interface and camera

        Returns
        -------
        None

        """
        try:
            logger.info("Initializing Spinnaker System")
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
                logger.info(
                    "System Initialized! %s camera(s) found on %s interface(s)",
                    self.num_cams,
                    self.num_interfaces,
                )
        except PySpin.SpinnakerException as ex:
            # Unexpected error, cleanup and raise our general exception
            self._cleanup()
            raise GenericSpinnakerError("Error initializing system!") from ex

    def _cleanup(self):
        """Internal SpinSystem cleanup function

        Deletes each interface and camera instance and releases the pointer

        """
        ## Clean up our classes if we leave the scope of this system
        for camera in self.cameras:
            camera.deinit()
        for interface in self.interfaces:
            interface.deinit()

        if self.video_acquisition_handler:
            self.video_acquisition_handler.shutdown()

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
        """Loops through pointers and instantiates wrappers for each


        Returns
        -------
        None
        """
        logger.info("Instantiating Camera Wrappers")
        for i, cam in enumerate(self.camera_list):
            new_cam = Cam(cam, i)
            self.cameras.append(new_cam)
        del cam

    def _instantiate_interface_wrappers(self):
        logger.info("Instantiating Interface Wrappers")
        for i, interface in enumerate(self._interface_list):
            new_interface = Interface(interface, i)
            self.interfaces.append(new_interface)
        del interface


    def __enter__(self):
        if self.system:
            return self
        else:
            raise GenericSpinnakerError("Unable to initialize SpinSystem!")

    def __exit__(self, exc_type, exc_val, tb):
        logger.debug("Hit context manager exit")
        self._cleanup()
        super().__exit__(exc_type, exc_val, tb)

    def __str__(self):
        return f"Spinnaker System: {self.system}"