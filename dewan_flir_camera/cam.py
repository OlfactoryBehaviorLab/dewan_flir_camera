import PySpin
from PySpin import SpinnakerException
from ._generics import SpinnakerObject
from .options import AutoExposureMode, AcquisitionMode

DEBUG = True


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
            except SpinnakerException as se:
                err_msg = 'Error initializing camera!'
                self.handle_error(se, err_msg, DEBUG)

    def deinit(self):
        if not self.is_init:
            print(f"Camera {self.number} is not initialized, no need to deinitialize!")
        else:
            try:
                self.unregister_event_handler()
                self.ptr.DeInit()
                self.is_init = False
            except SpinnakerException as se:
                err_msg = f'Error deinitializing camera {self.number}!'
                self.handle_error(se, err_msg, DEBUG)

    def poll(self):
        data = {
            'exposure_time': self.get_exposure(),
            'fps': 0,
        }

        return data

    def set_exposure(self, new_exposure) -> None:
        try:
            if self.ExposureTime.GetAccessMode() != PySpin.RW:
                raise SpinnakerException('Unable to set exposure time. Aborting...')

            if self.get_exposure_mode() == AutoExposureMode.OFF:
                max_exposure_time = self.ExposureTime.GetMax()
                exposure_time = min(max_exposure_time, new_exposure)
                self.ExposureTime.SetValue(exposure_time)
        except SpinnakerException as se:
            err_msg = 'Error setting the exposure!'
            self.handle_error(se, err_msg, DEBUG)

    def set_exposure_mode(self, exposure_mode: AutoExposureMode) -> None:
        try:
            # if exposure_mode not in AutoExposureMode:
            #     raise SpinnakerException(f'{exposure_mode} is not a valid exposure mode!')
            if self.ExposureAuto.GetAccessMode() != PySpin.RW:
                raise SpinnakerException('Unable to set exposure mode. Aborting...')
            else:
                self.ExposureAuto.SetValue(exposure_mode)
        except SpinnakerException as se:
            err_msg = 'Error setting the exposure!'
            self.handle_error(se, err_msg, DEBUG)

    def set_acquisition_mode(self, mode) -> None:
        try:
            self.AcquisitionMode.SetValue(mode)
        except SpinnakerException as se:
            err_msg = 'Error configuring acquisition mode!'
            self.handle_error(se, err_msg, DEBUG)

    def get_exposure(self) -> float:
        try:
            access_mode = self.ExposureTime.GetAccessMode()
            if access_mode != PySpin.RO and access_mode != PySpin.RW:
                print('Unable to get exposure time. Aborting...')
                return 0.0

            exposure = self.ExposureTime.GetValue()
            return exposure
        except SpinnakerException as se:
            err_msg = 'Error reading camera exposure!'
            self.handle_error(se, err_msg, DEBUG)
            return 0.0

    def get_exposure_mode(self) -> AutoExposureMode or None:
        try:
            exposure_mode = self.ExposureAuto.GetValue()
            print(exposure_mode)
            return AutoExposureMode(exposure_mode)
        except SpinnakerException as se:
            err_msg = 'Error reading exposure_mode mode!'
            self.handle_error(se, err_msg, DEBUG)
            return None

    def get_acquisition_mode(self):
        try:
            acquisition_mode = self.AcquisitionMode.GetValue()
            print(acquisition_mode)
            return AcquisitionMode(acquisition_mode)
        except SpinnakerException as se:
            err_msg = 'Error reading acquisition mode!'
            self.handle_error(se, err_msg, DEBUG)
            return None

    def register_event_handler(self, event_handler):
        try:
            self.RegisterEventHandler(event_handler)
            self.event_handler_ptr = event_handler
        except SpinnakerException as se:
            err_msg = 'Error registering event handler!'
            self.handle_error(se, err_msg, DEBUG)

    def unregister_event_handler(self):
        try:
            if self.event_handler_ptr is not None:
                self.UnregisterEventHandler(self.event_handler_ptr)
                self.event_handler_ptr = None
        except SpinnakerException as se:
            err_msg = 'Error unregistering event handler!'
            self.handle_error(se, err_msg, DEBUG)

    def configure_trigger(self):
        try:
            self.TriggerMode.SetValue(PySpin.TriggerMode_Off)
            self.TriggerSelector.SetValue(PySpin.TriggerSelector_AcquisitionStart)
            self.TriggerSource.SetValue(PySpin.TriggerSource_Line2)
            self.TriggerMode.SetValue(PySpin.TriggerMode_On)

        except SpinnakerException as se:
            err_msg = f'An error occurred while configuring camera {self.number}''s trigger'
            self.handle_error(se, err_msg, DEBUG)

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

        except SpinnakerException as se:
            err_msg = 'Error getting camera information!'
            self.handle_error(se, err_msg, DEBUG)
            self._exit_on_exception(self, se)

    def _get_stream_tl_info(self):
        """
        Internal method to get properties from stream transport layer
        """
        try:
            self.stream_ID = self.get_node_info(self.ptr.TLStream.StreamID)
            self.stream_type = self.get_node_info(self.ptr.TLStream.StreamType)
        except SpinnakerException as se:
            err_msg = 'Error getting stream information!'
            self.handle_error(se, err_msg, DEBUG)
            self._exit_on_exception(self, se)

    def __str__(self):
        return f'Camera {self.number}'

    def __repr__(self):
        return (f'Class: {self.__class__}:\n',
                f'Camera {self.number}:\n',
                f'\t -Vendor: {self.vendor}\n'
                f'\t -Model: {self.model}\n'
                f'\t -Serial: {self.serial}\n'
                f'\t -Speed: {self.speed}\n'
                f'Stream Information:\n'
                f'\t -Stream ID: {self.stream_ID}\n'
                f'\t -Stream Type: {self.stream_type}\n\n')
