import cv2
import numpy as np

class ImageSecurity:
    def __init__(self, img_path):
        self.img_path = img_path
        self.original_img = self.loadImage()

    def loadImage(self):
        img = cv2.imread(self.img_path)
        if img is None:
            raise FileNotFoundError("Image file not found.")
        return img

    def convertToGrayscale(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def convertToBinary(self, img):
        _, binary_img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
        return binary_img

    def convertToDecimal(self, binary_img):
        decimal_img = binary_img.astype(np.uint8)
        return decimal_img

    def showImages(self, original, encrypted, decrypted):
        cv2.imshow('Original Image', original)
        cv2.imshow('Encrypted Image', encrypted.astype(np.uint8))
        cv2.imshow('Decrypted Image', decrypted.astype(np.uint8))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

class CryptoProcessor:
    def generateChaoticMatrix(self, rows, cols):
        chaotic_matrix = np.random.randint(0, 256, (rows, cols), dtype=np.uint8)
        return chaotic_matrix

    def scrambleImage(self, img, chaotic_matrix):
        scrambled_img = cv2.bitwise_xor(img, chaotic_matrix)
        return scrambled_img

    def encryptImage(self, original_img):
        gray_img = ImageSecurity.convertToGrayscale(self, original_img)
        binary_img = ImageSecurity.convertToBinary(self, gray_img)

        rows, cols = binary_img.shape

        chaotic_key1 = self.generateChaoticMatrix(rows, cols)
        chaotic_key2 = self.generateChaoticMatrix(rows, cols)

        scrambled_img = self.scrambleImage(binary_img, chaotic_key1)
        scrambled_img = self.scrambleImage(scrambled_img, chaotic_key2)

        encrypted_img = ImageSecurity.convertToDecimal(self, scrambled_img)

        return encrypted_img, chaotic_key1, chaotic_key2

    def decryptImage(self, encrypted_img, chaotic_key1, chaotic_key2):
        decrypted_img = self.scrambleImage(encrypted_img, chaotic_key2)
        decrypted_img = self.scrambleImage(decrypted_img, chaotic_key1)
        decrypted_img = ImageSecurity.convertToDecimal(self, decrypted_img)

        return decrypted_img

if __name__ == "__main__":
    img_path = 'C:/Users/megha/Downloads/photo.jpg'   # Choose images

    try:
        img_security = ImageSecurity(img_path)
        crypto_processor = CryptoProcessor()

        encrypted_img, key1, key2 = crypto_processor.encryptImage(img_security.original_img)

        decrypted_img = crypto_processor.decryptImage(encrypted_img, key1, key2)

        img_security.showImages(img_security.original_img, encrypted_img, decrypted_img)

    except Exception as e:
        print(f"An error occurred: {e}")
