from enum import IntEnum
import PySpin


class AcquisitionMode(IntEnum):
    CONTINUOUS = PySpin.AcquisitionMode_Continuous  # 0
    SINGLE = PySpin.AcquisitionMode_SingleFrame  # 1
    MULTI = PySpin.AcquisitionMode_MultiFrame  # 2


class AcquisitionState(IntEnum):
    BEGIN = 1
    END = 0


class AutoExposureMode(IntEnum):
    OFF = PySpin.ExposureAuto_Off  # 0
    ONCE = PySpin.ExposureAuto_Once  # 1
    CONTINUOUS = PySpin.ExposureAuto_Continuous  # 2


class VideoType:
    """'Enum' to select video type to be created and saved"""
    UNCOMPRESSED = 0
    MJPG = 1
    H264_AVI = 2
    H264_MP4 = 3