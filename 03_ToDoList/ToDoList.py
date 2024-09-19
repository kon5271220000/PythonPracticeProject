def DisplayMenu():
    print("Menu: ")
    print("1. Add Task: ")
    print("2. View Task: ")
    print("3. Mark as Done: ")
    print("4. Exit")

def AddTask(tasks):
    task = input("Enter Task: ")
    tasks.append(task)
    print("task added succesful")

def ViewTask(tasks):
    i = 1
    for task in tasks:
        print(f"{i}-{task}")
        i += 1

def MarkTaskDone(tasks):
    ViewTask(tasks)
    index = int(input("Enter task index to mark it done: ")) - 1


    if 0 <= index < len(tasks):
        remove_task = tasks.pop(index)
        print(f"Task {remove_task} marked as done and remove")
    else:
        print("Invalid index task")

def SaveTask(tasks):
    with open("task.txt", "w") as f:
        for task in tasks:
            f.write(task + '\n')

def LoadTask():
    try:
        with open("task.txt","r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def main():
    tasks = LoadTask()

    while True:
        DisplayMenu()

        choice = input("Enter Your Choice: ").strip()


        if choice == "1":
            AddTask(tasks)
        elif choice == "2":
            ViewTask(tasks)
        elif choice == "3":
            MarkTaskDone(tasks)
        elif choice == "4":
            print("exiting")
            SaveTask(tasks)
            break
        else:
            print("invalid choice")


if __name__ == "__main__":
    main()

