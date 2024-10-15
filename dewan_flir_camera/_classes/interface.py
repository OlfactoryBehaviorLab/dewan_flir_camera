import PySpin
from PySpin import SpinnakerException
from ._generics import SpinnakerObject

class Interface(SpinnakerObject):
    def __init__(self, interface_ptr, number):
        super().__init__()
        self.interface_ptr = interface_ptr
        self.number = number
        self.interface_name = []
        self.interface_id = []
        self.interface_type = []

        self.host_adapter_name = []
        self.host_adapter_vendor = []
        self.host_adapter_driver_version = []

        self._get_interface_tl_info()
        self._get_HBA_tl_info()

    def __exit__(self, exc_type, exc_val, exc_tb):
        super().__exit__(exc_type, exc_val, exc_tb)

        del self.interface_ptr
        self.interface_ptr = []

    def _get_interface_tl_info(self):
        """
        Internal method to get interface properties from the transport layer
        """
        try:
            self.interface_name = self.get_node_info(self.interface_ptr.TLInterface.InterfaceDisplayName)
            self.interface_id = self.get_node_info(self.interface_ptr.TLInterface.InterfaceID)
            self.interface_type = self.get_node_info(self.interface_ptr.TLInterface.InterfaceType)

        except SpinnakerException as ex:
            print("Error getting camera information!")
            print(ex)
            self._exit_on_exception(self, ex)

    def _get_HBA_tl_info(self):
        """
        Internal method to get host bus adapter (HBA) properties from the transport layer
        """
        try:
            self.host_adapter_name = self.get_node_info(self.interface_ptr.TLInterface.HostAdapterName)
            self.host_adapter_vendor = self.get_node_info(self.interface_ptr.TLInterface.HostAdapterVendor)
            self.host_adapter_driver_version = self.get_node_info(self.interface_ptr.TLInterface.HostAdapterDriverVersion)

        except SpinnakerException as ex:
            print("Error getting camera information!")
            print(ex)
            self._exit_on_exception(self, ex)

    def __str__(self):
        return (f'Interface {self.number}:\n'
                f'\t -Name: {self.interface_name}\n'
                f'\t -ID: {self.interface_id}\n'
                f'\t -Type: {self.interface_type}\n'
                f'Host Bus Adapter (HBA) Information:\n'
                f'\t -HBA Name: {self.host_adapter_name}\n'
                f'\t -HBA Vendor: {self.host_adapter_vendor}\n'
                f'\t -HBA Driver Version: {self.host_adapter_driver_version}\n\n')