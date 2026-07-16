# Start an intentional infinite loop
while True:
    # Ask the user for their game score next to a prompt
    user_input = input("Enter a game score: ")
    
    # Clean up the input and check for the exit word
    if user_input.strip().lower() == "stop":
        print("Game session ended!")
        break  # Shut down the loop
        
    # Cast input into an integer and evaluate the score
    score = int(user_input)
    if score > 100:
        print("Wow! That’s a new high score!")
    else:
        print("Good try, keep playing!")
