from sys import exit
def add_task():
    while True:
        task = input("What task you want to add? ('exit' to exit) ")
        if task == "exit":
            exit1(1)
            break
        print(f"'Задача {task.lower()} записана'")
        tasks_list.append(task+"\n")

def task_list():
    for i, task in enumerate(tasks_list):
        print(f"{i+1}. {task.strip()}")
    input("Press any key to continue...")

def task_list2():
    for i, task in enumerate(tasks_list):
        print(f"{i+1}. {task.strip()}")

def done_task():
    while True:
        task_list2()
        try:
            list_done=input("What task you've done? ('exit' to exit) )")
            if list_done == "exit":
                exit1(1)
            else:
                tasks_list[int(list_done) - 1] = tasks_list[int(list_done) - 1].strip()
                tasks_list[int(list_done) - 1] = tasks_list[int(list_done) - 1] + " ✅\n"
                break
        except IndexError:
            print("-" * 15)
            print("You chose the wrong answer. Please enter right choice")
            print("-" * 15)
            continue
        except ValueError:
            print("-" * 15)
            print("You chose the wrong answer. Please enter right choice")
            print("-" * 15)
            continue

def save_in_file():
    with open("list.txt", "w", encoding="utf-8") as f:
        for i in tasks_list:
            f.write(i)

def del_task():
    task_list2()
    task = input("What task you want to remove? ")
    tasks_list.pop(int(task)-1)

def exit1(typo):
    if typo == 1:
        main()
    else:
        exit()


def main():
    with open("list.txt", "r+", encoding="utf-8") as f:
        global tasks_list
        tasks_list = f.readlines()
    while True:
        action = input(
        """----------
1. Add task
2. Remove task
3. Task list
4. Done task
5. Save tasks
6. Exit
Enter your choice: """)
        if action == "1":
            add_task()
        elif action == "2":
            del_task()
        elif action == "3":
            task_list()
        elif action == "4":
            done_task()
        elif action == "5":
            save_in_file()
        elif action == "6":
            exit1(0)
        else:
            print("Please enter right choice")
            continue

if __name__ == "__main__":
    main()


