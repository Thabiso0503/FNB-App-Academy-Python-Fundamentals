# we want to create username and message formatter

# collect the first name
first_name = input("Enter your first name:")
first_name.lower()


last_name = input("Enter your last name: ")

# full name in Title case
full_name = f"{first_name} {last_name}".title()
print(f"Full name is: {full_name}")

# take in the user message bio , strip leading/trailing whitespace and counting the number of characters
message = input("Enter a short bio : ").strip()

# character count
char_count = len(message)
print(f"Bio character count: {char_count}")


print(f"I am {first_name}{last_name}")
message = message.replace("I am", "I'm")


# creating the user name using first initial and last name
username = f"{first_name[0]}{last_name}".lower()
print(f"Your username is : {username.lower()}")
