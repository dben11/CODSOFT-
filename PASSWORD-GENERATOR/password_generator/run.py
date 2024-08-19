from src.generator import generate_password

def get_valid_integer(prompt):
    """Prompt user for valid interger input"""
    
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("The length must be a positive integer.")
            return value
        except ValueError as e:
            print(f"Ivalid entry: {e}. please enter a valid integer.")
            
def get_boolean_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ('y', 'n'):
            return response == 'y'
        print("Invalid input. please enter 'y' or 'n'.. ")
        
        
def main():
    """Prompt user for password length and character options, then display password"""
    length = get_valid_integer("Enter the desired password length (getpwd)$$: ")
    include_uppercase = get_boolean_input("Include uppercase letters? (y/n)$ ")
    include_lowercase = get_boolean_input("Include lowercase letters? (y/n)$ ")
    include_digits = get_boolean_input("Include digits? (y/n)$ ")
    include_special_chars = get_boolean_input("Include special characters? (y/n)$ ")
    
    if not (include_uppercase or include_lowercase or include_digits or include_special_chars):
        print("Notification: At least a character must be selected..")
    print("Try again!")
    return
    
    try:
        password = generate_password(
            length = length,
            include_uppercase = include_uppercase,
            include_lowercase = include_lowercase,
            include_digits = include_digits,
            include_special_chars = include_special_chars
        )
        print("Password generated sucessfuly:", password)
        
    except ValueError as e:
        print(f"Error: {e}")
    
    
if __name__ == "__main__":
    main()
        