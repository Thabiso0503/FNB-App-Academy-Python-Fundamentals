# Build an interactive program that asks an arcade player for their game score

# Start an intentional infinite loop - it will only stop when we hit 'break'
while True:
    # Ask the player to enter their score, right next to the flashing cursor
    game_score = input("Enter the score next to the flashing cursor: ")

    # Check the raw input as a string first (before converting to int),
    # since trying to int() the word "stop" would crash the program.
    # .strip() removes stray spaces, .lower() handles "Stop", "STOP", etc.
    if game_score.strip().lower() == "stop":
        # Let the player know the session is over
        print("Game session ended!")
        # Exit the while loop
        break
    else:
        # At this point we know it's not "stop", so it's safe to convert to a number
        game_score = int(game_score)

        # Check if the score counts as a new high score
        if game_score > 100:
            print("Wow! That's a new high score!")
        else:
            print("Good try, keep playing!")
