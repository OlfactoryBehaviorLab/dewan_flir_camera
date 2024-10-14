from PySpin import SpinnakerException
from _static_funcs import _exit_on_exception, get_node_info

class Cam:
    def __init__(self, cam_ptr, number):
        self.cam_ptr = cam_ptr
        self.number = number
        self.vendor = []
        self.model = []
        self.serial = []

        self.stream_type = []
        self.stream_ID = []

        self._get_cam_tl_info()
        self._get_stream_tl_info()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import traceback
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_val, exc_tb)

        del self.cam_ptr
        self.cam_ptr = []

    def _get_cam_tl_info(self):
        """
        Internal method to get properties from camera transport layer
        """
        try:
            self.serial = get_node_info(self.cam_ptr.TLDevice.DeviceSerialNumber)
            self.vendor = get_node_info(self.cam_ptr.TLDevice.DeviceVendorName)
            self.model = get_node_info(self.cam_ptr.TLDevice.DeviceModelName)

        except SpinnakerException as ex:
            print("Error getting camera information!")
            print(ex)
            _exit_on_exception(self, ex)

    def _get_stream_tl_info(self):
        """
        Internal method to get properties from stream transport layer
        """
        try:
            self.stream_ID = get_node_info(self.cam_ptr.TLStream.StreamID)
            self.stream_type = get_node_info(self.cam_ptr.TLStream.StreamType)
        except SpinnakerException as ex:
            print("Error getting stream information!")
            print(ex)
            _exit_on_exception(self, ex)

    def __str__(self):
        return (f'Camera {self.number}:\n'
                f'\t -Vendor: {self.vendor}\n'
                f'\t -Model: {self.model}\n'
                f'\t -Serial: {self.serial}\n'
                f'Stream Information:\n'
                f'\t -Stream ID: {self.stream_ID}\n'
                f'\t -Stream Type: {self.stream_type}\n\n')

    def __repr__(self):
        return f'Class: {self.__class__}'
