import base64
import random
import string
from pathlib import Path


def encode_image(image_path) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def id_generator(size=8, chars=string.ascii_uppercase + string.digits) -> str:
    return ''.join(random.choice(chars) for _ in range(size))


def read_file(filename: str) -> str:
    try:
        reading_file = open(filename, "r", encoding="utf-8")
        return reading_file.read()
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return ""


def check_images_dir() -> None:
    if not Path('images').is_dir():
        Path('images').mkdir()
