# PASSWORD GENERATOR
import random
import string

def generate_password(length):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Password Generator")

    # Prompt the user for the desired length of the password
    while True:
        try:
            password_length = int(input("Enter the desired length of the password: "))
            if password_length > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

    # Generate and display the password
    generated_password = generate_password(password_length)
    print("\nGenerated Password: {}".format(generated_password))

if __name__ == "__main__":
    main()
