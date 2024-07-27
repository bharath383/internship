
import random
import string

def generate_password(pwlength):
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    passwords = []

    for length in pwlength:
        password = ''.join(random.choice(alphabet) for _ in range(length))
        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)
        passwords.append(password)
    
    return passwords

def replace_with_number(password):
    num_replacements = random.randint(1, 3)
    for _ in range(num_replacements):
        replace_index = random.randrange(len(password))
        password = password[:replace_index] + str(random.randrange(10)) + password[replace_index + 1:]
    return password

def replace_with_uppercase_letter(password):
    num_replacements = random.randint(1, 3)
    for _ in range(num_replacements):
        replace_index = random.randrange(len(password))
        password = password[:replace_index] + password[replace_index].upper() + password[replace_index + 1:]
    return password

def get_valid_input(prompt, min_value=3):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                print(f"Value should be at least {min_value}. Setting to {min_value}.")
                return min_value
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    num_passwords = get_valid_input("How many passwords do you want to generate? ", min_value=1)
    print(f"Generating {num_passwords} passwords")

    password_lengths = []
    for i in range(num_passwords):
        length = get_valid_input(f"Enter the length of Password #{i + 1} (minimum length is 3): ")
        password_lengths.append(length)

    passwords = generate_password(password_lengths)
    for i, password in enumerate(passwords, start=1):
        print(f"Password #{i} = {password}")

if __name__ == "__main__":
    main()
