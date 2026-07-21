#  We want to create a South African Fuel Cost Calculator

# Asking the user how many kilometers they want to drive
kilometers = float(input("Enter the number of kilometers you want to drive:"))

# Asking them the current petrol per liter 
petrol_price = float(input("Enter the current petrol price per liter in : R"))

# Formula  for liters needed for every 10 km
liters_needed = kilometers /10 

# Calculating the total cost 
total_cost = liters_needed * petrol_price
print(f"Total fuel cost: R{round(total_cost, 2)}")
