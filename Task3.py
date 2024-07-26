import random
import string

def generate_password(length):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")

    # Prompt the user to specify the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
