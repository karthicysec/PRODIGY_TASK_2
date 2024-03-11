from PIL import Image

def process_image(image_path, key, action):
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    processed_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            if action == "encrypt":
                r ^= key
                g ^= key
                b ^= key
            elif action == "decrypt":
                r ^= key
                g ^= key
                b ^= key

            processed_pixels.append((r, g, b))

    processed_img = Image.new(img.mode, img.size)
    processed_img.putdata(processed_pixels)

    if action == "encrypt":
        processed_img.save("encrypted_image.png")
        print("Image encrypted successfully!")
    elif action == "decrypt":
        processed_img.show()
        print("Image decrypted successfully!")

# Input image path and encryption key
image_path = input("Enter the path of the image: ")
encryption_key = int(input("Enter the encryption key: "))

# Encrypt the image
process_image(image_path, encryption_key, "encrypt")

# Decrypt the image
encrypted_image_path = "encrypted_image.png"
process_image(encrypted_image_path, encryption_key, "decrypt")