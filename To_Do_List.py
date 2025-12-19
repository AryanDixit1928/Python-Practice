menu='''
📋 TO DO LIST
1. Add a task
2. View all tasks
3. Delete a task
4. Exit
'''
print(menu)
def add_a_task():
    task = input("Enter a task: ")
    with open("tasks.txt", "a+") as file:
        file.write(task + "\n")
    print("Task added successfully")

def view_all_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if len(tasks) == 0:
        print("No tasks available")
    else:
        for i in range(len(tasks)):
            print(i+1, ".", tasks[i].strip())

def delete_task():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if len(tasks) == 0:
        print("No tasks to delete")
    else:
        for i in range(len(tasks)):
            print(i+1, ".", tasks[i].strip())

        delete_no = int(input("Which task you want to delete: "))

        if delete_no < 1 or delete_no > len(tasks):
            print("Invalid task number")
        else:
            tasks.pop(delete_no - 1)

            with open("tasks.txt", "w") as file:
                file.writelines(tasks)

            print("Task deleted successfully")


while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_a_task()
        print(menu)
    elif choice == 2:
        view_all_tasks()
        print(menu)
    elif choice == 3:
        delete_task()
        print(menu)
    elif choice == 4:
        print("Exiting To Do List...")
        break
    else:
        print("Wrong Choice")
        print(menu)
