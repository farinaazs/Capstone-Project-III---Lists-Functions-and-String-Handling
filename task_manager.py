""""
==== Capstone Project III ====

- Create a Login Section
    > read usernames and passwords from the user.txt file to validate the user
    > the user to enter their username and password until it matches
    > once validated, open the menu section

- Create 2 different Menu Sections
    >> if the user_name IS "admin" and the pass_word is "adm1n"
        - open following menu:
            r       - Registering a User
            a       - Adding a Task
            va      - View all Tasks
            vm      - View my Task
            ds      - Display Statistics
            gr      - Generate Reports
            e       - Exit
    >> if the user_name is NOT "admin and the pass_word is NOT "adm1n"
        - open following menu:
            r       - Registering a User
            a       - Adding a Task
            va      - View all Tasks
            vm      - View my Task
            e       - Exit

- If menu == "r       - Registering a User"
    >> if the user is NOT "admin"
        - not authorized to register a new user

    >> if the user IS "admin"
        - register new user
            - loop over the user.txt file to validate that the user_name and pass_word
              does not already exist.
            -  should the user_name and pass_word not be in the user.txt file,
              write and append the input data to the user.txt file on a new line

- If menu == "a       - Adding a Task"
    >> create lists to append the input data for each section of the task requirements
        - request user input for the following data:
            - Task Name             :
            - Task is assigned to   :
            - Date assigned         :
            - Due date              :
            - Task complete (Yes/No):
            - Task description      :
        - write and append data on a new line to the tasks.txt file

- If menu == "va      - View all Tasks"
    >> open the tasks.txt file in read-only mode
        - display all the tasks in numeric order in the following format:

            1. Task            : Assign initial tasks
               Assigned to     : admin
               Date assigned   : 2019-10-10
               Due date        : 2019-10-25
               Task Complete   : No
               Task description: Use taskManager.py to assign each team member with appropriate tasks

- If menu == "vm      - View my Task"
    >> open the tasks.txt file in read-only mode
        - loop over the file to verify if the user_name that is logged in
            - if the logged-in user_name is in the tasks.txt file
                > display all Tasks assigned to that user_name in numeric order in the file
            -- Allow the user to make the following changes:

                1.  Reassign the Task to a new user?
                2.  Edit the due date?
                3.  Mark the Task as complete?
                4.  Edit the Task description?

            - if the logged-in user_name is NOT in the tasks.txt file
                > display "You have no tasks or no additional tasks assigned to you."

- If menu == "ds - display statistics"
    >> read from the task_overview.txt file in read-only mode
        - read the lines on the task_overview.txt file
        - display statistics from task_overview.txt
            1. Total number of Tasks
            2. Completed Tasks
            3. Incomplete Tasks
            4. Overdue Tasks
            5. Percentage of Incomplete and Overdue Tasks respectively

    >> open the user_overview.txt file in read-only mode
        - read the lines on the user.txt file
        - display statistics from user_overview.txt
            1. Total number of Users
            2. Total number of Tasks

        - For each user:
            1. Username and number of tasks assigned
            2. Percentage of Tasks completed
            3. Percentage of Tasks incomplete
            4. Percentage of tasks incomplete and overdue

- If menu == "gr - display statistics"
    >>  ● When the user chooses to generate reports, two text files, called task_overview.txt
          and user_overview.txt, should be generated. Both these text files should output data
          in a user-friendly, easy to read manner.

        o task_overview.txt should contain:

            ▪ The total number of tasks that have been generated and
              tracked using the task_manager.py.
            ▪ The total number of completed tasks.
            ▪ The total number of uncompleted tasks.
            ▪ The total number of tasks that haven’t been completed and that are overdue.
            ▪ The percentage of tasks that are incomplete.
            ▪ The percentage of tasks that are overdue.

        o user_overview.txt should contain:

            ▪ The total number of users registered with task_manager.py.
            ▪ The total number of tasks that have been generated and tracked using task_manager.py.
            ▪ For each user also describe:
            ▪ The total number of tasks assigned to that user.
            ▪ The percentage of the total number of tasks that have been assigned to that user
            ▪ The percentage of the tasks assigned to that user that have been completed
            ▪ The percentage of the tasks assigned to that user that must still be completed
            ▪ The percentage of the tasks assigned to that user that have not yet been completed and are overdue

- If menu == "e - Exit"
    >> exit the infinite loop

- if the user makes an invalid entry:
    print("You have made a wrong choice, Please Try again")
    the menu will loop back again.
"""

