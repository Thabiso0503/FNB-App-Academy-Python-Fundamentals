# We are going to learn about loops 

# While loop it acts like a continous statement it checks a condtion , as long as that condition remains true it keeps running that code over and over again  
# A while loop is used when the number of iterations is unknown in advance. The loop continues executing as long as a specified condition remains True.

# A countdown  using while loop

count = 4

while count > 0 :
    print(count)
    count = count - 1

print("Blast Off !")

# let us build a  simple rep counter for the gym

for rep in range(1,4) :
    print(f"This is rep no.{rep}")

# Combining loops with decision-making

# A guessing game

secret_word = "python"


while True:
    guess = input("Enter the programming we are using :").lower()

    if guess == secret_word:
        print("Ypu guessed the correct language !!!")
        break
    else:
        print("Incorrect guess try again !!!!")
