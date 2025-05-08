# Name: Kyle Javier
# Date: 16/04/2025

import csv
import os

'''

PSEUDOCODE: Detailed Design

DEFINE SecurityTask class
    
    INIT CONSTRUCTOR(task details, due date, priority, category, status)
        set private 'attributes' = (task details, due date, priority, category, status)

    // Getters and Setters for all attributes

    METHOD getTaskDetails()
        return self.__task_details
    
    METHOD setTaskDetails(taskDetails)
        set self.__task_details = taskDetails

    // similar methods for other attributes (due date, priority, category, status)

END CLASS


METHOD readFromFile(file)
    DECLARE empty list of tasks
    OPEN file for reading
        READ data from the file
        FOR each line in the file
            CREATE new SecurityTask Object with line values
            APPEND task to the list of tasks
        END FOR
    CLOSE file
    RETURN the list of tasks


METHOD writeToFile(file, tasks)
    OPEN file for writing
        WRITE csv header row
        FOR each task in tasks list
            WRITE task attributes to csv row
        END FOR
    CLOSE file

    
METHOD viewTasks(list_of_tasks)
    PRINT table header
    PRINT divider line
    FOR each task with index in the list of tasks
        PRINT formatted row with task details
    END FOR


// Main Program

PROMPT user for ID or Name
SET 'users' folder
CREATE folder if it doesn't exist
SET filename based on user ID or Name

IF file doesn't exist
    CREATE new file with header
    SET a task list for user
ELSE
    PRINT welcome message
    SET task list EQUAL readFromFile(filename) method
END IF

// Main Program Loop

WHILE true
    DISPLAY menu options
    PROMPT user for choice

    IF choice is invalid
        PRINT error message
        CONTINUE LOOP
    END IF

    IF choice is 1 (Add new task)
        PROMPT for (task details, due date, priority, category, status)
        CREATE new SecurityTask Object with inputs
        ADD task object to tasks list
        CALL writeToFile with filename and tasks list
        PRINT success message
    
    ELSE IF choice is 2 (View tasks)
        IF task list is not empty
            CALL viewTask method with tasks list
        ELSE
            PRINT no task/s message
        END IF
    
    ELSE IF choice is 3 (Update task)
        IF tasks list is not empty
            CALL viewTask method with tasks list
            PROMPT user for task number to update

            IF task number is valid
                INDICATE to user what task they are updating
                DISPLAY update options
                PROMPT user for task attribute to update

                IF updating task details
                    PROMPT new value
                    VALIDATE input not empty
                    UPDATE task
                    CALL writeToFile method
                    PRINT success message

                ELSE IF // similar for other attributes (for priority, category and status 
                        VALIDATE only from list of allowed values) 
                ELSE IF canceling update
                    BREAK from update
                END IF
            END IF
        ELSE
            PRINT no task message
        END IF

    ELSE IF choice is 4 (Delete task)
        IF task list if not empty
            CALL viewTasks method with tasks list
            PROMPT user for task number to delete

            IF task number is valid
                PROMPT user for confirmation

                IF confirmed
                    DELETE task from list
                    CALL writeToFile method
                    PRINT success message
                ELSE
                    PRINT cancellation message
                END IF
            END IF
        ELSE
            PRINT no task message
        END IF

    ElSE IF choice is 5 (Exit)
        PRINT exit message
        BREAK from main loop

    ELSE
        PRINT invalid option message
    END IF
END WHILE     
                
'''
# Security Task Class (each is an instance of a task)
class SecurityTask:
    def __init__(self, task_details, due_date, priority, category, status):
        self.__task_details = task_details
        self.__due_date = due_date
        self.__priority = priority
        self.__category = category
        self.__status = status
    
    def getTaskDetails(self):
        return self.__task_details

    def setTaskDetails(self, taskDetails):
        self.__task_details = taskDetails
    
    def getDueDate(self):
        return self.__due_date
    
    def setDueDate(self, dueDate):
        self.__due_date = dueDate
    
    def getPriority(self):
        return self.__priority
    
    def setPriority(self, priority):
        self.__priority = priority
    
    def getCategory(self):
        return self.__category
    
    def setCategory(self, category):
        self.__category = category

    def getStatus(self):
        return self.__status
    
    def setStatus(self, status):
        self.__status = status


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
                task.getTaskDetails(),
                task.getDueDate(),
                task.getPriority(),
                task.getCategory(),
                task.getStatus() 
            ])


