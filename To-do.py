def show_menu():
    print("__________---YOUR ALL CHOICE---__________")
    print()
    print("1. -- (Add a task )")
    print("2. --(Remove a task )")
    print("3. --(View all task )")
    print("4. --(Exit ) ")

def add_task(tasks):
    task = input("Enter a task: ").strip().lower()
    tasks.append(task)
    print(f"--'{task.upper()}'-- has been added!")

def remove_task(tasks):
    task = input("Enter a task for remove: ").strip()
    if task in tasks:
        tasks.remove(task)
        print(f"'\n --'{task}'-- has been removed!")
    else:
        print(f"{task} not found!")
        
def view_task(tasks):
    if tasks:
        print("YOUR ALL TASKS !")
        for i, task in enumerate(tasks, 1):
            print(f"{i}.{task}")
    else:
        print("NO TASK'S FOUND!")

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option \n: ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            view_task(tasks)
        elif choice == "4":
            print("Good Bye !")
            break
        else:
            print("invalid choice!\nChoose Number Between 1 and 4")

if __name__ == "__main__":
    main()
