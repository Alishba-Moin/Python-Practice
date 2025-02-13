import random

# Game Instructions
print("\n===== 🎲 Welcome to Snake, Water, Gun Game 🎲 =====")
print("Choose: 's' for 🐍 Snake, 'w' for 💧 Water, 'g' for 🔫 Gun")
print("Enter 'q' to quit anytime.")

# Score Variables
user_score = 0
computer_score = 0
draws = 0

# Mapping Choices
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

while True:
    # Taking User Input
    youstr = input("\n🎮 Enter Your Choice (s/w/g): ").lower()

    # Quit Condition
    if youstr == 'q':
        print("\nExiting Game... Thanks for Playing! 🏆")
        break

    # Check for Invalid Input
    if youstr not in youDict:
        print("❌ Invalid choice! Please enter 's', 'w', or 'g'.")
        continue  # Ask again

    you = youDict[youstr]  # Convert user choice to numeric value

    # Generate Computer Choice
    computer_choice = random.choice(["s", "w", "g"])
    computer = youDict[computer_choice]

    print(f"\n🕹️  You chose: {reverseDict[you]}")
    print(f"💻 Computer chose: {reverseDict[computer]}")

    # Win/Loss Logic
    if you == computer:
        print("🔄 It's a Draw!")
        draws += 1
    elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
        print("🎉 You Win! 🏆")
        user_score += 1
    else:
        print("😢You Lose!")
        computer_score += 1

    # Display Scoreboard
    print("\n🏆 Scoreboard:")
    print(f"  👤 You: {user_score}  \n 💻 Computer: {computer_score}  \n 🤝 Draws: {draws}")

print("\n===== Game Over! Final Score =====")
print(f"👤 You: {user_score}  | 💻 Computer: {computer_score}  | 🤝 Draws: {draws}")
print("Thanks for playing!")
