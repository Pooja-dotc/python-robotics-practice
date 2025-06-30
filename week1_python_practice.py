# Day 1 : Write a script

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, {name}! You are {age} years old.")


# Day 2 :Write a script that prints numbers 1 to 10. and Check if a number is even or odd.

for i in range(1,11):
    if i %2==0:
        print(f"{i} is an even number.")
    else:
        print(f"{i} is an odd number.")
    
#Day 3 :Write functions: add_numbers(a, b) → returns sum, is_even(n) → returns True if even
    
def add_numbers(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

result = add_numbers(5, 6)

if is_even(result):
    print(is_even(result))
else:
    print(is_even(result))

#Day 4 : Make list of your favorite sensors, Dictionary of motor specs and Print each item.

favorite_sensors = ["IR sensor", "Ultrasonic", "Camera"]

print("Favorite sensors:")
for sensor in favorite_sensors:
    print(sensor)

motor = {"type": "DC motor", "voltage": 6, "rpm": 200}

print("\nMotor specifications:")
for key, value in motor.items():
    print(f"{key}: {value}")

# Day 5 : Create class Sensor: 

class Sensor:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def show_info(self):
        print(f"{self.name} is a {self.type} sensor.")

ir = Sensor("IR Sensor", "Infrared")
ir.show_info()


# Day 6: Mini project idea: Ask user to enter 3 favorite sensors → save in file sensors.txt and Read and print the list from the file.

Sensor = input("enter your 3 favorite sensors by using comma: ")
favorite_sensors = Sensor.split(",")
with open("Sensor.txt", "w") as file:
    for sensor in favorite_sensors:
        file.write(sensor.strip() + "\n")
        
print("Your sensors have been saved to Sensor.txt ")