import unittest
import string
from src.generator import generate_password


class TestPasswordGenerator(unittest.TestCase):
    
    def test_generate_password_length(self):
        length = 16
        password = generate_password(length=length)
        self.assertEqual(len(password), length)
        
    def test_generate_password_character(self):
        length = 16
        password = generate_password(length=length)
        valid_characters = set(string.ascii_letters + string.digits + string.punctuation)
        self.assertTrue(all(char in valid_characters for char in password))
        
        
    def test_generate_password_no_characters(self):
        with self.assertRaises(ValueError) as context:
            generate_password(
                include_uppercase=False,
                include_lowercase=False,
                include_digits=False,
                include_special_chars=False
            )
            
            sefl.asserEqual(str(contex.exception), "No character types selected. Password cannto be generated..")
            


if __name__ == "__main__":
    main()
        

