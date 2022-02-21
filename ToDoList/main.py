import service

tasks = []

def end_work():
    print("Good bye!")
    exit(0)

def create_new_task():
    id = service.get_task_id(tasks)

    new_task = {
        "id": id,
        "title": service.get_title(),
        "descr": service.get_description(),
        "status": service.status[0],
        "priority": service.get_priority(),
        "due_date": service.get_due_date()
    }

    tasks.append(new_task)
    print(f"New task created successfully! ID = {id}", end="\n\n")

def view_tasks_list():
    print(tasks)

def view_task():
    task_id = service.input_task_id()
    try:
        print(tasks[task_id])
    except IndexError:
        print(f"There is no task with ID {task_id}", end="\n\n")

def edit_task():
    pass

def delete_task():
    task_id = service.input_task_id()
    try:
        tasks.pop(task_id - 1)
        print(f"Task with ID = {task_id} was deleted", end="\n\n")
    except IndexError:
        print(f"There is no task with ID {task_id}", end="\n\n")

###########################################################
if __name__ == "__main__":
    print("""
Here are the functions of this program:
    0. End work
    1. Create new task
    2. View tasks list
    3. View task detail
    4. Edit task
    5. Delete task
    """)

    while True:
        usr_func = service.input_no_func()
        if usr_func == 0:
            end_work()
        elif usr_func == 1:
            create_new_task()
        elif usr_func == 2:
            view_tasks_list()
        elif usr_func == 3:
            view_task()
        elif usr_func == 4:
            edit_task()
        elif usr_func == 5:
            delete_task()
