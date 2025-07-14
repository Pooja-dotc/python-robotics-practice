from sensors import IRSensor, UltrasonicSensor

# Simulated sensors
ir = IRSensor(True)
ultra = UltrasonicSensor(30)

print("Starting robot simulation...")

# Run for 3 time steps
for step in range(3):
    # Fake distance changing each step (simulate robot moving closer)
    current_distance = ultra.read() - (step * 10)
    
    print(f"\nStep {step+1}:")
    print(f"IR Sensor detects object: {ir.read()}")
    print(f"Ultrasonic distance: {current_distance} cm")
    
    # Control logic
    if ir.read() and current_distance < 20:
        print("Robot action: STOP! Obstacle too close.")
    elif ir.read() and current_distance >= 20:
        print("Robot action: Slow down, but can move.")
    else:
        print("Robot action: Path clear, move forward!")
