import json
from datetime import datetime
from utils import load_lists, save_lists


def create_task_list(list_name):
    """ Create a new list """
    task_lists = load_lists()
    
    
    if list_name in task_lists:
        print(f"List '{list_name}' already exists.")
        
    else:
        task_lists[list_name] = []
        save_lists(task_lists)
        print(f"List '{list_name}' created successfully..")
        
        
def select_task_list():
    """Allow the user to select a task list."""
    task_lists = load_lists()
    
    if not task_lists:
        print("No task lists available. ")
        return None
    
    print("Available lists: ")
    for index, list_name in enumerate(task_lists.keys(), start=1):
        print(f"{index}. {list_name}")
        
    choice = input("select a list by number: ").strip()
    
    try:
        list_index = int(choice) - 1
        if 0 <= list_index < len(task_lists):
            return list(task_lists.keys())[list_index]
        else:
            print("Invalid selection.")
            return None
        
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
    
    
def add_task(list_name, description):
    """Add a new task to the selected list."""
    task_lists = load_lists()
    task_id = len(task_lists[list_name]) + 1
    created_at = datetime.now().isoformat()
    task_lists[list_name].append({
        "id": task_id,
        "description": description,
        "completed": False,
        "created_at": created_at,
    })
    save_lists(task_lists)
    print(f"Task added to '{list_name}': ID {task_id}, Discription '{description}'")
    
    
def view_tasks(list_name):
    """View tasks in the selected list. """
    task_lists = load_lists()
    
    if not task_lists.get(list_name):
        print(f"No tasks found in list '{list_name}'.")
        return
    
    for task in task_lists[list_name]:
        status = "Completed" if task["completed"] else "Pending"
        print(f"ID: {task['id']} - {task['description']} [{status}] (created at: {task['created_at']})")
        
def update_task(list_name, task_id, new_description):
    """Update a task's description """
    task_lists = load_lists()
    for task in task_lists[list_name]:
        if task['id'] == task_id:
            task['description'] = new_description
            save_lists(task_lists)
            print(f"Task ID {task_id} updated to: '{new_description}'")
            return
        print(f"Task ID {task_id} not found in list '{list_name}'.")
        
def delete_task(list_name, task_id):
    """Delete a task from the selected list"""
    task_lists = load_lists()
    updated_tasks = [task for task in task_lists[list_name] if task['id'] != task_id]
    task_lists[list_name] = updated_tasks
    save_lists(task_lists)
    print(f"Task ID {task_id} deleted from list '{list_name}'.")
    
def complete_task(list_name, task_id):
    """Mark a task a scompleted. """
    task_lists = load_lists()
    for task in task_lists[list_name]:
        if task['id'] == task_id:
            task['completed'] = True
            save_lists(task_lists)
            print(f"Tank ID {task_id} marked as completed.")
            return
        print(f"Task ID {task_id} not found in list '{list_name}'.")
        

def delete_task_list(list_name):
    """Delete a task list."""
    task_lists = load_lists()
    
    if list_name in task_lists:
        del task_lists[list_name]
        save_lists(task_lists)
        print(f"List '{list_name}' deleted sucessfully")
        print("list is empty")
    else:
        print(f"List '{list_name}' not found.")
        
        
def show_help():
    try:
        with open("help.txt", "r") as file:
            help_content = file.read()
        print(help_content)
    except FileNotFoundError:
        print("Help file not found. Please ensure 'help.txt' is in the application directory.")