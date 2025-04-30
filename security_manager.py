# Name: Kyle Javier
# Date: 16/04/2025

import csv
import os

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
    with open(file, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Task Details", "Due Date", "Priority", "Category", "Status"])
        
        for task in tasks:
            writer.writerow([
                task.to_string() # using the built in to_string method to write into the csv file
            ])


def viewTasks(list_of_tasks):
    '''View tasks in a table like format'''
    print(f"{'':<5} {'Task':<30} {'Due Date':<12} {'Priority':<10} {'Category':<10} {'Status':<12}")
    print("-"*90)

    # iterate through the whole list and print each task
    for index, task in enumerate(list_of_tasks, start=1):
        print(f"{index:<5} {task.task_details:<30} {task.due_date:<12} {task.priority:<10} {task.category:<10} {task.status:<12}")


# -- Start Main Program --

user = input("Enter your student/staff details (ID or Name): ".strip()) # ask user for identity

folder = "users"
os.makedirs(folder, exist_ok=True) # make a users folder if it doesn't exist
filename = os.path.join(folder, f"{user}.csv") # example fileanmae would be users/{user}.csv}

if not os.path.exists(filename): # if there is no existing file for the user
    print(f"No file found for: {user}. Creating a new one..")
    with open(filename, "w", newline='') as f: # create a new one
        writer = csv.writer(f)
        writer.writerow(["Task Details", "Due_Date", "Priority", "Category", "Status"]) # writing a header for the user file
    tasks = [] # empty list for the user to store tasks into
else: # if user exists
    print(f"Current User: {user}") # print current user
    tasks = readFromFile(filename) # call readFromFile function to get a list of tasks from users last session

# -- Main Program Loop --
while True:
    print("\nMenu Options:")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")

    # Ask user for service to use
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid choice, Please enter a number (1-5).")
        continue

    # if user selected to add a new task
    if choice == 1:
        # acquire task details from the user
        task_details = input("Enter task details: ").title()
        due_date = input("Enter due date: ")
        priority = input("Enter priority level: ").title()
        category = input("Enter category: ").title()
        status = input("Enter status: ").title()

        # create a new task object and store user input
        new_task = SecurityTask(task_details, due_date, priority, category, status)
        tasks.append(new_task) # append new_task to the list
        writeToFile(filename, tasks) # write the task to the file

        # print success message
        print("Task added successfully!")
    
    # if user selects to view all tasks
    elif choice == 2:
        if tasks:
            viewTasks(tasks)
        else:
            print("\nYou don't have any tasks available. Please add some and try again.")
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
    else:
        print("Please enter a valid option (1-5).")