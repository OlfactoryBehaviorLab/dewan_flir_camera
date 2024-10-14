import PySpin

class Cam:
    def __init__(self, cam_ptr, number):
        self.cam_ptr = cam_ptr
        self.number = number
        self.vendor = []
        self.model = []

        self._get_cam_info()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import traceback
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_val, exc_tb)
        del self.cam_ptr
        self.cam_ptr = []



    def _get_cam_info(self):
        if self.cam_ptr.TLDevice.DeviceVendorName.GetAccessMode() == PySpin.RO:
            self.vendor = self.cam_ptr.TLDevice.DeviceVendorName.ToString()

        if self.cam_ptr.TLDevice.DeviceModelName.GetAccessMode() == PySpin.RO:
            self.model = self.cam_ptr.TLDevice.DeviceModelName.GetValue()

    def __str__(self):
        return f'Camera {self.number}, Vendor: {self.vendor}, Module: {self.model}'    @staticmethod
    def get_node_info(node):
        if node is not None and PySpin.IsReadable(node):
            return PySpin.CValuePtr(node).ToString()
        else:
            return None