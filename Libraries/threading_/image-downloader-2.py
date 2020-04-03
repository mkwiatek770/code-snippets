"""
Using unsplash API download X high resolution images and then edit them
using Pillow library
"""
import os
import time
import requests
import concurrent.futures
# from .image_downloader import download_image, download_images
# from .image_downloader import get_image_path


API_ACCESS_KEY = os.environ.get("UNSPLASH_ACCESS_KEY")
RANDOM_IMAGE_ENDPOINT = f'https://api.unsplash.com/photos/random?client_id={API_ACCESS_KEY}'


def timer(func):

    def inner(*args, **kwargs):
        t0 = time.perf_counter()
        func(*args, **kwargs)
        t1 = time.perf_counter()
        print(f"Time took: {t1-t0:.2f} seconds.")
    return inner


def download_image():
    image_data = requests.get(RANDOM_IMAGE_ENDPOINT)
    if image_data.status_code != 200:
        raise Exception(image_data.text)
    image_url = image_data.json()['urls']['full']

    image = requests.get(image_url)
    path = get_image_path(image_url)
    with open(path, "wb") as im:
        im.write(image.content)

    print(f"Downloaded image {image_url}")


def get_image_path(image_url: str) -> str:
    filename = image_url.split("?")[0].split("unsplash.com/")[1] + ".jpg"
    absolute_path = os.path.abspath(os.path.join("images_2", filename))
    return absolute_path


@timer
def download_images(n: int):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(download_image) for _ in range(n)]
        for f in concurrent.futures.as_completed(results):
            try:
                f.result()
            except Exception as err:
                print(str(err))


download_images(10)
