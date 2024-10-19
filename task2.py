from PIL import Image
import random


# Function to encrypt the image by manipulating pixels
def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()  # Load the pixel data

    # Get image dimensions
    width, height = img.size

    # Apply encryption by adding the key to each pixel's RGB values
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Encrypt each channel by adding the key and using modulo to keep it in range (0-255)
            pixels[x, y] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)

    # Optional: Randomly swap pixels
    for _ in range(1000):  # 1000 random swaps for encryption
        x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
        x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
        # Swap the pixel values
        pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]

    # Save the encrypted image
    encrypted_image_path = "my1_encrypt.png"
    img.save(encrypted_image_path)
    print(f"Encrypted image saved as {encrypted_image_path}")


# Function to decrypt the image by reversing pixel manipulation
def decrypt_image(image_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    pixels = img.load()

    # Get image dimensions
    width, height = img.size

    # Optional: Reverse the pixel swaps (assuming we know the swap pattern or have the reverse process)
    for _ in range(1000):  # Reverse 1000 swaps (for demo purposes)
        x1, y1 = random.randint(0, width - 1), random.randint(0, height - 1)
        x2, y2 = random.randint(0, width - 1), random.randint(0, height - 1)
        # Swap the pixel values back
        pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]

    # Decrypt by subtracting the key from each pixel's RGB values
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Decrypt each channel by subtracting the key and using modulo to keep it in range (0-255)
            pixels[x, y] = ((r - key) % 256, (g - key) % 256, (b - key) % 256)

    # Save the decrypted image
    decrypted_image_path = "my1_decrypt.png"
    img.save(decrypted_image_path)
    print(f"Decrypted image saved as {decrypted_image_path}")


# Main function to execute the program
def main():
    print("-" * 50)
    print("Welcome to Nagra Image Encryption Tool")
    print("-" * 50)

    # Get user choice to encrypt or decrypt
    choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()

    # Get the image file path
    image_path = input("Enter the image file path: ")

    # Get the key (an integer value for the pixel manipulation)
    key = int(input("Enter the encryption/decryption key (a number): "))

    if choice == 'E':
        encrypt_image(image_path, key)
    elif choice == 'D':
        decrypt_image(image_path, key)
    else:
        print("Invalid choice! Please type 'E' for Encrypt or 'D' for Decrypt.")


# Run the main function
if __name__ == "__main__":
    main()
