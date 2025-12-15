print('''
1 for Addition
2 for Subtraction
3 for Multiplication
4 for Division
5 for Exit
''')

while True:
    choice = int(input("Enter Your Choice: "))

    if choice == 5:
        print("Exiting the calculator. Goodbye!")
        break

    if choice in [1, 2, 3, 4]:
        num_1 = float(input("Enter First Number: "))
        num_2 = float(input("Enter Second Number: "))

        if choice == 1:
            print("Result:", num_1 + num_2)

        elif choice == 2:
            print("Result:", num_1 - num_2)

        elif choice == 3:
            print("Result:", num_1 * num_2)

        elif choice == 4:
            if num_2 == 0:
                print("Error: Division by zero not allowed")
            else:
                print("Result:", num_1 / num_2)
    else:
        print("Invalid Choice! Please enter between 1 and 5.")
