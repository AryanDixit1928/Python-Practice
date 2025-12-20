import csv

menu = '''
1. Write Data
2. Display Data
3. Highest Total Marks
4. Count Fail Students
5. Exit
'''

# Function to write data into CSV file
def write_data():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # writing header
        writer.writerow(["Roll", "Name", "Marks"])

        for i in range(5):
            roll = int(input(f"Enter Roll No of student {i+1}: "))
            name = input("Enter Name: ")
            marks = int(input("Enter Marks: "))

            # writing one row at a time
            writer.writerow([roll, name, marks])

    print("Data written successfully")

# Function to display CSV data
def display_data():
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Function to find highest marks
def highest_marks():
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)          # skip header

        highest = 0
        topper = ""

        for row in reader:
            marks = int(row[2])
            if marks > highest:
                highest = marks
                topper = row[1]

    print("Topper Name:", topper)
    print("Highest Marks:", highest)

# Function to count failed students
def count_fail():
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)          # skip header

        count = 0
        for row in reader:
            if int(row[2]) < 33:
                count += 1

    print("Number of failed students:", count)

# Menu driven program
while True:
    print(menu)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        write_data()
    elif choice == 2:
        display_data()
    elif choice == 3:
        highest_marks()
    elif choice == 4:
        count_fail()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
