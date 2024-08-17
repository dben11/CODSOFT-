from task_manage import  create_task_list, select_task_list, add_task, view_tasks, update_task, delete_task, delete_task_list, complete_task, show_help


def main():
    """Main function to handle user input. """
    print('Welcom to my Todo-App!')
    
    while True:
        command_line = input('Todo-@@ ').strip().lower()
        
        if command_line == 'help':
            show_help()
            # print("Available commands:\ncreate list\nselect list\ndelete list\nquit")
            
        elif command_line == 'create list':
            list_name = input("Enter list name:").strip()
            create_task_list(list_name)
            
        elif command_line == 'select list':
            list_name = select_task_list()
            
            if list_name:
                while True:
                    sub_command = input(f'{list_name} % ').strip().lower()
                    
                    if sub_command == 'add task':
                        description = input("Enter task description: ").strip()
                        add_task(list_name, description)
                        
                    elif sub_command == 'view task':
                        view_tasks(list_name)
                        
                    elif sub_command == 'update task':
                        task_id = int(input("Enter task ID to update: ").strip())
                        new_description = input("Enter new task description: ").strip()
                        update_task(list_name, task_id, new_description)
                        
                    elif sub_command == 'delete task':
                        task_id = int(input("Enter task ID to delete: ").strip())
                        delete_task(list_name, task_id)
                        
                    elif sub_command == 'complete task':
                        task_id = int(input("Enter task ID to complete: ").strip())
                        complete_task(list_name, task_id)
                        
                    elif sub_command == 'quit':
                        break
                        
                    else:
                        print("Unknown command. Type 'help' for options. ")
                        
        elif command_line == 'delete list':
            list_name = input("Enter list name to delete: ").strip()
            delete_task_list(list_name)
            
        elif command_line == 'quit':
            print("Exiting Application")
            break
        
        else:
            print("Unknown command. Type 'help' for options. ")
            
            
            
            
if __name__ == '__main__':
    main()