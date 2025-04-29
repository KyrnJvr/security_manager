# Name: Kyle Javier
# Date: 16/04/2025

import csv

'''
BYOD Security Manager App

The university Information Technology services (ITS) have decided to create a UniSC BYOD security manager for student/staff devices and the university has asked you to create the app. This app will include information such as last patched, password last changed, software licensing (when expire etc) specifically for personal devices that users (staff and students) are bringing onto the university campus - university hardware such as staff laptops and lab computers are centrally managed).

The user should be able to:

1. Create a security task list.
2. Load their security task list from a file or database (see below).
3. Add security tasks.
4. Update security tasks (change priority, mark complete, change date)
5. View the task list.
6. Delete tasks.
7. Save their task list.

Implement features like due dates, priorities, and categories for security updates (and password changing). So, a task could be:


Task details        Due Date    Priority    Category    Completed

Change phone PIN    7/6/2025    A           Mobile      Not Yet


Load and save the security task data to a file (e.g., JSON or CSV) so that students and ITS can resume  later. You will need to identify this file based on the student/staff’s details (student ID/Staff ID ??). This will function as a login – without the need for a password.

Advanced.

1. Use classes and objects to model your data structures.
2. Allow ITS to have a system that manages all staff and students (create multiple lists that have many tasks within them). 
3. Add search functionality to find specific security tasks based on keywords or dates.
4. Add a password to make your system a bit more secure.
5. Use a database rather than individual files

'''
# Security Task Class (each is an instance of a task)
class SecurityTask:
    def __init__(self, task_details, due_date, priority, category, status):
        self.task_details = task_details
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.status = status
    
    def to_string(self):
        return f"{self.task_details},{self.due_date},{self.priority},{self.category},{self.status}"


def readFromFile(file):
    '''Read from a file of tasks'''
    tasks = [] # empty list to put tasks to from the file
    with open(file, "r", newline='') as data_file:
        data_csv = csv.DictReader(data_file) 
        for line in data_csv:
            # create a Security Task Object for each line in the file
            task = SecurityTask(
                line["Task Details"],
                line["Due Date"],
                line["Priority"],
                line["Category"],
                line["Status"]
            )
            tasks.append(task) # Add each task to a list
        data_file.close() # clsoe the file
    return tasks


def writeToFile(file, tasks):
    '''Writes to a file'''
    data_file = open(file, "w")
    for task in tasks:
        data_file.write(f"{task.task_details},{task.due_date},{task.priority},{task.category},{task.status}")
    data_file.close()


def viewTasks(list_of_tasks):
    '''View tasks in a table like format'''
    print(f"{'':<5} {'Task':<30} {'Due Date':<12} {'Priority':<10} {'Category':<10} {'Status':<12}")
    print("-"*90)

    # iterate through the whole list and print each task
    for index, task in enumerate(list_of_tasks, start=1):
        print(f"{index:<5} {task.task_details:<30} {task.due_date:<12} {task.priority:<10} {task.category:<10} {task.status:<12}")

        
# Initialise empty task list to be populated when user adds new task/s
tasks = readFromFile("tasksFile.csv")


# Start of program
while True:
    # print main menu options
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")

    # Ask user for service to use
    choice = int(input("Enter choice: "))
    print() # for readability

    # if user selected to add a new task
    if choice == 1:

        task_details = input("Enter task details: ").title()
        due_date = input("Enter due date: ")
        priority = input("Enter priority level: ").title()
        category = input("Enter category: ").title()
        status = input("Enter status: ").title()

        new_task = SecurityTask(task_details, due_date, priority, category, status)
        # add new task to the list
        tasks.append(new_task)
        # print success message
        print("Task added successfully!")

        writeToFile("tasksFile.csv", tasks)
    
    # if user selects to view all tasks
    elif choice == 2:
        viewTasks(tasks)
        print()

    # if user selects to update a task
    elif choice == 3:
        # view the list of task for the user to pick which one to update
        if tasks:
            viewTasks(tasks)

            # ask user which task to update
            task_number = int(input("Enter task number to update: "))
            print() # for readability

            # print task options to choose from
            print("a. task details")
            print("b. due date")
            print("c. priority")
            print("d. category")
            print("e. status")

            # ask user which task attribute to update
            what_to_update = input("What do you want to update?: ").lower()

            '''
            
            codition template

            if user selects to update {task attribute} THEN
                ask for new value
                update task accordingly
                print success message
            else:
                print invalid choice

            
            '''

            # if user selects to update task details
            if what_to_update == 'a':
                new_value = input("Enter new task details: ")
                tasks[task_number - 1].task_details = new_value
                print("Successfully updated task details!")

            # if user selects to update due date
            elif what_to_update == 'b':
                new_value = input("Enter new due date: ")
                tasks[task_number - 1].due_date = new_value
                print("Successfully updated due date!")

            # if user selects to update priority
            elif what_to_update == 'c':
                new_value = input("Enter new priority: ")
                tasks[task_number - 1].priority = new_value
                print("Successfully updated priority!")

            # if user selects to update category
            elif what_to_update == 'd':
                new_value = input("Enter new category: ")
                tasks[task_number - 1].category = new_value
                print("Successfully updated category!")

            # if user selects to update status
            elif what_to_update == 'e':
                new_value = input("Enter new status: ")
                tasks[task_number - 1].status = new_value
                print("Successfully updated status!")
            else:
                print("Invalid choice, please try again.")            

        # if task list is empty
        else:
            print("No task available to update, please add a new one and try again.")

    elif choice == 5:
        print("Exiting the program..")
        break


        