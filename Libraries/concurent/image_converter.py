import time
import concurrent.futures

from PIL import Image
from PIL import ImageFilter


IMAGES = ['photo-1585348897687-d7a96a8f7e2a.jpg',
          'photo-1583751180317-6e6cd0a3b870.jpg',
          'photo-1584179307525-24c1d5948b23.jpg',
          'photo-1584903212412-ca40e31585c6.jpg',
          'photo-1584193393092-c3449d91fdd3.jpg',
          'photo-1585749668827-8675327f6e44.jpg',
          'photo-1585390664932-fa7b06f2b03b.jpg',
          'photo-1585496435563-73bb9c679a56.jpg',
          'photo-1584508332313-ce3965484131.jpg',
          'photo-1585830351556-89c487a0c76e.jpg']


def timer(func):

    def inner(*args, **kwargs):
        t0 = time.perf_counter()
        func(*args, **kwargs)
        t1 = time.perf_counter()
        print(f"Time took: {t1-t0:.2f}")

    return inner


def blur_and_resize_image(image_name):
    image = Image.open(f"images_2/{image_name}")
    image.thumbnail((1200, 1200), Image.ANTIALIAS)
    filtered = image.filter(ImageFilter.GaussianBlur)
    filtered.save(f"resized/{image_name}", "JPEG")
    print(f"{image_name} saved")


# @timer
# def resize_images(image_list):
    # for image in image_list:
    # blur_and_resize_image(image)


@timer
def resize_images(image_list: list):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(blur_and_resize_image, image)
                   for image in image_list]
        for res in concurrent.futures.as_completed(results):
            print(res.result())

        # results = executor.map(blur_and_resize_image, image_list)
        # for result in results:
        #     print(result)

        # results = [executor.submit(blur_and_resize_image, image)
            #    for image in image_list]
        # for res in concurrent.futures.as_completed(results):
        #     print(res.result())


resize_images(IMAGES)
