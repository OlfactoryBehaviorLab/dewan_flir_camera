import PySpin

class SpinSystem:
    def __init__(self):
        self.system : PySpin.System = []
        self.version = []
        self.interface_list : PySpin.InterfaceList = []
        self.num_interfaces : int = 0
        self.camera_list : PySpin.CameraList = []
        self.num_cams : int = 0

        self._initialize_system()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, tb):
        import traceback
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_val, tb)

        self.camera_list.Clear()
        self.interface_list.Clear()
        self.system.ReleaseInstance()

        self.cameras = []
        self.interfaces = []
        self.system = []


    def _initialize_system(self):
        try:
            self.system = PySpin.System.GetInstance()
            self.version = self.system.GetLibraryVersion()
            self.interface_list = self.system.GetInterfaces()
            self.num_interfaces = self.interface_list.GetSize()
            self.camera_list = self.system.GetCameras()
            self.num_cams = self.camera_list.GetSize()

            if self.num_cams == 0 or self.num_interfaces == 0:
                print("No cameras present! Exiting!")
                self.__exit__([],[],[])
            else:
                print(f"System Initialized! {self.num_cams} camera(s) found on {self.num_interfaces} interface(s)")
        except PySpin.SpinnakerException as e:
            print(e)
            self.__exit__(type(e), str(e), e.__traceback__)