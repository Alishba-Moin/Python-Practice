import random

def play_game():
    num = random.randint(1, 30)
    guesses = 0

    print("\n🎯 Welcome to the Number Guessing Game!")
    print("🔢 I'm thinking of a number between 1 and 30.\n")

    while True:
        user = int(input("👉 Enter your guess: "))
        guesses += 1

        if user > num:
            print("📉 Too high! Try a smaller number.")
        elif user < num:
            print("📈 Too low! Try a bigger number.")
        else:
            print(f"\n🎉 Congratulations! You guessed the number {num} correctly.")
            print(f"✅ It took you {guesses} attempts.\n")
            break  

# Game loop to allow replay
while True:
    play_game()
    again = input("Play again? (yes/no): ").lower()

    if again != "yes":  # No need to check for multiple options
        print("👋 Thanks for playing! Goodbye.")
        break