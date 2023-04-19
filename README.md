# opencv_kamera
This monorepo contains two python packages:
- opencv_kamera
- opencv_kamera_types

**opencv_kamera** provides a class that has a simplified API for interfacing with cameras: snapping images, capturing video, getting/setting camera parameters, and simple post image processing, i.e. conversion to gray images.

**opencv_kamera_types** provides some types for interfacing with opencv_kamera that can be used both on client and server side applications. It takes inspiration from TypeScript's separation of libraries and types associated with said libraries.

This repo is primarily meant to be used with these two projects:
- kamera_cloud: https://github.com/ShaysRebellion/kamera_cloud
- camera-streaming-app: https://github.com/ShaysRebellion/camera-streaming-app
