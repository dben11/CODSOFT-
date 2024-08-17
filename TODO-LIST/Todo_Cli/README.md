# 1. Project Overview

    - Title: To-Do List CLI Application
    - Description: A command-line interface(CLI) App for managing the following
            - add, update, view and delete tasks
    - Goals
        - Implement a user-friendly CLI for task management.
        - Implementation of basic CRUD operations

# 2. Project Setup

    - Requirements:
        Python3.x
        External libraries(e.g 'argparse' for command-line arguments, 'json' for data storage)

# 3. Features
    Todo-List CLI Application - Help Guide
=======================================

Available Commands:
-------------------

1. create list
   - Creates a new task list.
   - Usage: `create list`
   - Example: `create list`
   - The user will be prompted to enter a name for the new list.

2. select list
   - Selects an existing task list for adding, viewing, or modifying tasks.
   - Usage: `select list`
   - Example: `select list`
   - The user will be prompted to choose from available lists.

3. delete list
   - Deletes an existing task list and all its associated tasks.
   - Usage: `delete list`
   - Example: `delete list`
   - The user will be prompted to enter the name of the list to delete.

4. add task
   - Adds a new task to the selected task list.
   - Usage: `add task`
   - Example: `add task`
   - The user will be prompted to enter a description for the task.

5. view task
   - Views all tasks in the selected task list.
   - Usage: `view task`
   - Example: `view task`

6. delete task <task_id>
   - Deletes a specific task from the selected task list.
   - Usage: `delete task <task_id>`
   - Example: `delete task 1`

7. update task <task_id>
   - Updates the description of a specific task in the selected task list.
   - Usage: `update task <task_id>`
   - Example: `update task 1`

8. complete task <task_id>
   - Marks a specific task in the selected task list as complete.
   - Usage: `complete task <task_id>`
   - Example: `complete task 1`

9. help
   - Displays this help guide.
   - Usage: `help`

10. clear
    - Clears the screen.
    - Usage: `clear`

11. quit
    - Exits the application.
    - Usage: `quit`


# 4. Implementation Details

  ├── __pycache__
│   ├── task_manage.cpython-310.pyc
│   └── utils.cpython-310.pyc
├── README.md
├── task_lists.json
├── task_manage.py
├── tasks.json
├── todo.py
└── utils.py

    . Imports
        import argparse
        import json
        import os

    Functions:
        . load_tasks()': Load task from 'task.json file'
        . save_tasks(tasks): 'Saves tasks to 'tasks.json'
        . add_task(Description): Add a new task
        . view_task(): Displays all tasks
        . update_task(task_id, new_description): Update an existing task
        . deleteelete a task
        . complete_task(task_id): Mark a task as completedelete task
        . complete <task_id>: Mark a task as completed

# 7. Documentation

    . README.md:
        . Project overview
        . Installation
        . Usage Instruction
        . Example commands and outputs

# 8. Additional Conciderations

    . Error Handling:
     . Hadle invlaid commands or missing arguments
    Data Backup:
    . Implement a mechanism to backup or exports tasks
