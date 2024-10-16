import PySpin
from ._generics import SpinnakerObject

class SpinSystem(SpinnakerObject):
    def __init__(self):
        self.system : PySpin.System = []
        self.version = []
        self._interface_list : PySpin.InterfaceList = []
        self.num_interfaces : int = 0
        self._camera_list : PySpin.CameraList = []
        self.num_cams : int = 0

        # Lists to hold the pointers so enumerate and for loops don't complain
        self.cameras = []
        self.interfaces = []

        self._initialize_system()
        super().__init__(self.system)


    def __exit__(self, exc_type, exc_val, tb):
        super().__exit__(exc_type, exc_val, tb)

        self.cameras = []
        self.interfaces = []

        self._camera_list.Clear()
        self._interface_list.Clear()
        self.system.ReleaseInstance()

        self.system = []


    def _initialize_system(self):
        try:
            self.system = PySpin.System.GetInstance()
            self.version = self.system.GetLibraryVersion()
            self._interface_list = self.system.GetInterfaces()
            self.num_interfaces = self._interface_list.GetSize()
            self.interfaces = list(self._interface_list)
            self._camera_list = self.system.GetCameras()
            self.num_cams = self._camera_list.GetSize()
            self.cameras = list(self._camera_list)

            if self.num_cams == 0 or self.num_interfaces == 0:
                print("No cameras present! Exiting!")
                self.__exit__([],[],[])
            else:
                print(f"System Initialized! {self.num_cams} camera(s) found on {self.num_interfaces} interface(s)")
        except PySpin.SpinnakerException as ex:
            print(ex)
            self._exit_on_exception(self, ex)

