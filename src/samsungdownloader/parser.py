"""
For parsing data related to the device.
"""
from .exceptions import *
from bs4 import BeautifulSoup

def get_image_url(soup: BeautifulSoup) -> str:
    """
    Returns the URL of the device's image.
    """
    img_url = soup.find("div", {"class": "support-product-hero__image"}).find("img")["data-desktop-src"]
    if "no_result" in img_url:
        raise ImageNotFound
    return f"https:{img_url.split('?')[0]}?$__PNG$"

def get_device_name(soup: BeautifulSoup) -> dict:
    """
    Returns the name and code of the device.
    """
    return {
        "name": soup.find("h2", {"class": "support-product-hero__lnb-product-name"}).text,
        "codename": soup.find("span", {"class": "support-product-hero__lnb-product-code"}).text.replace("/", "_")
    }
