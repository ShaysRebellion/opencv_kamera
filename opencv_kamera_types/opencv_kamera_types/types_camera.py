from enum import Enum

# see enum cv::VideoCaptureProperties: https://docs.opencv.org/4.7.0/d4/d15/group__videoio__flags__base.html
OpenCvVideoCaptureProp = int

CameraSettings = dict[OpenCvVideoCaptureProp, float]
SupportedSettings = dict[OpenCvVideoCaptureProp, bool]

class ImageColor(Enum):
    COLOR = 'color'
    GRAY = 'gray'

class ImageFormat(Enum):
    RAW = '.raw'
    JPG = '.jpg'
    PNG = '.png'
