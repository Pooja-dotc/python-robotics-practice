class IRSensor:
    def __init__(self, is_object_detected=False):
        self.is_object_detected = is_object_detected

    def read(self):
        return self.is_object_detected


class UltrasonicSensor:
    def __init__(self, distance_cm=0):
        self.distance_cm = distance_cm

    def read(self):
        return self.distance_cm


class CameraSensor:
    def __init__(self, objects_seen=None):
        if objects_seen is None:
            objects_seen = []
        self.objects_seen = objects_seen

    def read(self):
        return self.objects_seen


if __name__ == "__main__":
    ir = IRSensor(True)
    print(f"IR Sensor detects object: {ir.read()}")

    ultra = UltrasonicSensor(25)
    print(f"Ultrasonic sensor distance: {ultra.read()} cm")

    cam = CameraSensor(["ball", "cube"])
    print(f"Camera sees: {cam.read()}")
