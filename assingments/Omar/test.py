print("Welcome to our game. I will guess the number in your head.")

num = input("Are you ready? (Yes or No)\n").strip()

if num.lower() == "yes":
    low = 1
    high = 1000
    attempts = 0

    while True:
        guess = (low + high) // 2
        print(f"Is your number {guess}?")
        response = input("Enter 'higher', 'lower', or 'correct': ").strip().lower()
        
        if response == "higher":
            low = guess + 1
        elif response == "lower":
            high = guess - 1
        elif response == "correct":
            print(f"Great! I guessed your number in {attempts} attempts.")
            break
        else:
            print("Invalid response. Please enter 'higher', 'lower', or 'correct'.")
        
        attempts += 1
else:
    print("Okay, I will come again.")
    exit()