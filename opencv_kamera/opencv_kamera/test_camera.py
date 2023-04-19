import time
import pytest
from .camera import OpenCvCamera

@pytest.fixture
def camera():
    camera = OpenCvCamera()
    yield camera
    camera.stop_video_capture()
    camera.close_camera_connection()

def test_initialization(camera):
    assert not camera.has_camera_connection()

def test_camera_open_connection(camera):
    camera.open_camera_connection()
    assert camera.has_camera_connection()

def test_camera_close_connection(camera):
    camera.open_camera_connection()
    camera.close_camera_connection()
    assert not camera.has_camera_connection()

def test_camera_snap_image(camera):
    _, image = camera.snap_image()
    assert len(image) != 0

def test_camera_video_capture(camera):
    camera.start_video_capture()
    time.sleep(2) # Give some time to start up and snap image
    assert camera.get_video_capture_image().tolist() != None
