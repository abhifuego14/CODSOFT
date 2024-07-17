import random
import string

def generate_password(length):
    # Define the character sets
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    print("---------------------------------")
     
    try:
        # Prompt the user to specify the length of the password
        length = int(input("Enter the length of the password: "))
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Generated Password: {password}")
    
    except ValueError:
        print("Error: Please enter a valid integer for password length.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
