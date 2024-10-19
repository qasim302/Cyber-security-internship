# Function to encrypt the message using Caesar Cipher
def encrypt(text, shift):
    result = ""
    
    # Traverse each character in the text
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep the character as is (spaces, punctuation, etc.)
        else:
            result += char
    
    return result

# Function to decrypt the message using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)

# Main program logic
def main():
    print("-"*50)
    print("Welcome to Nagra Caesar Cipher Program")
    print("-"*50)
    
    # Get user input for the message and shift value
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (a number): "))
    
    # Ask the user if they want to encrypt or decrypt
    choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()
    
    if choice == 'E':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'D':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice! Please type 'E' for Encrypt or 'D' for Decrypt.")

# Run the program
if __name__ == "__main__":
    main()
