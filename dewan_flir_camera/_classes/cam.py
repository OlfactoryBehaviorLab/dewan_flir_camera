import PySpin
from PySpin import SpinnakerException


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
            self.serial = Cam.get_node_info(self.cam_ptr.TLDevice.DeviceSerialNumber)
            self.vendor = Cam.get_node_info(self.cam_ptr.TLDevice.DeviceVendorName)
            self.model = Cam.get_node_info(self.cam_ptr.TLDevice.DeviceModelName)

        except SpinnakerException as ex:
            print("Error getting camera information!")
            print(ex)
            self._exit_on_exception(ex)

    def _get_stream_tl_info(self):
        try:
            self.stream_ID = Cam.get_node_info(self.cam_ptr.TLStream.StreamID)
            self.stream_type = Cam.get_node_info(self.cam_ptr.TLStream.StreamType)
        except SpinnakerException as ex:
            print("Error getting stream information!")
            print(ex)
            self._exit_on_exception(ex)

    def __str__(self):
        return f'Camera {self.number}, Vendor: {self.vendor}, Module: {self.model}, Serial: {self.serial}'

    @staticmethod
    def get_node_info(node):
        if node is not None and PySpin.IsReadable(node):
            return PySpin.CValuePtr(node).ToString()
        else:
            return None

    def _exit_on_exception(self, ex):
        self.__exit__(type(ex), str(ex), ex.__traceback__())