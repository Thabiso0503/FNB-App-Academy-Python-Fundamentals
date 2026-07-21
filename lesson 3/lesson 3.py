# Our code is goinf to take 3 inputs from the user and output it on our terminal

# adding two numbers 

num1 = input("Enter the first number")
num2 = input("Enter the second number")

print(int(num1) + int(num2))

# Core data types 
# str : String/Text  "hello"
# int : Integer/Whole number  5  -1  10
# float:  Decimal Numbers 5.34  6.1 
# bool:   True or False 

# Type casting - moving from one datatype to another 

# Calculating a tip

bill = float(input("Enter the bill: R"))
tip = 0.15 # written in decimal

val_tip = bill * tip
total_cost = bill + val_tip

print(f"Here is the tip: {val_tip}")
print(f"Here is the tip: {round(val_tip,2)}rounded")


print(f"Here is the total_cost: {total_cost}")
print(f"Here is the total_cost: {round(total_cost,2)}rounded")
