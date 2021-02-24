d = {}
# Main program Loop
ch = 0
while ch != 4:

  # Create the drop-down menu
  print("\n1. Add new task\n2. Finished a task\n3. Show all my tasks\n4. Exit")
  ch = int(input("Enter your choice: "))

  if ch == 1:
    # When new task is added...
    task_title = input("Enter the title for your task: ")
    if task_title not in d.keys():
        task_des = input("Enter the description for your task: ")
        d[task_title] = task_des
        change = True
        print("New task added")
        # f.write(task_title + ':' + task_des + '\n')
    else:
        print("Task already exists")

  elif ch == 2:
    # When a task is finished...
    task_title = input("Enter the title of the task that you completed: ")
    if task_title in d.keys():
        del d[task_title]
        change = True
        print("Task removed")
    else:
        print("No such task exists")

  elif ch == 3:
    # Printing the dictionary
    print()
    for key in d:
        print(key, end="\t")

    print()
    for value in d.values():
        print(value, end = "\t")

    print()

  elif ch == 4:
    # Loop over, quit
    print("Task complete")
    break

  else:
      print('Enter a valid number!')

