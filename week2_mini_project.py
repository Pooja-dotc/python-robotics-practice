"""
week2_mini_project.py

Mini project: Simulate a robot arm motor.
- Create a Motor object using user input
- Calculate linear speed
- Log motor info and speed to a text file
- Read and print the log file
"""

from robot_utils import calculate_speed
# If your Motor class is in the same folder, import like:
# from week2_robot_arm import Motor
# But for now, let's define it again here for clarity:

class Motor:
    """
    Represents a motor in the robot arm.
    """
    def __init__(self, name, rpm, voltage, direction):
        """
        Initialize a Motor instance.

        Parameters:
            name (str): Motor name.
            rpm (int): Speed in RPM.
            voltage (int): Voltage in volts.
            direction (str): Rotation direction.
        """
        self.name = name
        self.rpm = rpm
        self.voltage = voltage
        self.direction = direction

    def rotate(self):
        """
        Print motor rotation info.
        """
        print(f"The {self.name} motor is rotating at {self.rpm} RPM, "
              f"with max voltage {self.voltage}V in {self.direction} direction.")

    def log_status(self, speed, filename="motor_log.txt"):
        """
        Save motor status and speed to a log file.

        Parameters:
            speed (float): Calculated linear speed.
            filename (str): Log file name.
        """
        with open(filename, "a") as file:
            file.write(f"Motor: {self.name}, RPM: {self.rpm}, Voltage: {self.voltage}V, "
                       f"Direction: {self.direction}, Linear speed: {speed:.2f} m/s\n")


def main():
    print("🤖 Robot Arm Mini Project")

    try:
        name = input("Enter motor name: ").strip()
        rpm = int(input("Enter RPM (e.g., 150): "))
        voltage = int(input("Enter voltage (V): "))
        direction = input("Enter direction (forward/reverse): ").strip()

        radius = float(input("Enter radius in meters (e.g., 0.05): "))

        # Create motor and show status
        motor = Motor(name, rpm, voltage, direction)
        motor.rotate()

        # Calculate speed using helper function
        speed = calculate_speed(rpm, radius)
        print(f"Calculated linear speed: {speed:.2f} m/s")

        # Log to file
        motor.log_status(speed)

        print("\n✅ Motor info saved to motor_log.txt")
        print("\n📄 File contents:")
        with open("motor_log.txt", "r") as file:
            print(file.read())

    except ValueError:
        print("❗ Invalid input! Please enter numbers for RPM, voltage, and radius.")

if __name__ == "__main__":
    main()
