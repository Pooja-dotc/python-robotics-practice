import random
from sensors import IRSensor, UltrasonicSensor

print("🚀 Starting obstacle avoidance simulation...")

for step in range(5):
    # Randomly decide if object is detected (True/False)
    is_detected = random.choice([True, False])
    # Random distance between 5 cm to 50 cm
    distance = random.randint(5, 50)
    
    # Create sensor instances
    ir = IRSensor(is_detected)
    ultra = UltrasonicSensor(distance)
    
    print(f"\nStep {step+1}:")
    print(f"IR Sensor detects object: {ir.read()}")
    print(f"Ultrasonic distance: {ultra.read()} cm")
    
    # Control logic
    if ir.read() and ultra.read() < 20:
        print("Robot action: STOP! Obstacle too close.")
    elif ir.read() and ultra.read() >= 20:
        print("Robot action: Slow down, but can move.")
    else:
        print("Robot action: Path clear, move forward!")
