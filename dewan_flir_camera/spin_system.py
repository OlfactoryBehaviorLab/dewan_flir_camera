import PySpin
from ._generics import SpinnakerObject
from .cam import Cam


class SpinSystem(SpinnakerObject):
    def __init__(self):
        self.system: PySpin.System = []
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
        super().__init__(self.system)

    def __exit__(self, exc_type, exc_val, tb):
        super().__exit__(exc_type, exc_val, tb)

        ## Clean up our classes if we leave the scope of this system
        for camera in self.cameras:
            camera.__exit__(None, None, None)
        for interface in self.interfaces:
            interface.__exit__(None, None, None)

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
        super().__exit__(exc_type, exc_val, tb)

    def _initialize_system(self):
        try:
            print('Initializing System!')
            self.system = PySpin.System.GetInstance()
            self.version = self.system.GetLibraryVersion()
            self._interface_list = self.system.GetInterfaces()
            self.num_interfaces = self._interface_list.GetSize()
            self.interface_list = list(self._interface_list)
            self._camera_list = self.system.GetCameras()
            self.num_cams = self._camera_list.GetSize()
            self.camera_list = list(self._camera_list)

            if self.num_cams == 0 or self.num_interfaces == 0:
                print("No cameras present! Exiting!")
                self.__exit__(None,None,None)
            else:
                self._instantiate_camera_wrappers()
                print(
                    f"System Initialized! {self.num_cams} camera(s) found on {self.num_interfaces} interface(s)"
                )
        except PySpin.SpinnakerException as ex:
            self._exit_on_exception(self, ex)

    def _instantiate_camera_wrappers(self):
        print("Instantiating Camera Wrappers...")
        for i, cam in enumerate(self.camera_list):
            new_cam = Cam(cam, i)
            self.cameras.append(new_cam)
        del cam

    def get_cameras(self):
        try:
            self._camera_list = self.system.GetCameras()
            self.num_cams = self._camera_list.GetSize()
            self.camera_list = list(self._camera_list)

            self._instantiate_camera_wrappers()
        except PySpin.SpinnakerException as ex:
            self._exit_on_exception(self, ex)

    def get_interfaces(self):
        try:
            self._interface_list = self.system.GetInterfaces()
            self.num_interfaces = self._interface_list.GetSize()
            self.interface_list = list(self._interface_list)
        except PySpin.SpinnakerException as ex:
            self._exit_on_exception(self, ex)
