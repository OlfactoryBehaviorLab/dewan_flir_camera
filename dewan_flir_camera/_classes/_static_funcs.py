import PySpin

def get_node_info(node):
    if node is not None and PySpin.IsReadable(node):
        return PySpin.CValuePtr(node).ToString()
    else:
        return None

def _exit_on_exception(self, ex):
    self.__exit__(type(ex), str(ex), ex.__traceback__())