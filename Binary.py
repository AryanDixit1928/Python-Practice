import pickle

# Menu for user
menu = '''
1. Add Employee
2. Display All Employees
3. Search Employee by ID
5. Exit
'''

# Function to add employee record
def add_employee():
    file = open("employee.dat", "ab")      # open binary file in append mode
    eid = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    salary = int(input("Enter Salary: "))

    emp = {"eid": eid, "name": name, "salary": salary}  # dictionary
    pickle.dump(emp, file)                 # write data to binary file
    file.close()
    print("Employee added successfully")

# Function to display all records
def display_all():
    try:
        file = open("employee.dat", "rb")  # open file in read mode
        while True:
            emp = pickle.load(file)        # read one record
            print(emp)
    except EOFError:                       # end of file reached
        file.close()

# Function to search employee by ID
def search_employee():
    eid = int(input("Enter Employee ID to search: "))
    found = False
    try:
        file = open("employee.dat", "rb")
        while True:
            emp = pickle.load(file)
            if emp["eid"] == eid:
                print("Record Found:", emp)
                found = True
    except EOFError:
        file.close()
        if not found:
            print("Employee not found")

# Main program (menu driven)
while True:
    print(menu)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_employee()
    elif choice == 2:
        display_all()
    elif choice == 3:
        search_employee()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