def viewTasks(list_of_tasks):
    '''View tasks in a table like format'''
    print(f"{'':<5} {'Task':<30} {'Due Date':<12} {'Priority':<10} {'Category':<10} {'Status':<12}")
    print("-"*90)

    # iterate through the whole list and print each task
    for index, task in enumerate(list_of_tasks, start=1):
        print(f"{index:<5} {task.getTaskDetails():<30} {task.getDueDate():<12} {task.getPriority():<10} {task.getCategory():<10} {task.getStatus():<12}")


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
    print(f"Welcome {user}!") # print current user
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
        task_details = input("Enter task details (e.g. Install anti-virus): ").title()
        due_date = input("Enter due date (DD/MM/YYYY): ")
        priority = input("Enter priority level (A, B, C): ").title()
        category = input("Enter category (e.g. Mobile, Desktop, Tablet): ").title()
        status = input("Enter status (e.g. Not Yet, In Progress, Completed): ").title()

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

            try:
                task_number = int(input("\nEnter task number to update: "))

                if task_number  < 1 or task_number > len(tasks): # is task number entered is less than 1 or greater than length of tasks
                    print(f"Please enter a valid number between 1 and {len(tasks)}") # print error message
                    continue
                    
                print(f"You are updating the task: '{tasks[task_number - 1].getTaskDetails()}'. \n")

                    
                print("a. task details")
                print("b. due date")
                print("c. priority")
                print("d. category")
                print("e. status")
                print("f. cancel update")

                what_to_update = input("\nWhat would you like to update?: ").lower()

                if what_to_update == 'a': #* TASK DETAILS: update validation
                    new_value = input("Enter new task details: ")

                    if not new_value.strip():
                        print("Task details cannot be empty. Update Cancelled.")
                    else:
                        tasks[task_number - 1].setTaskDetails(new_value.title())
                        writeToFile(filename, tasks)
                        print("Task details updated successfully.")

                elif what_to_update == 'b': #* DUE DATE: update validation
                    while True:
                        new_value = input("Enter new due date (dd/mm/yy): ")

                        if len(new_value.split('/')) == 3: # small validation to have consistent date formats
                            break
                        print("Invalid date format. Please use DD/MM/YYYY format.")
                    tasks[task_number - 1].setDueDate(new_value)
                    writeToFile(filename, tasks)
                    print("Due date updated successfully .")

                elif what_to_update == 'c': #* PRIORITY: update validation 

                    priorities = ['A', 'B', 'C'] # list of valid priorities

                    while True:
                        new_value = input(f"Enter new priority ({','.join(priorities)}): ").upper()

                        if new_value in priorities: # validation to restrict priority to certain values only
                            break
                        print(f"Invalid priority. Please choose from: {','.join(priorities)}")

                    tasks[task_number - 1].setPriority(new_value.title())
                    writeToFile(filename, tasks)
                    print("Priority updated successfully.")
                
                elif what_to_update == 'd': #* CATEGORY: update validation

                    categories = ['Mobile', 'Desktop', 'Tablet']

                    while True:
                        new_value = input(f"Enter new category ({','.join(categories)}): ").title()

                        if new_value in categories: #* restrict categories to certain values
                            break
                        print(f"Invalid Category. Please choose from: {','.join(categories)}")
                    
                    tasks[task_number - 1].setCategory(new_value.title())
                    writeToFile(filename, tasks)
                    print("Category updated successfully.")

                elif what_to_update == 'e': #* STATUS: update validation
                    
                    statuses = ['Not Yet', 'In Progress', 'Completed']

                    while True:
                        new_value = input(f"Enter new status ({','.join(statuses)}): ").title()

                        if new_value in statuses: #* restrict status to certain values
                            break
                        print(f"Invalid Status. Please choose from: {','.join(statuses)}")
                    
                    tasks[task_number - 1].setStatus(new_value.title())
                    writeToFile(filename, tasks)
                    print("Status updated successfully.")
                
                elif what_to_update == 'f': #* CANCEL: update
                    print("Cancelling update..")
                    break

            except ValueError:
                print("Please enter a valid number.")
                continue         

        # if task list is empty
        else:
            print("No task available to update, please add a new one and try again.")

    elif choice == 4:
        if tasks:
            viewTasks(tasks)

            try:

                task_number= int(input("\nEnter task to delete: "))

                if task_number <1 or task_number > len(tasks):
                    print(f"Please enter a valid number between 1 and {len(tasks)}")
                
                # task to delete (adjusted for zero based indexing)
                task_to_delete = tasks[task_number - 1]


                while True:
                    confirm = input(f"Are you sure you want to delete '{task_to_delete.getTaskDetails()}'? (y/n): ").lower()

                    if confirm == 'y':
                        del tasks[task_number - 1] # delete task from the list

                        writeToFile(filename, tasks) # re write the task in the file

                        print("Task successfully deleted.") # print success message

                        break 
                    elif confirm == 'n':
                        print("Deletion cancelled.") # print message of deletion cancellation
                        break
                    else:
                        print("Invalid choice, please enter (y/n).") # print error message of invalid choice
                        continue



            except ValueError:
                print("Please enter a valid number.")
                continue
        
        else:
            print("There is no task available to delete.")
            
    elif choice == 5:
        print("Exiting the program..")
        break
    else:
        print("Please enter a valid option (1-5).")