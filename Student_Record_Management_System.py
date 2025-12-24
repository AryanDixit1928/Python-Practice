FILE = "students.txt"


def add_student():
    with open(FILE, "r") as file:
        data = file.readlines()

    roll_no = input("Enter Roll No: ")

    for line in data[1:]:
        if line.split(",")[0] == roll_no:
            print("Roll No already exists!")
            return

    name = input("Enter Name: ")
    cls = input("Enter Class: ")
    marks = input("Enter Marks: ")

    with open(FILE, "a") as file:
        file.write(f"{roll_no},{name},{cls},{marks}\n")

    print("Record added successfully")


def display_students():
    with open(FILE, "r") as file:
        print(file.read())


def search_student():
    roll = input("Enter Roll No: ")
    with open(FILE, "r") as file:
        for line in file.readlines()[1:]:
            if line.split(",")[0] == roll:
                print(line)
                return
    print("Roll No not found")


def update_marks():
    roll = input("Enter Roll No: ")
    new_marks = input("Enter New Marks: ")

    with open(FILE, "r") as file:
        data = file.readlines()

    for i in range(1, len(data)):
        parts = data[i].strip().split(",")
        if parts[0] == roll:
            parts[3] = new_marks
            data[i] = ",".join(parts) + "\n"

            with open(FILE, "w") as file:
                file.writelines(data)

            print("Marks updated successfully")
            return

    print("Roll No not found")


def delete_student():
    roll = input("Enter Roll No: ")

    with open(FILE, "r") as file:
        data = file.readlines()

    new_data = [data[0]]
    found = False

    for line in data[1:]:
        if line.split(",")[0] != roll:
            new_data.append(line)
        else:
            found = True

    if found:
        with open(FILE, "w") as file:
            file.writelines(new_data)
        print("Record deleted")
    else:
        print("Roll No not found")


def count_students():
    with open(FILE, "r") as file:
        print("Total Students =", len(file.readlines()) - 1)


def show_topper():
    with open("students.txt", "r") as file:
        data = file.readlines()[1:]   

    max_marks = 0
    topper = ""

    for line in data:
        parts = line.strip().split(",")
        marks = int(parts[3])

        if marks > max_marks:
            max_marks = marks
            topper = parts

    if topper:
        print("🏆 TOPPER DETAILS 🏆")
        print("Roll :", topper[0])
        print("Name :", topper[1])
        print("Class:", topper[2])
        print("Marks:", topper[3])
    else:
        print("No records found")



menu = """
===== STUDENT RECORD MANAGEMENT SYSTEM =====
1. Add New Student
2. Display All Students
3. Search Student by Roll Number
4. Update Student Marks
5. Delete Student Record
6. Count Total Students
7. Show Topper
8. Exit
"""


while True:
    print(menu)
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        count_students()
    elif choice == "7":
        show_topper()
    elif choice == "8":
        break
    else:
        print("Invalid choice")