# ============== Importing Libraries ============= #
import datetime  # import datetime module to format the dates

# defining functions for:
# o reg_user    — that is called when the user selects ‘r’ to register a user.
# o add_task    — that is called when a user selects ‘a’ to add a new task.
# o view_all    — that is called when users type ‘va’ to view all the tasks
#                 listed in ‘tasks.txt’.
# o view_mine   — that is called when users type ‘vm’ to view all the
#                 tasks that have been assigned to them.


def reg_user(new_user_name, new_pass_word):
    if new_user_name != usernames and new_pass_word != passwords:
        file = open("user.txt", "a")
        file.write(f"\n{new_user_name}, {new_pass_word}")
        file.close()


def add_task(_assign, _task, _t_desc, _date_assign, _due_date, _t_comp):
    task = []
    assigned_to = []
    date_assigned = []
    due_date = []
    task_complete = []
    task_description = []

    with open("tasks.txt", "r") as task_f:
        for lines in task_f:
            temp = lines.strip()
            temp = temp.split(", ")

            task.append(temp[1])
            assigned_to.append(temp[0])
            date_assigned.append(temp[3])
            due_date.append(temp[4])
            task_complete.append(temp[5])
            task_description.append(temp[2])
    task_f = open("tasks.txt", "a")
    task_f.write(f"\n{_assign}, {_task}, {_t_desc}, {_date_assign}, {_due_date}, {_t_comp}")


def view_all():
    file = open("tasks.txt", "r")
    lines = file.readlines()
    for i, line in enumerate(lines):
        temp = line.strip()
        temp = temp.split(", ")

        print(f"""
{i + 1}.\tTask            : {temp[1]}
    Assigned to     : {temp[0]}
    Date assigned   : {temp[3]}
    Due date        : {temp[4]}
    Task Complete   : {temp[5]}
    Task description: {temp[2]}""")

    file.close()


def view_mine(user_name):
    file = open("tasks.txt", "r")
    lines = file.readlines()
    for i, line in enumerate(lines):
        temp = line.strip()
        temp = temp.split(", ")
        while user_name in temp[0]:
            print(f"""
{i + 1}.\tTask            : {temp[1]}
    Assigned to     : {temp[0]}
    Date assigned   : {temp[3]}
    Due date        : {temp[4]}
    Task Complete   : {temp[5]}
    Task description: {temp[2]}
""")

            if user_name != temp[0]:
                print("\nYou have no tasks or any additional tasks assigned to you.")
            break
    file.close()


# ================= Login Section ================ #
print("\n# ================= Login Section ================ #")
# created a dictionary for the usernames and passwords to link to each other
users = {}

# opened user.txt file as a dictionary with key:value pairs
with open("user.txt", "r") as file:
    for lines in file:
        (keys, values) = lines.split()
        keys = keys.replace(",", "")
        users[keys] = values

# created a while true loop, for the input data to validate the user credentials over the dictionary
while True:
    user_name = input("\nPlease enter your username: ")
    pass_word = input("Please enter your password: ")

    if user_name in users.keys() and pass_word == users[user_name]:
        print(f"\nThank you and Welcome, {user_name}!")

    elif user_name and pass_word != users.items():
        print("\nYour username and/or password is incorrect. Please try again.")
        continue
    break

