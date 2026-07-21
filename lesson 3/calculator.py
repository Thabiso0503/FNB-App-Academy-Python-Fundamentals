# Build a calculator that takes two numbers as input and performs all four basic arithmetic operations

# Multi-Function Calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Basic calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print("\n==============================")
print(f"{'Operation':<20}{'Result'}")
print("==============================")

print(f"{'Addition':<20}{round(addition, 2)}")
print(f"{'Subtraction':<20}{round(subtraction, 2)}")
print(f"{'Multiplication':<20}{round(multiplication, 2)}")

# Division calculations
if num2 == 0:
    print(f"{'Division':<20}Undefined (cannot divide by zero)")
    print(f"{'Floor Division':<20}Undefined (cannot divide by zero)")
    print(f"{'Modulus':<20}Undefined (cannot divide by zero)")
else:
    division = num1 / num2
    floor_division = num1 // num2
    modulus = num1 % num2

    print(f"{'Division':<20}{round(division, 2)}")
    print(f"{'Floor Division':<20}{round(floor_division, 2)}")
    print(f"{'Modulus':<20}{round(modulus, 2)}")
