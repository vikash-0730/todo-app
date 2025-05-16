import os
from datetime import date

class TODO:
    title = "TODO"

    def __init__(self, title):
        self.title = title

    def add(self, task):
        today_date = date.today()
        with open(f"{self.title}.txt", "a") as file:
            file.write(f"{task} {today_date}\n")
        print("Task added succesfully")

    def get_tasks(self, filename=None):
        if not filename:
            filename = self.title

        if os.path.exists(f"{filename}.txt"):
            with open(f"{filename}.txt", "r") as file:
                return [task.strip() for task in file.readlines()]
        else:
            print("File does not exist...")
            return []

    def view(self, filename=None):
        """Only displays tasks"""
        tasks = self.get_tasks(filename)
        for index, task_line in enumerate(tasks, start=1):
            parts = task_line.rsplit(" ", 1)
            if len(parts) == 2:
                task, task_date = parts
                print(f"{index}. {task}    {task_date}")
            else:
                print(f"{index}. {task_line}")

    def update(self, idx, taskname, filename=None):
        if not filename:
            filename = self.title

        tasks = self.get_tasks(filename)
        
        # print(tasks)
        if 0 < idx <= len(tasks):
            today_date = date.today()
            tasks[idx-1] = f"{taskname.strip()} {today_date}"
            with open(f"{filename}.txt", "w") as file:
                for task in tasks:
                    file.write(task + "\n")
            print("Task updated successfully.")
        else:
            print("Incorrect index")

    def delete(self,idx,filename=None):
        if not filename:
            filename=self.title
        tasks = self.get_tasks(filename)  # ✅ get tasks from view
        if 0 < idx <= len(tasks):
            removed_task =tasks.pop(idx-1)
            with open(f"{filename}.txt", "w") as file:
                for task in tasks:
                    file.write(task + "\n")
            print(f"Deleted: {removed_task} successfully.")
        else:
            print("Incorrect index")
            
def clear():
     os.system('cls' if os.name=='nt' else 'clear')

v = TODO("vikas")
while True:
    print("a) Add Todo")
    print("b) Update Todo")
    print("c) Delete Todo")
    print("d) View Todo")
    value=input("Enter the option to add/update/delete or enter 'q' to exit: ")
    if value=="a":
        clear()
        taskname=input("Enter the taskname...  ")
        v.add(taskname)
        print("press any key to continue...")
        input()
        clear()
    elif value=="b":
        clear()
        filename=input("Enter the filename or it will be selected default: ")
        v.view(filename)
        index=int(input("Enter the number of task you want to update: "))
        taskname=input("Enter the taskname...  ")
        v.update(index,taskname,filename)
        print("press any key to continue...")
        input()
        clear()
    elif value=="c":
        clear()
        filename=input("Enter the filename or it will be selected default: ")
        v.view(filename)
        index=int(input("Enter the number of task you want to update: "))
        v.delete(index,filename)
        print("press any key to continue...")
        input()
        clear()
    elif value=="d":
        clear()
        filename=input("Enter the filename or it will be selected default: ")
        v.view(filename)
        print("press any key to continue...")
        input()
        clear()
        
    else:
        break
        
    
