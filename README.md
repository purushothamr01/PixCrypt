# PixCrypt
PixCrypt is a simple image encryption and decryption tool using pixel manipulation. Encrypt images by applying XOR operations with a custom key, ensuring reversible transformations. Supports popular formats like PNG and JPEG. Easy-to-use, key-based security for protecting visual data. Perfect for learning image encryption basics!

How It Works
Encryption:

The program reads the image and converts it into a NumPy array.
Each pixel value is XORed with a user-specified key (an integer). This alters the pixel values to create an encrypted version.
The encrypted image is saved.
Decryption:

The program reads the encrypted image and performs the XOR operation again with the same key. XORing twice with the same key reverses the operation.
Input and Output:

The user specifies the input image path, the encryption key, and the output path.
Key Features
Simple Pixel Manipulation: XOR operation ensures reversible encryption.
Supports Various Formats: Works with PNG, JPEG, BMP, etc., using the Pillow library.
Key-Based Security: The encryption is tied to the user's key, making it unique.
Usage
Run the program.
Select encrypt or decrypt.
Provide the input image path, key, and output image path.
View the output image.
