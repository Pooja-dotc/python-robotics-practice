from sensors import IRSensor, UltrasonicSensor

# Simulated sensors
ir = IRSensor(True)
ultra = UltrasonicSensor(15)  # pretend object is at 15 cm

# Read sensor data
object_detected = ir.read()
distance = ultra.read()

print(f"IR Sensor detects object: {object_detected}")
print(f"Ultrasonic distance: {distance} cm")

# Control logic
if object_detected and distance < 20:
    print("Robot action: STOP! Obstacle too close.")
elif object_detected and distance >= 20:
    print("Robot action: Slow down, but can move.")
else:
    print("Robot action: Path clear, move forward!")
