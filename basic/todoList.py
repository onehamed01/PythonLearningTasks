def display_menu():
    print("\nTo-Do List Manager")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as complete")
    print("4. Exit")

def todo_list_managment():
    display_menu()
    tasks = []
    while True:
        try:
            choice = int(input("Enter the option: "))
            if choice == 1:
                description_input = input("write Description: ")
                tasks.append({'description':description_input, "completed":False})
            elif choice == 2:
                for n, i in enumerate(tasks):
                    status = "Completed" if i['completed'] else "Not Completed"
                    print(f"{n}. {i['description']} - {status}")
            elif choice == 3:
                    try:
                        index_task = int(input('Enter the index of task: '))
                        if 0 <= index_task < len(tasks):
                            tasks[index_task]['completed'] = True
                        else:
                            print('invalid choice! please choose the correct index!')
                    except ValueError:
                        print("invalid Data. add number please")
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print('invalid choice. it should be 1, 2, 3 or 4')
        except ValueError:
            print("invalid data. please Enter the number")

if __name__ == "__main__":
    todo_list_managment()
        

