"""
Use a one-time pad to encrypt and decrypt images.
"""
from typing import Tuple
from random import randint
from encryption import random_key


def encrypt_image(image_path: str):
    with open(image_path, "rb") as image:
        image = bytearray(image.read())
        key = randint(1, 20)
        for index, value in enumerate(image):
            image[index] = value^key
        return image, key


def save_image(image_bytes: bytearray, file_name="encrypted.jpeg"):
    with open(file_name, "wb") as image:
        image.write(bytes(image_bytes))

def decrypt_image(image: bytearray, key: int) -> bytes:
    for index, value in enumerate(image):
        image[index] = value^key
    return image



if __name__ == "__main__":
    image_path = './image.jpeg'
    encrypted, key = encrypt_image(image_path)
    save_image(encrypted)
    
    decrypted = decrypt_image(encrypted, key)
    save_image(decrypted, "s.jpeg")

