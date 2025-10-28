import logging
import PySpin

logger = logging.getLogger(__name__)

class SpinnakerObject:
    """ Parent class for all Spinnaker objects
    Holds reference to pointer that all spinnaker objects will have and some simple dunder methods

    """
    def __init__(self, ptr):
        self.ptr = ptr

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.ptr:
            # If we got here and the pointer is still around; release it
            self.deinit()

        if exc_type is not None:
            logger.error("SpinnakerObject error!", exc_info=(exc_type, exc_val, exc_tb))

    def __repr__(self):
        return f"Class: {self.__class__}"

    def deinit(self):
        logger.debug("Deleting %s", self.ptr)
        del self.ptr

    @staticmethod
    def get_node_info(node) -> str | None:
        """ Will check that a Spinnaker node exists and is readable

        Parameters
        ----------
        node
            Spinnaker object node to return value of

        Returns
        -------
        str | None
            Returns node represented as a string or None if it is unreadable or doesn't exist

        """
        if node is not None and PySpin.IsReadable(node):
            return PySpin.CValuePtr(node).ToString()
        else:
            return None


class GenericSpinnakerError(Exception):
    def __init__(self, msg: str):
        super().__init__()
        self.msg = msg
