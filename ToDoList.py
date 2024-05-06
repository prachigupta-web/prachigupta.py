def print_tasks(task_list):
    task_list.sort(key=lambda x: -int(x[2]))
    for row in task_list:
        print(f"{row}")

def main():
    task_list = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            n_tasks = int(input("How many tasks do you want to add: "))
            for i in range(n_tasks):
                task = input("Enter the task: ")
                task_list.append([task, "Not Done", str(len(task_list) + 1)])
                print("Task added!")

        elif choice == '2':
            print("\nTasks:")
            for row in task_list:
                print(f"{row[2]}. {row[0]} - {row[1]}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(task_list):
                task_list[task_index][1] = "Done"
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif choice == '4':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
