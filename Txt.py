menu = '''
1. Create file
2. Display all
3. Count pass
4. Exit
5. Search Roll
'''

def create_file():
    file = open("student.txt", "w")
    for i in range(5):
        roll = int(input(f"Enter Roll No of student {i+1}: "))
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))
        file.write(f"{roll},{name},{marks}\n")
    file.close()
    print("File created successfully")

def display_all():
    file = open("student.txt", "r")
    for line in file:
        print(line.strip())
    file.close()

def count_pass():
    file = open("student.txt", "r")
    count = 0
    for line in file:
        record = line.strip().split(",")
        if int(record[2]) >= 33:
            count += 1
    file.close()
    print("Number of students passed:", count)

def search_roll():
    roll = int(input("Enter roll number to search: "))
    found = False
    file = open("student.txt", "r")
    for line in file:
        record = line.strip().split(",")
        if int(record[0]) == roll:
            print("Record Found:", record)
            found = True
    file.close()
    if not found:
        print("Roll number not found")

while True:
    print(menu)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_file()
    elif choice == 2:
        display_all()
    elif choice == 3:
        count_pass()
    elif choice == 4:
        break
    elif choice == 5:
        search_roll()
    else:
        print("Invalid choice")
