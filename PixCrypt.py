from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    """
    Encrypts an image using a pixel-wise XOR operation with a key.
    
    :param image_path: Path to the input image.
    :param key: Encryption key (integer).
    :param output_path: Path to save the encrypted image.
    """
    # Load the image
    img = Image.open(image_path)
    img_array = np.array(img)  # Convert to a NumPy array
    
    # Perform XOR operation on each pixel
    encrypted_array = img_array ^ key
    
    # Convert back to an image and save
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Encrypted image saved to: {output_path}")


def decrypt_image(image_path, key, output_path):
    """
    Decrypts an image by reversing the XOR operation with the key.
    
    :param image_path: Path to the encrypted image.
    :param key: Decryption key (same as the encryption key).
    :param output_path: Path to save the decrypted image.
    """
    # Load the image
    img = Image.open(image_path)
    img_array = np.array(img)  # Convert to a NumPy array
    
    # Reverse the XOR operation
    decrypted_array = img_array ^ key
    
    # Convert back to an image and save
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(output_path)
    print(f"Decrypted image saved to: {output_path}")


# User Interaction
def main():
    print("Image Encryption Tool")
    choice = input("Do you want to 'encrypt' or 'decrypt' an image? ").strip().lower()
    
    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice. Please choose 'encrypt' or 'decrypt'.")
        return
    
    image_path = input("Enter the path to the image: ").strip()
    key = int(input("Enter a numeric key (integer): "))
    output_path = input("Enter the path to save the output image: ").strip()
    
    if choice == 'encrypt':
        encrypt_image(image_path, key, output_path)
    else:
        decrypt_image(image_path, key, output_path)


if __name__ == "__main__":
    main()
