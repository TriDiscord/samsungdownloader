import sys
import requests
from .parser import *

def get_device_preview_image(support_url: str) -> bytes:
    """
    Returns the device's preview image.
    """
    content = requests.get(support_url).text
    soup = BeautifulSoup(content, "html.parser")
    img = requests.get(get_image_url(soup)).content
    names = get_device_name(soup)
    return {
        "name": names["name"],
        "codename": names["codename"],
        "image": img
    }