# ================= Menu Section ================= #
# creating an infinite loop so that the user comes back to the menu section repeatedly
# after a selection has been executed
while True:  # presenting the menu to the user
    # if the user is NOT "admin" the standard option will be generated
    if user_name != "admin" and pass_word != "adm1n":
        menu = input('''\n# ================= Menu Section ================= #

Select one of the following Options below:

r       - Registering a User
a       - Adding a Task
va      - View all Tasks
vm      - View my Task
e       - Exit

Option  : ''').lower()  # making sure that the user input is converted to lower case.
    else:  # if the user IS "admin" the customised option will be generated
        menu = input('''\n# ================= Menu Section ================= #

Select one of the following Options below:

r       - Registering a User
a       - Adding a Task
va      - View all Tasks
vm      - View my Task
ds      - Display Statistics
gr      - Generate Reports
e       - Exit

Option  : ''').lower()  # making sure that the user input is converted to lower case.

    # =============== Registering a new user =============== #
    # if the logged-in user is not "admin", they are unable to add a new user
    if user_name != "admin" and pass_word != "adm1n" and menu == "r":
        print("\n# ============ Registering a New User ============ #")
        print(f"\nUnfortunately {user_name}, you are not authorized to register a new user.")

    # if the logged-in user is "admin", they authorized to add a new user
    elif user_name == "admin" and pass_word == "adm1n" and menu == "r":
        print("\n# ============ Registering a New User ============ #")
        # lists to loop over in the user.txt file
        usernames = []
        passwords = []

        with open("user.txt", "r") as file:
            for lines in file:
                temp = lines.strip()
                temp = temp.split(", ")

                usernames.append(temp[0])
                passwords.append(temp[1])

        while True:  # validating user input
            new_user_name = input("\nPlease enter the new username    : ")
            new_pass_word = input("Please enter the new password    : ")
            confirm_password = input("Please confirm the new password  : ")

            if new_user_name in usernames:
                print("\n*** This username already exists! ***")

            elif new_pass_word in passwords:
                print("\n*** This password already exists! ***")

            elif new_pass_word == confirm_password:
                print("\nThe passwords match")
                reg_user(new_user_name, new_pass_word)  # calling reg_user function to write to the file
                print("\nThank you! The new user credentials have been added to the 'user.txt' file.")
                break
            else:
                print("\n*** The passwords do not match! ***")

    # =============== Adding a new Task =============== #
    elif menu == 'a':
        print("\n# ============== Adding a new Task =============== #")
        # user to input Task details to be added
        _task = input("\nTask Name                                    : ").capitalize()
        _assign = input("Task is assigned to                          : ")
        _date_assign = datetime.date.today()
        due_date_entry = input("Enter the due date in this format dd-mm-yyyy : ")
        year, month, day = map(int, due_date_entry.split('-'))
        _due_date = datetime.date(day, month, year)
        _t_comp = input("Task complete (Yes/No)                       : ").capitalize()
        if _t_comp == "Y".capitalize():
            _t_comp = "Yes"
        elif _t_comp == "N".capitalize():
            _t_comp = "No"
        _t_desc = input("Task description                             : ").capitalize()

        # calling add_task function to write the Task to the task.txt file
        add_task(_assign, _task, _t_desc, _date_assign, _due_date, _t_comp)
        print("\nThank you! The new Task has been added to the 'task.txt' file.")

    # =============== Viewing All Tasks =============== #
    elif menu == 'va':
        print("\n# =============== Viewing All Tasks ============== #")
        # calling view_all() function
        # displays all the Tasks in the tasks.txt file
        view_all()
        print(f"\nThank you, {user_name}! These are all the current Tasks in the 'tasks.txt file.")

    # =============== Viewing My Tasks =============== #

    elif menu == 'vm':
        print("\n# =============== Viewing My Tasks =============== #")
        # displaying all the tasks assigned to the user in a number format (enumerate)
        # the user can select a Task number and make changes to it
        while True:
            print(f"\nThese are all your Tasks, {user_name}!")
            view_mine(user_name)
            choice = int(input("Enter the task number you would like to edit or -1 to return to the main menu: "))
            if choice > 0:
                task_number = choice - 1
                print(f"""\nWhat would you like to do?
    1.  Reassign the Task to a new user?
    2.  Edit the due date?
    3.  Mark the Task as complete?
    4.  Edit the Task description?""")

                option = int(input("\nEnter your option here: "))
                # user can reassign the task to another user
                if option == 1:
                    new_user = input("Enter the new user that this Task needs to be reassigned to: ")
                    with open("tasks.txt", "r") as f:
                        reassign = f.readlines()
                        reassign[task_number] = reassign[task_number].replace(user_name, new_user)
                    with open("tasks.txt", "w") as f:
                        f.writelines(reassign)

                # user can change the due date
                elif option == 2:
                    new_due_date = input("\nEnter the new due date: ")
                    with open("tasks.txt", "r") as f:
                        date = f.readlines()
                        for lines in date[task_number]:
                            temp = date[task_number].strip()
                            temp = temp.split(", ")
                            date[task_number] = date[task_number].replace(temp[4], new_due_date)
                    with open("tasks.txt", "w") as f:
                        f.writelines(date)

                # user can mark the task as complete
                elif option == 3:
                    task_status = input("Do you want to mark this task as complete? Yes/No: ").capitalize()
                    if task_status == "y".capitalize():
                        task_status = "Yes".capitalize()
                        with open("tasks.txt", "r") as f:
                            status = f.readlines()
                            status[task_number] = status[task_number].replace("No", "Yes")
                        with open("tasks.txt", "w") as f:
                            f.writelines(status)
                            print("\nYour task is now complete.")
                    elif task_status != "Yes".capitalize():
                        print("\nYour task will remain incomplete.")

                # user can edit the task description
                elif option == 4:
                    task_description = input("\nEnter the edited task description: : ")
                    with open("tasks.txt", "r") as f:
                        task = f.readlines()
                        for lines in task[task_number]:
                            temp = task[task_number].strip()
                            temp = temp.split(", ")
                            task[task_number] = task[task_number].replace(temp[2], task_description)
                    with open("tasks.txt", "w") as f:
                        f.writelines(task)

                else:
                    print("\n*** You have made an invalid selection ***")

            elif choice == -1:
                print("\nThank you :)")
                break

    # =============== Display Statistics ============== #
    elif menu == 'ds':
        print("\n# ============== Display Statistics ============== #")

        # displays the report of tasks in the task_overview.txt file
        tasks_file = open("task_overview.txt", "r")
        file_lines = tasks_file.readlines()
        for line in file_lines:
            temp = line.strip()
            temp = temp.split(", ")
            print(temp[0])
        tasks_file.close()

        # displays the report of users listed in the user_overview.txt file
        users_file = open("user_overview.txt", "r")
        users_file_lines = users_file.readlines()
        for line in users_file_lines:
            temp = line.strip()
            temp = temp.split(", ")
            print(temp[0])
        users_file.close()

    # =============== Generating Reports ============== #
    elif menu == 'gr':
        print("\n# ============== Generating Reports ============== #")
        print(f"""\n*** Your reports have been generated.

*** Please check the task_overview.txt and user.overview.txt files, thank you!""")

    # ================= Task Overview ================= #
        # ▪ The total number of tasks that have been generated and tracked using the task_manager.py.
        with open("tasks.txt", "r") as tasks_file:
            number_of_tasks = tasks_file.readlines()
            number_of_tasks = f"""
                 Task Overview                 
_______________________________________________
The total number of Tasks are : {len(number_of_tasks)}\n"""
        with open("task_overview.txt", "w") as f:
            f.writelines(number_of_tasks)

        # ▪ The total number of completed tasks
        # ▪ The total number of uncompleted tasks.
        count_yes = 0
        word_yes = "Yes"
        count_no = 0
        word_no = "No"

        # date formatting, to calculate the overdue tasks
        today = datetime.datetime.today()
        year = today.strftime("%Y")
        month = today.strftime("%m")
        day = today.strftime("%d")
        formatted_date = year + "-" + month + "-" + day

        with open("tasks.txt", "r") as f:
            for line in f:
                words = line.split()
                for i in words:
                    if i == word_yes:
                        count_yes += 1
                for j in words:
                    if j == "No":
                        count_no += 1
        with open("task_overview.txt", "a") as f:
            f.writelines(f"""\nCompleted tasks  : {count_yes}
Incomplete tasks : {count_no}\n""")

        # ▪ The total number of tasks that haven’t been completed and that are overdue.
        tasks_overdue_count = 0

        with open("tasks.txt", "r") as f:
            for line in f.readlines():
                temp = line.strip()
                temp = temp.split(", ")
                if temp[5] == word_no and temp[4] < formatted_date:
                    tasks_overdue_count += 1
        with open("task_overview.txt", "a") as f:
            f.writelines(f"""Overdue tasks    : {tasks_overdue_count}\n""")

        # ▪ The percentage of tasks that are incomplete.
        # ▪ The percentage of tasks that are overdue.
        with open("tasks.txt", "r") as tasks_file:
            number_of_tasks = tasks_file.readlines()
            number_of_tasks = len(number_of_tasks)
        with open("task_overview.txt", "a") as f:
            f.writelines(f"""
   Percentage of Incomplete and Overdue Tasks
_______________________________________________
Incomplete Tasks : {round(count_no / number_of_tasks * 100, 1)}%
Overdue Tasks    : {round(tasks_overdue_count / number_of_tasks * 100, 1)}%\n""")

    # ================= User Overview ================= #
        # ▪ The total number of tasks that have been generated and tracked using the task_manager.py.
        with open("user.txt", "r") as user_file:
            number_of_users = user_file.readlines()
            number_of_users = f"""
                User Overview                 
_______________________________________________
The total number of Users are: {len(number_of_users)}\n"""

        with open("user_overview.txt", "w") as f:
            f.writelines(number_of_users)

        # ▪ The total number of tasks that have been generated and tracked using task_manager.py.
        with open("tasks.txt", "r") as tasks_file:
            number_of_tasks = tasks_file.readlines()
            number_of_tasks = f"The total number of Tasks are: {len(number_of_tasks)}\n"
        with open("user_overview.txt", "a") as f:
            f.writelines(number_of_tasks)

        user_list = []
        # appending the usernames to user_list to iterate through
        with open("user.txt", "r") as f1:
            u_file = f1.readlines()
            for line in u_file:
                temp = line.strip()
                temp = temp.split(", ")
                user_list.append(temp[0])

        task_list = []
        # appending all the tasks in the file as lists within the task_list
        with open("tasks.txt", "r") as f2:
            t_file = f2.readlines()
            for line in t_file:
                temp = line.strip()
                temp = temp.split(", ")
                task_list.append(temp)

        # iterating through the lists and calculating the percentages as follows:
        #  ▪ For each user also describe:
        #     ▪ The total number of tasks assigned to that user.
        #     ▪ The percentage of the total number of tasks that have been assigned to that user
        #     ▪ The percentage of the tasks assigned to that user that have been completed
        #     ▪ The percentage of the tasks assigned to that user that must still be completed
        #     ▪ The percentage of the tasks assigned to that user that have not yet been completed and are overdue

        for user in user_list:
            user_count = 0
            user_task_overdue = 0
            user_count_yes = 0
            user_count_no = 0
            user_yes_percentage = 0
            user_no_percentage = 0
            user_task_overdue_percentage = 0
            for task in task_list:
                if task[0] == user:
                    user_count += 1
                    if task[5] == "Yes":
                        user_count_yes += 1
                        user_yes_percentage = round(user_count_yes / user_count * 100, 1)
                    if task[5] == "No":
                        user_count_no += 1
                        user_no_percentage = round(user_count_no / user_count * 100, 1)
                    if task[5] == "No" and task[4] < formatted_date:
                        user_task_overdue += 1
                        user_task_overdue_percentage = round(user_task_overdue / user_count * 100, 1)
            with open("user_overview.txt", "a") as f5:
                f5.writelines(f"""
User                           : {user}                        
Number of Tasks Assigned       : {user_count}
Percentage of Assigned Tasks   : {round(user_count / len(number_of_tasks) * 100, 1)}%
Percentage of Completed Tasks  : {user_yes_percentage}%
Percentage of Incomplete Tasks : {user_no_percentage}%
Percentage of Overdue Tasks    : {user_task_overdue_percentage}%\n""")

    # =============== Exiting the Menu =============== #
    elif menu == 'e':
        print("\n# =============== Exiting the Menu =============== #")
        # exiting the menu and ending the program
        print(f"\nGoodbye and see you soon, {user_name}!!!")
        exit()

    # ============== Invalid Entries =============== #
    else:
        print("\n# =============== Invalid Entries ================ #")
        print("\nYou have made a wrong choice, Please Try again")

# Thank you, Farinaaz :)
