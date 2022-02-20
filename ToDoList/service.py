from datetime import datetime

status = (
    "pending",
    "in progress",
    "done"
)


def get_title():
    title = input("Write here the task title: ")
    return check_title(title)

def check_title(title):
    if len(title) > 60:
        print("Title must be no longer 60 symbols!")
    elif len(title) == 0:
        print("Title is a required field!")
    else:
        return title

    if repeat_input():
        return get_title()


def get_description():
    return input("Write here the description of your task: ")


def get_priority():
    priority = input("Write here the task priority (from 1 to 10): ")
    if priority == "":
        return 1    # priority = 1 by default
    else:
        return check_priority(priority)

def check_priority(priority):
    try:
        if int(priority) >= 1 and int(priority) <= 10:
            return priority
        else:
            print("Priority must be integer number from 1 to 10!")
    except:
        print("Priority must be integer number from 1 to 10!!")

    if repeat_input():
        return get_priority()


def get_due_date():
    due_date = input("When your task must be complete (dd.mm.yyyy): ")
    return check_due_date(due_date)

def check_due_date(due_date):
    date_format = "%d.%m.%Y"
    try:
        deadline = datetime.strptime(due_date, date_format)
        return deadline
    except:
        print("Error date! Date format must be dd.mm.yyyy!")

    if repeat_input():
        return get_due_date()


def get_task_id(tasks):
    try:
        return tasks[-1].get("id") + 1
    except:
        return 1


def repeat_input():
    usr_answer = input("Do you want to repeat input (Y | N)? ")
    if usr_answer == "y" or usr_answer == "Y":
        return True
    else:
        exit(0)


def input_no_func():
    usr_func = input("Enter function No: ")
    return check_input_no_func(usr_func)

def check_input_no_func(usr_func):
    try:
        if int(usr_func) >= 0 and int(usr_func) <= 5:
            return int(usr_func)
        else:
            print("We have functions from 0 to 5! AHTUNG!")
    except:
        print("Write No of needed function (integer number from 0 to 5!")

    if repeat_input():
        return input_no_func()


def input_task_id():
    task_id = input("Enter task ID")
    return check_input_task_id(task_id)

def check_input_task_id(task_id):
    try:
        if int(task_id):
            return int(task_id)
        else:
            print("Write integer task ID")
    except:
        print("Task ID must be integer number!")

    if repeat_input():
        return input_task_id()