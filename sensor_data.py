from sensors import IRSensor, UltrasonicSensor, CameraSensor

# Simulated sensor instances
ir = IRSensor(True)
ultra = UltrasonicSensor(30)
cam = CameraSensor(["ball", "cube"])

# Collect readings
readings = []

# Let's say we collect 3 readings
for i in range(3):
    reading = {
        "IR": ir.read(),
        "Distance": ultra.read() + i * 5,   # fake change in distance
        "Objects": cam.read()
    }
    readings.append(reading)

# Print all readings
print("Collected sensor readings:")
for r in readings:
    print(r)

# Create a dictionary mapping reading number -> data
readings_dict = {i+1: r for i, r in enumerate(readings)}

print("\nReadings dictionary:")
for number, data in readings_dict.items():
    print(f"Reading {number}: {data}")
