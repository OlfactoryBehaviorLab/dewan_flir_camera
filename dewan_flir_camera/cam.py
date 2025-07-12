import traceback
import time
import PySpin
from PySpin import SpinnakerException
from dewan_flir_camera._generics import SpinnakerObject, CameraException
from dewan_flir_camera.options import AutoExposureMode, AcquisitionMode, AcquisitionState

DEBUG = True



class Cam(SpinnakerObject):
    def __init__(self, cam_ptr, logger, number):
        super().__init__(cam_ptr, logger)
        self.number = number
        self.is_init = False
        self.vendor = []
        self.model = []
        self.serial = []
        self.speed = []

        self.stream_type = []
        self.stream_ID = []

        self.acquisition_enabled: bool = False

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
            self.logger.info("Camera %s is not initialized, no need to deinitialize!", self.number)
        else:
            try:
                self.unregister_event_handler()
                self.is_init = False
                self.ptr.DeInit() # Must DeInit camera ptr
                super().deinit()
            except SpinnakerException as se:
                err_msg = f'Error deinitializing camera {self.number}!'
                self.handle_error(se, err_msg, DEBUG)

    def capture_single_frame(self):
        try:
            print("Get Single Frame")
            current_acquisition_mode = self.get_acquisition_mode()  # Get Current mode
            if current_acquisition_mode != AcquisitionMode.SINGLE:  # If not single, temporarily set it to single
                self.set_acquisition_mode(AcquisitionMode.SINGLE)
            self.configure_software_trigger()

            if self.trigger_acquisition(AcquisitionState.BEGIN):
                self.TriggerSoftware.Execute()
                time.sleep(2)
            if self.trigger_acquisition(AcquisitionState.END):
                self.set_acquisition_mode(current_acquisition_mode)  # Reset to initial mode
        except SpinnakerException as se:
            raise CameraException("Unable to capture single frame!") from se

    def trigger_acquisition(self, state: AcquisitionState) -> bool:
        try:
            if state == AcquisitionState.BEGIN:
                if self.acquisition_enabled:
                    self.logger.info("Camera acquisition already enabled!")
                else:
                    self.BeginAcquisition()
                    self.acquisition_enabled = True
            elif state == AcquisitionState.END:
                if self.acquisition_enabled:
                    self.EndAcquisition()
                    self.acquisition_enabled = False
                else:
                    self.logger.info("Camera acquisition already disabled!")
            return self.acquisition_enabled
        except SpinnakerException as se:
            raise CameraException(f"Unable to set camera acquisition state to {state}!") from se


    def poll(self):
        data = {
            'exposure_time': self.get_exposure(),
            'fps': 0,
        }

        return data

    def set_exposure(self, new_exposure: AutoExposureMode) -> int:
        try:
            if self.ExposureTime.GetAccessMode() != PySpin.RW:
                raise SpinnakerException('Unable to set exposure time. Aborting...')

            if self.get_exposure_mode() == AutoExposureMode.OFF:
                max_exposure_time = self.ExposureTime.GetMax()
                min_exposure_time = self.ExposureTime.GetMin()
                exposure_time = min(max_exposure_time, new_exposure)
                exposure_time = max(exposure_time, min_exposure_time)
                self.ExposureTime.SetValue(exposure_time)
                return exposure_time
            else:
                print('Exposure mode must be set to automatic to manually set the exposure!')
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

    def set_acquisition_mode(self, mode: AcquisitionMode) -> None:
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

    def get_acquisition_mode(self) -> AcquisitionMode:
        try:
            acquisition_mode = self.AcquisitionMode.GetValue()
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

    def configure_hardware_trigger(self):
        try:
            print('Configuring triggers...')
            self.TriggerMode.SetValue(PySpin.TriggerMode_Off)
            self.TriggerSelector.SetValue(PySpin.TriggerSelector_FrameStart)
            self.TriggerSource.SetValue(PySpin.TriggerSource_Line2)
            self.TriggerActivation.SetValue(PySpin.TriggerActivation_LevelHigh)
            self.TriggerMode.SetValue(PySpin.TriggerMode_On)

        except SpinnakerException as se:
            err_msg = f'An error occurred while configuring camera {self.number}''s trigger'
            self.handle_error(se, err_msg, DEBUG)

    def configure_software_trigger(self):
        try:
            print('Configuring triggers...')
            self.TriggerMode.SetValue(PySpin.TriggerMode_Off)
            self.TriggerSelector.SetValue(PySpin.TriggerSelector_FrameStart)
            self.TriggerSource.SetValue(PySpin.TriggerSource_Software)
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
        # Overload to ensure that the cameras local deinit function gets called if camera is used in a context manager
        self.deinit()
        super().__exit__(exc_type, exc_val, exc_tb)

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
