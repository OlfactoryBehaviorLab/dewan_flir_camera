import traceback
import PySpin


class SpinnakerObject:
    def __init__(self, ptr):
        self.ptr = ptr

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import traceback

        if exc_type is not None:
            traceback.print_exception(exc_type, exc_val, exc_tb)
        print(f'Shutting down {self}!')

    def __repr__(self):
        return f"Class: {self.__class__}"


    @staticmethod
    def handle_error(exception: type[BaseException], error_msg=None, DEBUG=False):
        if DEBUG:
            print(traceback.format_exception(exception))
        else:
            if error_msg:
                print(error_msg)
            else:
                print(exception)


    @staticmethod
    def get_node_info(node):
        if node is not None and PySpin.IsReadable(node):
            return PySpin.CValuePtr(node).ToString()
        else:
            return None

    @staticmethod
    def _exit_on_exception(self, ex):
        self.__exit__(type(ex), str(ex), ex.__traceback__())

class CameraException(Exception):
    def __init__(self, msg: str):
        super().__init__()
        self.msg = msg
        print(f"There was a problem loading the cameras: {msg}")