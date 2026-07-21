# Basic if/else statement script 

age = input("Enter your age:")
section_pass = input("Do you j" \
"have a vip ticket ? (yes/no)").lower()

if age >= 18  and section_pass == "yes" :
    print("Acess grantrd tot the  VIP section !!!")

elif age >= 18 :
    print("Access granted  to the general section!!!")
else :
    print("Access denied !!!")
