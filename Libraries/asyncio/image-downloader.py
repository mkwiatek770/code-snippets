"""
Download multiple images from unsplash concurrently.
"""
import requests
import os
import asyncio
import aiohttp
import time
import concurrent.futures
from contextlib import closing


IMAGES = [
    "https://images.unsplash.com/photo-1478264635837-66efba4b74ba?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1941&q=80",
    "https://images.unsplash.com/photo-1478368499690-1316c519df07?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1353&q=80",
    "https://images.unsplash.com/photo-1526818614391-390bc085968b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60",
    "https://images.unsplash.com/photo-1519608419835-84525d3f0473?ixlib=rb-1.2.1&auto=format&fit=crop&w=2090&q=80",
    "https://images.unsplash.com/photo-1509817177816-ca503fa03f60?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
    "https://images.unsplash.com/photo-1519427107403-087c96eed2df?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80",
    "https://images.unsplash.com/photo-1509747004090-da7453da79eb?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80",
    "https://images.unsplash.com/photo-1478059299873-f047d8c5fe1a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1868&q=80",
    "https://images.unsplash.com/photo-1478155536073-c815e5cefe44?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1906&q=80",
    "https://images.unsplash.com/photo-1478811482469-30ec30b9f534?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80",
    "https://images.unsplash.com/photo-1474123685650-afa16479e04b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80",
    "https://images.unsplash.com/photo-1545297730-c7a5ff431e8a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=656&q=80",
    "https://images.unsplash.com/photo-1567161291271-549795048c09?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1923&q=80",
    "https://images.unsplash.com/photo-1484704407203-402da6f3879d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80",
    "https://images.unsplash.com/photo-1559899289-36ec37c9ac61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80"
]


def get_image_path(image_url: str) -> str:
    filename = image_url.split("?")[0].split("unsplash.com/")[1] + ".jpg"
    absolute_path = os.path.abspath(os.path.join("images", filename))
    return absolute_path


async def download_image(image_url: str, session: aiohttp.ClientSession) -> str:

    async with session.get(image_url) as response:
        path = get_image_path(image_url)
        with open(path, "wb") as image:
            await image.write(response.read())



@asyncio.coroutine
def download_images(images: list, session: aiohttp.ClientSession) -> None:
    """
    Concurrently download multiple images.
    """
    download_futures = [download_image(url, session) for url in images]
    print("Results")
    for download_future in asyncio.as_completed(download_futures):
        result = yield from download_future
        print("finished: ", result)


def main():
    with closing(asyncio.get_event_loop()) as loop:
        with aiohttp.ClientSession() as session:
            result = loop.run_until_complete(download_images(IMAGES, session))
            print("finished: ", result)


download_images(IMAGES)
