import time
import PySpin
from PySpin import SpinnakerException
from dewan_flir_camera._generics import SpinnakerObject, CameraError
from dewan_flir_camera.options import (
    AutoExposureMode,
    AcquisitionMode,
    AcquisitionState,
)

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

        self.current_FPS = 0

        self.armed = False

        self.acquisition_state: AcquisitionState = AcquisitionState.END

        self.event_handler_ptr = None

        self._get_cam_tl_info()
        self._get_stream_tl_info()

    def init(self):
        if self.is_init:
            self.logger.info("Camera %s is already initialized!", self.number)
        else:
            try:
                self.ptr.Init()
                self.is_init = True
            except SpinnakerException as se:
                raise CameraError(
                    f"Error initializing camera {self.number}!"
                ) from se

    def deinit(self):
        if not self.is_init:
            self.logger.info(
                "Camera %s is not initialized, no need to deinitialize!", self.number
            )
        else:
            try:
                self.unregister_event_handler()
                self.is_init = False
                if self.acquisition_state == AcquisitionState.BEGIN:
                    self.logger.warning(
                        "Force ending camera acquisition to clean up!\n End acquisition before initializing camera!"
                    )
                    self.trigger_acquisition(AcquisitionState.END, force=True)
                self.ptr.DeInit()  # Must DeInit camera ptr as opposed to just deleting the reference
                super().deinit()
            except SpinnakerException as se:
                raise CameraError(
                    f"Error initializing camera {self.number}!"
                ) from se

    def capture_single_frame(self):
        try:
            self.logger.info("Attempting to capture 1 frame!")
            current_acquisition_mode = self.get_acquisition_mode()  # Get Current mode
            if (
                current_acquisition_mode != AcquisitionMode.SINGLE
            ):  # If not single, temporarily set it to single
                self.set_acquisition_mode(AcquisitionMode.SINGLE)
            self.configure_software_trigger()

            if self.trigger_acquisition(AcquisitionState.BEGIN):
                self.TriggerSoftware.Execute()
                time.sleep(0.01)
            if self.trigger_acquisition(AcquisitionState.END):
                self.set_acquisition_mode(
                    current_acquisition_mode
                )  # Reset to initial mode
        except SpinnakerException as se:
            self.logger.error("Unable to capture single frame!: %s", se)

    def trigger_acquisition(
        self, state: AcquisitionState, force: bool = False
    ) -> AcquisitionState:
        try:
            if state == AcquisitionState.BEGIN:
                if self.acquisition_state == AcquisitionState.BEGIN:
                    self.logger.info("Camera acquisition already enabled!")
                else:
                    self.BeginAcquisition()
                    self.acquisition_state = state
            elif state == AcquisitionState.END:
                if self.acquisition_state == AcquisitionState.BEGIN or force:
                    self.EndAcquisition()
                    self.acquisition_state = state
                else:
                    self.logger.info("Camera acquisition already disabled!")
            return self.acquisition_state
        except SpinnakerException as se:
            raise CameraError(
                f"Unable to set camera acquisition state to {state}!"
            ) from se

    def poll(self):
        return {
            "exposure_time": self.get_exposure(),
            "fps": 0,
        }


    def set_exposure(self, new_exposure: int) -> int:
        try:
            if self.ExposureTime.GetAccessMode() != PySpin.RW:
                self.logger.warning("Unable to set exposure time. Aborting...")
                return self.ExposureTime.GetValue()
            if self.get_exposure_mode() == AutoExposureMode.OFF:
                max_exposure_time = self.ExposureTime.GetMax()
                min_exposure_time = self.ExposureTime.GetMin()
                exposure_time = min(max_exposure_time, new_exposure)
                exposure_time = max(exposure_time, min_exposure_time)
                self.ExposureTime.SetValue(exposure_time)
                return exposure_time
            else:
                self.logger.warning(
                    "Automatic exposure must be disabled to manually set the exposure!"
                )
                return self.ExposureTime.GetValue()
        except SpinnakerException as se:
            raise CameraError("Error setting exposure!") from se

    def set_exposure_mode(self, exposure_mode: AutoExposureMode) -> None:
        try:
            # if exposure_mode not in AutoExposureMode:
            #     raise SpinnakerException(f'{exposure_mode} is not a valid exposure mode!')
            if self.ExposureAuto.GetAccessMode() != PySpin.RW:
                self.logger.warning("Unable to set exposure mode. Aborting...")
            else:
                self.ExposureAuto.SetValue(exposure_mode)
        except SpinnakerException as se:
            raise CameraError("Error setting the exposure!") from se

    def set_acquisition_mode(self, mode: AcquisitionMode) -> None:
        try:
            self.logger.debug("Setting acquisition mode to %s", mode)
            self.AcquisitionMode.SetValue(mode)
        except SpinnakerException as se:
            raise CameraError("Error configuring acquisition mode!") from se

    def set_num_burst_frames(self, num_frames: int) -> None:
        try:
            self.logger.debug("Setting number of burst frames to %s", num_frames)
            self.AcquisitionFrameCount.SetValue(num_frames)
        except SpinnakerException as se:
            raise CameraError("Error setting number of burst frames!") from se

    def get_exposure(self) -> float:
        try:
            access_mode = self.ExposureTime.GetAccessMode()
            if access_mode != PySpin.RO and access_mode != PySpin.RW:
                self.logger.warning("Unable to get exposure time. Aborting...")
                return 0.0

            return self.ExposureTime.GetValue()

        except SpinnakerException as se:
            raise CameraError("Error reading camera exposure!") from se

    def get_exposure_mode(self) -> AutoExposureMode or None:
        try:
            exposure_mode = self.ExposureAuto.GetValue()
            self.logger.debug("%s", exposure_mode)
            return AutoExposureMode(exposure_mode)
        except SpinnakerException as se:
            raise CameraError("Error reading exposure_mode mode!") from se

    def get_acquisition_mode(self) -> AcquisitionMode:
        try:
            acquisition_mode = self.AcquisitionMode.GetValue()
            return AcquisitionMode(acquisition_mode)
        except SpinnakerException as se:
            raise CameraError("Error reading acquisition mode!") from se

    def get_num_burst_frames(self) -> float:
        try:
            return self.AcquisitionFrameCount.GetValue()
        except SpinnakerException as se:
            raise CameraError("Error reading acquisition frames!") from se

    def register_event_handler(self, event_handler):
        try:
            self.RegisterEventHandler(event_handler)
            self.event_handler_ptr = event_handler
        except SpinnakerException as se:
            raise CameraError("Error registering event handler!") from se

    def unregister_event_handler(self):
        try:
            if self.event_handler_ptr is not None:
                self.UnregisterEventHandler(self.event_handler_ptr)
                self.event_handler_ptr = None
        except SpinnakerException as se:
            raise CameraError("Error unregistering event handler!") from se

    def configure_hardware_trigger(self):
        try:
            self.logger.info("Configuring triggers...")
            self.TriggerMode.SetValue(PySpin.TriggerMode_Off)
            self.TriggerSelector.SetValue(PySpin.TriggerSelector_AcquisitionStart)
            self.TriggerSource.SetValue(PySpin.TriggerSource_Line2)
            self.TriggerActivation.SetValue(PySpin.TriggerActivation_RisingEdge)
            self.TriggerMode.SetValue(PySpin.TriggerMode_On)

        except SpinnakerException as se:
            raise CameraError(
                f"An error occurred while configuring camera {self.number}"
                "s hardware trigger"
            ) from se

    def configure_software_trigger(self):
        try:
            self.logger.info("Configuring triggers...")
            self.TriggerMode.SetValue(PySpin.TriggerMode_Off)
            self.TriggerSelector.SetValue(PySpin.TriggerSelector_FrameStart)
            self.TriggerSource.SetValue(PySpin.TriggerSource_Software)
            self.TriggerMode.SetValue(PySpin.TriggerMode_On)

        except SpinnakerException as se:
            raise CameraError(
                f"An error occurred while configuring camera {self.number}"
                "s software trigger"
            ) from se

    @property
    def frame_size(self):
        return self.Width.GetValue(), self.Height.GetValue()

    @property
    def exposure(self):
        return self.get_exposure()

    @property
    def num_burst_frames(self):
        return self.get_num_burst_frames()

    def __getattr__(self, attribute):
        """
        Override getattr to search if the underlying pointer object has the value; done to avoid subclassing the ptr
        since the underlying functionality is a bit ambiguous
        """
        try:
            return self.ptr.__getattribute__(
                attribute
            )  ## See if the camera_ptr class has the attribute


        except AttributeError:
            self.logger.error(
                "The camera does not have a property or attribute named %s", attribute
            )
            return None
        except SpinnakerException as se:
            if "AccessException" in str(se):
                self.logger.error(
                    "An AccessException occurred when trying to read %s."
                    " It is likely that your camera does not have this property",
                    attribute,
                )
            return None

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
            raise CameraError(
                "Error getting camera information from transport layer!"
            ) from se

    def _get_stream_tl_info(self):
        """
        Internal method to get properties from stream transport layer
        """
        try:
            self.stream_ID = self.get_node_info(self.ptr.TLStream.StreamID)
            self.stream_type = self.get_node_info(self.ptr.TLStream.StreamType)
        except SpinnakerException as se:
            raise CameraError("Error getting stream information!") from se

    def __str__(self):
        return f"Camera {self.number}"

    def __repr__(self):
        return (
            f"Class: {self.__class__}:\n",
            f"Camera {self.number}:\n",
            f"\t -Vendor: {self.vendor}\n"
            f"\t -Model: {self.model}\n"
            f"\t -Serial: {self.serial}\n"
            f"\t -Speed: {self.speed}\n"
            f"Stream Information:\n"
            f"\t -Stream ID: {self.stream_ID}\n"
            f"\t -Stream Type: {self.stream_type}\n\n",
        )
