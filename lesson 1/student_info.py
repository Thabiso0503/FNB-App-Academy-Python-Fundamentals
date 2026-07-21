# Task to student details 

# user input name 
full_name = str(input("Enter your first name :"))

# Displaying the name in Uppercase and  Title Case
print(str(full_name.upper()))
print(full_name.title())

# user input getting user's surname
surname =str(input("Enter your surname :"))
print(surname.upper())
print(surname.title())

# Displaying a formatted greeting
print(f"Greetings  , {full_name} {surname}!")

# calculating and displaying user age in months 
age = int(input("Enter your age :"))
month = int(age) * 12
print("Age in months" , month)

#getting user's favourite number and rounding it off to 2 decimal places
favourite_number = float(input("Enter your favourite number:"))
print(round(favourite_number , 2))

# Data types
print(type(full_name))
print(type(surname))
print(type(age))
print(type(favourite_number))
