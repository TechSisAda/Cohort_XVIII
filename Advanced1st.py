run_again = True
tasks = []


while run_again:
    print("WELCOME TO THE TODO LIST MANAGEER 📜📜")
    print("How may I help you today? ")
    print(
        """

    1. Add Task
    2. Remove Task
    3. View Task
    4. Exit

        """
        )
    
    user_choice = input("Select an option [1 - 4]: ")
    user_choice = int(user_choice)
   
    if user_choice == 1:
        new_task = input("Enter new tasks: ")
        tasks.append(new_task)
        print(new_task, "has been added successfully.")

    elif user_choice ==2:
        for task in tasks:
            print(task)
        remove_task = int(input("What the number of task you would like to remove?: "))
        task_to_remove = tasks.pop(remove_task - 1)
        print(task_to_remove, "has been removed\n")
    
    elif user_choice == 3:
        if len(tasks) > 0:
            print("\n Your tasks are: ")
            for task in tasks:
                print(task)
            print()
    
        else: 
            print("You have no tasks to view \n")
    elif user_choice == 4:
        run_again = False

    else:
        print("Invalid Input entered. Try again \n")

        




    run_again = user_choice != 5