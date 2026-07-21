# We want to create a secure password hint tool

# ask the user their password
password = input("Enter your password:").strip()

# Grab the first and last letter
first_letter = password[0]
last_letter = password[-1]

# Print a hint using only those two letters , uppercased
print(f"Your password starts with {first_letter.upper()} and ends with {last_letter.upper()}")
