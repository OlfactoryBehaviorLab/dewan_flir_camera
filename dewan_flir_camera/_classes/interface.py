import PySpin
from PySpin import SpinnakerException
from ._generics import SpinnakerObject

class Interface(SpinnakerObject):
    def __init__(self, interface_ptr):
        super().__init__()
        self.interface_ptr = interface_ptr

    def __exit__(self, exc_type, exc_val, exc_tb):
        super().__exit__(exc_type, exc_val, exc_tb)

        del self.interface_ptr
        self.interface_ptr = []


