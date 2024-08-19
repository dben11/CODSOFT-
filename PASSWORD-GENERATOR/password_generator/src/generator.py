import random
import string
from config import settings

def get_character_pool(include_uppercase, include_lowercase, include_digits, include_special_chars):
    character_pool = ""
    if include_uppercase:
        character_pool += string.ascii_uppercase
        
    if include_lowercase:
        character_pool += string.ascii_lowercase
        
    if include_digits:
        character_pool += string.digits
        
    if include_special_chars:
        character_pool += string.punctuation
    
    return character_pool


def generate_password(length= settings.DEFAULT_LENGTH,
                 include_uppercase=settings.INCLUDE_UPPERCASE,
                 include_lowercase=settings.INCLUDE_LOWERCASE,
                 include_digits=settings.INCLUDE_DIGITS,
                 include_special_chars=settings.INCLUDE_SPECIAL_CHARS):
    character_pool = get_character_pool(include_uppercase, include_lowercase, include_digits, include_special_chars)
    if not character_pool:
        raise ValueError("No character types selected. password cannot be generated.")
    return ''.join(random.choice(character_pool) for _ in range(length))
    