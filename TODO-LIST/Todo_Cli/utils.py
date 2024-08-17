import json

TASK_LISTS_FILE = 'task_lists.json'

def load_lists():
    """Load the task lists from the JSON file"""
    
    try:
        with open(TASK_LISTS_FILE, 'r') as file:
            data = json.load(file)
            if not isinstance(data, dict):
                raise ValueError("Data is not in the expected dictionary format.")
            return data
        
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error loading task lists: {e}")
        return {}
    
    
def save_lists(task_lists):
    """Save the task lists to the JSON file."""
    with open(TASK_LISTS_FILE, 'w') as file:
        json.dump(task_lists, file)