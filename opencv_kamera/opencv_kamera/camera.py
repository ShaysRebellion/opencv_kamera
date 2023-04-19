from typing import Optional
import threading
import cv2 as cv
from opencv_kamera_types import OpenCvVideoCaptureProp, CameraSettings, SupportedSettings, ImageColor, ImageFormat

class OpenCvCamera:
    def __init__(self):
        self._camera = None # lazy initialization
        self._shouldCaptureVideo = False;
        self._videoImageColor = ImageColor.GRAY
        self._videoImageFormat = ImageFormat.JPG
        self._captureVideoThread = threading.Thread(target=self._video_capture_thread)
        self._image = None

    def __del__(self):
        self.close_camera_connection()

    def has_camera_connection(self) -> bool:
        return bool(self._camera and self._camera.isOpened())

    def open_camera_connection(self) -> bool:
        if not self._camera: self._camera = cv.VideoCapture(0)
        return self._camera.open(0)

    def close_camera_connection(self) -> None:
        if self.has_camera_connection(): self._camera.release()

    def snap_image(self, imgColor: Optional[ImageColor] = ImageColor.COLOR, imgFormat: Optional[ImageFormat] = ImageFormat.RAW):
        if not self.has_camera_connection(): self.open_camera_connection()
        readSuccess, img = self._camera.read()
        if readSuccess:
            if imgColor == ImageColor.GRAY: img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            if imgFormat and imgFormat != ImageFormat.RAW: _, img = cv.imencode(imgFormat.value, img)
        return readSuccess, img

    def start_video_capture(self) -> None:
        self._shouldCaptureVideo = True
        self._captureVideoThread.start()

    def stop_video_capture(self) -> None:
        self._shouldCaptureVideo = False
        if self._captureVideoThread.is_alive(): self._captureVideoThread.join()

    def set_video_image_color(self, imgColor: ImageColor) -> None:
        self._videoImageColor = imgColor

    def set_video_image_format(self, imgFormat: ImageFormat) -> None:
        self._videoImageFormat = imgFormat

    def _video_capture_thread(self) -> None:
        while self._shouldCaptureVideo:
            _, image = self.snap_image(self._videoImageFormat, self._videoImageFormat)
            self._image = image

    def get_video_capture_image(self):
        return self._image

    def get_camera_settings(self, settings: list[OpenCvVideoCaptureProp]) -> CameraSettings:
        cameraSettings: CameraSettings = dict()
        if self.has_camera_connection():
            for setting in settings:
                value: float = self._camera.get(setting)
                cameraSettings.setdefault(setting, value)
        return cameraSettings

    def set_camera_settings(self, settings: CameraSettings) -> SupportedSettings:
        supportedSettings: SupportedSettings = dict()
        if self.has_camera_connection():
            for setting, value in settings.items():
                supported: bool = self._camera.set(value)
                supportedSettings.setdefault(setting, supported)
        return supportedSettings
