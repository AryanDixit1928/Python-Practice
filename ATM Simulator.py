PIN =2511
Account_Number =123456789
Balance=10000
Menu=('''
Menu:
1.Check Balance
2.Deposit Money
3.Withdraw Money
4.Pin Change
5.Check Pin
6.Exit  ''')
def Check_Balance():
        global Balance
        print(Balance)
def Deposit_Money():
        global Balance
        Deposited_Money=int(input("How Much Money You Want To Deposit:"))
        if Deposited_Money>0:
            Balance=Balance+Deposited_Money
            print(Deposited_Money," Ruppees Are Succesfully Deposited")
            print("Balance:",Balance)
        else:
               print("Error!!!")
def Withdraw_Money():
        global Balance
        Withdrawn_Money=int(input("How Much Money You Want To Withdraw:"))
        if Withdrawn_Money>0:
            if Withdrawn_Money>Balance:
                print("Insufficient Balance")
            elif Withdrawn_Money<=Balance:
                print(Withdrawn_Money,"Ruppees Succesfuly Withdrawn")
                Balance=Balance-Withdrawn_Money
                print("Balance:",Balance)
        else:
               print("Error!!!")
def Pin_Change():
        global PIN
        Current_Pin=int(input("Enter Current Pin:"))
        if Current_Pin==PIN:
                New_Pin=int(input("Enter Your New Pin:"))
                New_Pin1=int(input("Enter New Pin Again:"))
                if New_Pin==New_Pin1:
                    PIN=New_Pin
                    print("PIN Changed Succesfully")

                if New_Pin1!=New_Pin:
                       print("PIN Does Not Match")
        else:
                print("Wrong Pin")
def check_pin():
        PIN1=int(input("Enter Your PIN:"))
        if PIN1==PIN:
            print("You have entered correct pin")
        else:
            print("Entered PIN is wrong!!!")

ac=int(input("Enter Your Account Number:"))
pn=int(input("Enter Your Pin:"))
if ac==Account_Number and pn==PIN:
        print(Menu)
        while True:
                Choice=int(input("Enter Your Choice:"))
                if Choice == 1:
                        Check_Balance()
                        print(Menu)
                elif Choice == 2:
                        Deposit_Money()
                        print(Menu)
                elif Choice == 3:
                        Withdraw_Money()
                        print(Menu)
                elif Choice == 4:
                        Pin_Change()
                        print(Menu)
                elif Choice == 5:
                        check_pin()
                elif Choice == 6:
                       print("Thank You For Using The ATM ;)")
                       break
                else:
                        print("Invalid Choice! Choose From 1 to 6")
                        
                        
                


    
