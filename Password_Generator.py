import random
import string

def generate_password(length, complexity):
    """Generates a random password of the specified length and complexity.

    Args:
        length: The desired length of the password.
        complexity: The desired complexity level (1-3).

    Returns:
        A string representing the generated password.
    """

    if complexity == 1:
        char_set = string.ascii_letters
    elif complexity == 2:
        char_set = string.ascii_letters + string.digits
    elif complexity == 3:
        char_set = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level. Please choose 1, 2, or 3.")

    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                raise ValueError("Password length must be positive.")
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    while True:
        try:
            complexity = int(input("Enter the desired complexity level (1-3): "))
            if complexity not in (1, 2, 3):
                raise ValueError("Invalid complexity level. Please choose 1, 2, or 3.")
            break
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")

    password = generate_password(length, complexity)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()