import os
from setuptools import setup, find_packages

folder = os.path.dirname(os.path.realpath(__file__))
file = '{}/requirements.txt'.format(folder)
with open(file) as f:
    install_requires = f.read().splitlines()

setup(
    name='opencv-kamera',
    version='0.0.1',
    description='Lightweight package for camera interfacing',
    packages=find_packages(),
    install_requires=install_requires,
    python_requires='>=3.6',
)
