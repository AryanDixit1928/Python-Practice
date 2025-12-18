import random

def print_rules():
    print("""
🎯 NUMBER GUESSING GAME 🎯
--------------------------------
RULES:
✔ The computer will choose a random number
✔ Number will be between 1 and 100
✔ You have limited attempts
✔ For each wrong guess, you'll get a hint:
   - Too High
   - Too Low
✔ Fewer attempts used = higher score

--------------------------------
DIFFICULTY LEVELS:
1️⃣ Easy   → 10 Attempts
2️⃣ Medium → 7 Attempts
3️⃣ Hard   → 5 Attempts

--------------------------------
Good Luck 🤞
""")

def play_game(attempts):
    Number = random.randint(1, 100)
    for i in range(attempts):
        num = int(input(f"Attempt {i+1}: Enter your guess: "))
        
        if num > Number:
            print("Choose a lower number")
        elif num < Number:
            print("Choose a higher number")
        else:
            print("🎉 YOU WON! 🎉")
            break
    else:
        print(f"😢 Game Over! The number was {Number}")
    
    max_score = attempts * 100
    if num == Number:
        score = (attempts - i) * 100
    else:
        score = 0
    print("Score:", score, "/", max_score)

while True:
    print("""
MENU:
1. Start Game
2. View Rules
3. Exit
""")
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        level = input("Choose Difficulty Level (1-Easy, 2-Medium, 3-Hard): ")
        if level == '1':
            play_game(10)
        elif level == '2':
            play_game(7)
        elif level == '3':
            play_game(5)
        else:
            print("Invalid Difficulty Level!")
    elif choice == '2':
        print_rules()
    elif choice == '3':
        print("Thanks for playing! Bye 👋")
        break
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
