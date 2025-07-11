import PySpin
from PySpin import SpinnakerException
from ._generics import SpinnakerObject


class Cam(SpinnakerObject):
    def __init__(self, cam_ptr, number):
        super().__init__(cam_ptr)
        self.number = number
        self.is_init = False
        self.vendor = []
        self.model = []
        self.serial = []
        self.speed = []

        self.stream_type = []
        self.stream_ID = []

        self.event_handler_ptr = None

        self._get_cam_tl_info()
        self._get_stream_tl_info()

    def init(self):
        if self.is_init:
            print(f"Camera {self.number} is already initialized!")
        else:
            try:
                self.ptr.Init()
                self.is_init = True
            except SpinnakerException as ex:
                print(f"Error initializing camera {self.number}!")
                print(ex)

    def deinit(self):
        if not self.is_init:
            print(f"Camera {self.number} is not initialized, no need to deinitialize!")
        else:
            try:
                self.unregister_event_handler()
                self.ptr.DeInit()
                self.is_init = False
            except SpinnakerException as ex:
                print(f"Error deinitializing camera {self.number}!")
                print(ex)

    def configure_acquisition_mode(self, mode):
        try:
            self.AcquisitionMode.SetValue(mode)
        except SpinnakerException as se:
            print("Error configuring acquisition mode!")
            print(se)

    def register_event_handler(self, event_handler):
        try:
            self.RegisterEventHandler(event_handler)
            self.event_handler_ptr = event_handler
        except SpinnakerException as se:
            print("Error registering event handler!")
            print(se)

    def unregister_event_handler(self):
        try:
            if self.event_handler_ptr is not None:
                self.UnregisterEventHandler(self.event_handler_ptr)
                self.event_handler_ptr = None
        except SpinnakerException as se:
            print("Error unregistering event handler!")
            print(se)

    def configure_trigger(self):
        try:
            self.TriggerMode.SetValue(PySpin.TriggerMode_Off)
            self.TriggerSelector.SetValue(PySpin.TriggerSelector_AcquisitionStart)
            self.TriggerSource.SetValue(PySpin.TriggerSource_Line2)
            self.TriggerMode.SetValue(PySpin.TriggerMode_On)

        except SpinnakerException as se:
            print(f"An error occurred while configuring camera {self.number}s trigger")
            print(se)

    @property
    def frame_size(self):
        return self.Width, self.Height

    def __getattr__(self, attribute):
        """
        Override getattr to search if the underlying pointer object has the value; done to avoid subclassing the ptr
        since the underlying functionality is a bit ambiguous
        """
        try:
            return_ptr = self.ptr.__getattribute__(
                attribute
            )  ## See if the camera_ptr class has the attribute
            return return_ptr

        except AttributeError as ae:
            print(f"The camera does not have a property or attribute named {attribute}")
            print(f"Original Exception: {ae}")
        except SpinnakerException as se:
            if "AccessException" in str(se):
                print(
                    f"An AccessException occurred when trying to read {attribute}."
                    f" It is likely that your camera does not have this property"
                )
                print(f"Original Exception: {se}")
            else:
                raise SpinnakerException(
                    f"Camera must be initialized to read {attribute}"
                )

    def __exit__(self, exc_type, exc_val, exc_tb):
        super().__exit__(exc_type, exc_val, exc_tb)
        self.ptr.DeInit()
        del self.ptr
        # self.ptr = []

    def _get_cam_tl_info(self):
        """
        Internal method to get properties from camera transport layer
        """
        try:
            self.serial = self.get_node_info(self.ptr.TLDevice.DeviceSerialNumber)
            self.vendor = self.get_node_info(self.ptr.TLDevice.DeviceVendorName)
            self.model = self.get_node_info(self.ptr.TLDevice.DeviceModelName)
            self.speed = self.get_node_info(self.ptr.TLDevice.DeviceCurrentSpeed)

        except SpinnakerException as ex:
            print("Error getting camera information!")
            print(ex)
            self._exit_on_exception(self, ex)

    def _get_stream_tl_info(self):
        """
        Internal method to get properties from stream transport layer
        """
        try:
            self.stream_ID = self.get_node_info(self.ptr.TLStream.StreamID)
            self.stream_type = self.get_node_info(self.ptr.TLStream.StreamType)
        except SpinnakerException as ex:
            print("Error getting stream information!")
            print(ex)
            self._exit_on_exception(self, ex)

    def __str__(self):
        return (
            f"Camera {self.number}:\n"
            f"\t -Vendor: {self.vendor}\n"
            f"\t -Model: {self.model}\n"
            f"\t -Serial: {self.serial}\n"
            f"\t -Speed: {self.speed}\n"
            f"Stream Information:\n"
            f"\t -Stream ID: {self.stream_ID}\n"
            f"\t -Stream Type: {self.stream_type}\n\n"
        )

    def __repr__(self):
        return f"Class: {self.__class__}"
