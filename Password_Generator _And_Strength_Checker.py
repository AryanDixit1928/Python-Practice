import random

Menu = '''
Menu:
1. Password Strength Checker
2. Password Generator
3. Exit
'''

print(Menu)

def Password_Strength_Checker():
    print("""
🔐 PASSWORD STRENGTH RULES 🔐
--------------------------------
To get a STRONG password, make sure it contains:

✔ Minimum 8 characters
✔ At least 1 Uppercase letter (A–Z)
✔ At least 1 Lowercase letter (a–z)
✔ At least 1 Number (0–9)
✔ At least 1 Special Character (! @ # $ - & * _ ?)

--------------------------------
💡 Tip: Mix all types for better security!
""")

    Password = input("Enter Your Password:- ")
    Point = 0
    special_chars = ['!','@','#','$','-','&','*','_','?']
    if len(Password) >= 8:
        Point += 1
    for x in Password:
        if x.isupper():
            Point += 1
            break
    for x in Password:
        if x.islower():
            Point += 1
            break
    for x in Password:
        if x.isnumeric():
            Point += 1
            break
    for x in Password:
        if x in special_chars:
            Point += 1
            break
    if Point <= 2:
        print("Your Password Strength Is Weak :(")
    elif Point <= 4:
        print("Your Password Strength Is Medium :)")
    else:
        print("Your Password Strength Is Strong ;)")

    print("Your Password Score is", Point, "/5")


def Password_Generator():
    import random

    special_chars = ['!','@','#','$','-','&','*','_','?']
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    capital_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    sc = random.choice(special_chars)
    num = random.choice(numbers)

    alpha = (
        random.choice(alphabets) +
        random.choice(alphabets) +
        random.choice(alphabets) +
        random.choice(alphabets) +
        random.choice(alphabets)
    )

    caps = random.choice(capital_letters)

    Generated_password = sc + num + alpha + caps
    print("Generated Password:", Generated_password)



while True:
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        Password_Strength_Checker()
        print(Menu)

    elif choice == 2:
        Password_Generator()
        print(Menu)

    elif choice == 3:
        print("Thanks for using the tool 🔐")
        break

    else:
        print("Invalid Choice! Choose from 1 to 3.")
        print(Menu)
