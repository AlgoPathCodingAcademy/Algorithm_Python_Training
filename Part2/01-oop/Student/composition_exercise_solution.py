class Camera:
    def record(self):
        print("Recording video.")

class AdvancedCamera(Camera):
    def record_4k(self):
        print("Recording in 4K resolution.")

class Photographer:
    def __init__(self, camera):
        self.camera = camera  # Photographer uses the camera that's passed in

# Usage
standard_camera = Camera()
advanced_camera = AdvancedCamera()

# Different photographers with different cameras
standard_photographer = Photographer(standard_camera)
advanced_photographer = Photographer(advanced_camera)

standard_photographer.camera.record()  # Outputs: Recording video.
advanced_photographer.camera.record_4k()  # Outputs: Recording in 4K resolution.
