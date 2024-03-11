**Title: Image Encryption and Decryption using Python**

**Overview:**
This Python script provides functionality to encrypt and decrypt images using a simple encryption algorithm. The script utilizes the Python Imaging Library (PIL) to manipulate image data.

**Features:**
- Image encryption using a provided encryption key.
- Image decryption using the same encryption key.
- Encryption and decryption processes performed pixel-wise.

**Dependencies:**
- Python 3.x
- PIL (Python Imaging Library)

**Usage:**
1. Clone the repository to your local machine.
2. Navigate to the directory containing the script.
3. Ensure Python and PIL are installed.
4. Run the script using Python.

**Instructions:**
1. **Installation:**
   - Clone the repository using the following command:
     ```
     git clone https://github.com/your_username/your_repository.git
     ```
   - Ensure Python and PIL are installed on your system.

2. **Running the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Run the script using Python:
     ```
     python image_encrypt_decrypt.py
     ```

3. **Input Parameters:**
   - When prompted, enter the path of the image you want to encrypt/decrypt.
   - Enter the encryption key as an integer.

4. **Encryption:**
   - The script will encrypt the provided image using the specified encryption key.
   - The encrypted image will be saved as "encrypted_image.png" in the same directory.
   - A success message will be displayed upon completion.

5. **Decryption:**
   - The script will decrypt the encrypted image using the same encryption key.
   - The decrypted image will be displayed.
   - A success message will be displayed upon completion.

**Example:**
```
Enter the path of the image: /path/to/your/image.jpg
Enter the encryption key: 12345
Image encrypted successfully!
Image decrypted successfully!
```

**Note:**
- Ensure that you have the necessary permissions to read/write files in the specified directories.
- This script provides basic encryption and decryption functionality and may not be suitable for secure applications.
- The encrypted image is saved as "encrypted_image.png" and will overwrite any existing file with the same name.

