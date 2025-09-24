## Setup
### openh264
On Windows, openh264-1.8.0 must be downloaded and installed manually prior to using video recording features. Download the
dll from [here](http://ciscobinary.openh264.org/openh264-1.8.0-win64.dll.bz2). Do one of the following:
1)  (Preferred) Set the environment variable `OPENH264_LIBRARY` to the absolute path for the DLL. We provide a copy in this repository in the following directory: `[PATH_TO_REPOSITORY]\lib\openh264-1.8.0-win64.dll`
2) Copy the dll to `C:\Windows\System32`
3) Copy the dll to the root of the dewan_flir_camera repository
