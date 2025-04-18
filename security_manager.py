# Name: Kyle Javier
# Date: 16/04/2025

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
    

# Initialise empty task list to be populated when user adds new task/s
task_list = []

# Start of program
while True:
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Exit")
        