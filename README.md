## Image-based Data Hiding and Retrieval
This project implements a basic image steganography technique using Python and OpenCV to hide and retrieve secret text messages in an image file. The system encrypts the message by XOR-ing each character of the message with a security key and embedding it in the RGB planes of the image pixels. The process also allows for decryption of the embedded message using the same key.

### Features:
- **Data Hiding**: Hide a secret text message within an image by modifying pixel values using a security key.
- **Encryption**: Uses XOR encryption between the message characters and the key to ensure basic security.
- **Data Retrieval**: Extract and decrypt the hidden message using the correct security key.
- **OpenCV Integration**: Leverages OpenCV for image reading, writing, and pixel manipulation.

### How it Works:
- The program reads an image and converts the message into ASCII values.
- The message is encrypted by XOR-ing it with the user-provided security key.
- The encrypted values are then stored in the RGB channels of the image pixels.
- The encrypted image is saved, and the original message can later be extracted using the same key.

### Usage:
1. Run the script and provide the image path, security key, and text to hide.
2. Save the encrypted image.
3. To retrieve the hidden text, rerun the script, provide the security key, and extract the message.
