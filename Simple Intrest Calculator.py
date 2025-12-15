print('''
Simple Interest Calculator
Formula: S.I = (P * R * T) / 100
1 for Principal Amount
2 for Rate
3 for Time
4 for Simple Interest''')

choice = int(input("Enter Your Choice (1-4): "))

if choice == 1:
    Rate = float(input("Enter Rate (in %): "))
    Time = float(input("Enter Duration (in years): "))
    Simple_Interest = float(input("Enter Simple Interest: "))
    Principal = (Simple_Interest * 100) / (Rate * Time)
    print("Principal Amount is:", Principal)

elif choice == 2:
    Principal = float(input("Enter Principal Amount: "))
    Time = float(input("Enter Duration (in years): "))
    Simple_Interest = float(input("Enter Simple Interest: "))
    Rate = (Simple_Interest * 100) / (Principal * Time)
    print("Rate is:", Rate, "%")

elif choice == 3:
    Principal = float(input("Enter Principal Amount: "))
    Rate = float(input("Enter Rate (in %): "))
    Simple_Interest = float(input("Enter Simple Interest: "))
    Time = (Simple_Interest * 100) / (Principal * Rate)
    print("Time is:", Time, "years")

elif choice == 4:
    Principal = float(input("Enter Principal Amount: "))
    Rate = float(input("Enter Rate (in %): "))
    Time = float(input("Enter Duration (in years): "))
    Simple_Interest = (Principal * Rate * Time) / 100
    print("Simple Interest is:", Simple_Interest)

else:
    print("Invalid Choice! Please enter 1, 2, 3, or 4.")