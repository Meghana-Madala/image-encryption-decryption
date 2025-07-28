# Secure Image Encryption and Decryption for Network Security

This project demonstrates a basic secure image encryption and decryption mechanism using chaotic matrices and bitwise XOR operations. It converts an image to grayscale, applies binary thresholding, encrypts it using randomly generated chaotic keys, and then successfully decrypts it to retrieve the original image.

## Features

- Load and display input image
- Convert image to grayscale and binary
- Encrypt image using XOR with chaotic matrices
- Decrypt the image using inverse XOR operations
- Visualize original, encrypted, and decrypted images

## Technologies Used

- Python
- OpenCV (`cv2`)
- NumPy

## Workflow

1. Load the image from the specified path.
2. Convert the image to grayscale.
3. Apply binary thresholding.
4. Generate two chaotic matrices (keys).
5. Encrypt the image by scrambling it twice using XOR and the chaotic matrices.
6. Decrypt the image by reversing the XOR operations.
7. Display original, encrypted, and decrypted images.

### Prerequisites

- Python 3.x
- Install required libraries:
```bash
pip install opencv-python numpy
```

### Run the Script

Update the `img_path` in `ImageEncryptDecrypt.py` to point to your image file.

## Example

```python
img_path = 'C:/Users/megha/Downloads/photo.jpg'
```

## Output

- `Original Image`: The input image before encryption
- `Encrypted Image`: The result of applying XOR with two chaotic matrices
- `Decrypted Image`: The reconstructed image after decryption

## Notes

- This implementation uses NumPy's `random.randint` for chaos, which can be extended to more complex chaotic systems like logistic maps or Arnold Cat maps.
- The encryption technique here is for educational purposes and does not represent a secure cryptographic algorithm for production use.

## Author

Meghana Madala  
Graduate Student, Computer Science  
University of Memphis