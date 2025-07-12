from enum import IntEnum, Enum
import PySpin


class AcquisitionMode(IntEnum):
    CONTINUOUS = PySpin.AcquisitionMode_Continuous # 0
    SINGLE = PySpin.AcquisitionMode_SingleFrame # 1
    MULTI = PySpin.AcquisitionMode_MultiFrame # 2

class AcquisitionState(IntEnum):
    BEGIN = 1
    END = 0

class AutoExposureMode(IntEnum):
    OFF = PySpin.ExposureAuto_Off # 0
    ONCE = PySpin.ExposureAuto_Once # 1
    CONTINUOUS = PySpin.ExposureAuto_Continuous # 2


