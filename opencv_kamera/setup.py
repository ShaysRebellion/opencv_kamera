from setuptools import setup, find_packages

setup(
    name='opencv-kamera',
    version='0.0.1',
    description='Lightweight package for camera interfacing',
    packages=find_packages(),
    install_requires=['opencv_kamera_types==0.0.1'],
    python_requires='>=3.6',
)
