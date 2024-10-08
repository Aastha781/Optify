import random
import string

def generate_password(length: int, use_letters: bool, use_numbers: bool, use_symbols: bool) -> str:
    """Generates a random password based on user-defined criteria."""
    
    # Build the character set based on user preferences
    character_set = ''
    
    if use_letters:
        character_set += string.ascii_letters  # Includes both uppercase and lowercase letters
    if use_numbers:
        character_set += string.digits  # Includes digits (0-9)
    if use_symbols:
        character_set += string.punctuation  # Includes symbols (e.g., !@#$%^&*)
    
    if not character_set:
        raise ValueError("You must select at least one type of character to generate the password.")
    
    # Generate the password by randomly choosing characters from the selected set
    password = ''.join(random.choice(character_set) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Command Line Password Generator!")
    
    # Get user input for password length
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
    except ValueError:
        print("Invalid input! Please enter a positive integer for the password length.")
        return

    # Get user preferences for character types
    use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    # Ensure at least one character type is selected
    if not any([use_letters, use_numbers, use_symbols]):
        print("You must select at least one character type (letters, numbers, or symbols).")
        return
    
    # Generate the password based on user preferences
    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Your generated password is: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
