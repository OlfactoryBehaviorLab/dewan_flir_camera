import PySpin
from PySpin import SpinnakerException
from _static_funcs import _exit_on_exception, get_node_info


class Interface:
    def __init__(self, interface_ptr):
        self.interface_ptr = interface_ptr

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import traceback
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_val, exc_tb)

        del self.interface_ptr
        self.interface_ptr = []


