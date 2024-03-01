from PIL import Image

def encrypt_image(image_path, key):
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Convert image to RGB mode
        img = img.convert("RGB")
        
        # Get the size of the image
        width, height = img.size
        
        # Encrypt each pixel
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                img.putpixel((x, y), (r ^ key, g ^ key, b ^ key))
        
        # Save the encrypted image
        img.save("encrypted_image.png")
        print("Image encrypted successfully!")
    except Exception as e:
        print("Error:", e)

def decrypt_image(image_path, key):
    try:
        # Open the encrypted image
        img = Image.open(image_path)
        
        # Convert image to RGB mode
        img = img.convert("RGB")
        
        # Get the size of the image
        width, height = img.size
        
        # Decrypt each pixel
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                img.putpixel((x, y), (r ^ key, g ^ key, b ^ key))
        
        # Save the decrypted image
        img.save("decrypted_image.png")
        print("Image decrypted successfully!")
    except Exception as e:
        print("Error:", e)

def main():
    while True:
        print("\n1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Quit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            image_path = input("Enter the path of the image to encrypt: ")
            key = int(input("Enter the encryption key (an integer): "))
            encrypt_image(image_path, key)
        elif choice == "2":
            image_path = input("Enter the path of the image to decrypt: ")
            key = int(input("Enter the decryption key (an integer): "))
            decrypt_image(image_path, key)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
