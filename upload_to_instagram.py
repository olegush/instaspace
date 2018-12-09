import os
import math
from dotenv import load_dotenv
from instabot import Bot
import time
import random
from PIL import Image, ImageFilter


def expand_image(img, width, height, ratio, width_ratio, height_ratio):
    delta_w = math.ceil((width * (width_ratio / ratio - 1)) / 2)
    delta_h = math.ceil((height * (ratio / height_ratio - 1)) / 2)
    box = (delta_w, delta_h, width + delta_w, height + delta_h)
    region = img.crop()
    img_res = img.resize((width + delta_w * 2, height + delta_h * 2))
    img_filtered = img_res.filter(ImageFilter.GaussianBlur(20))
    img_filtered.paste(region, box)
    return img_filtered


def get_image_for_instagram(path, filename, dir_insta):
    img = Image.open(path)
    width, height = img.size
    # image resolutions https://help.instagram.com/1631821640426723
    if width > 1080:
        width, height = 1080, int(height * 1080 / width)
        img = img.resize((width, height))
    ratio = width / height
    width_ratio, height_ratio = (0.8, 1.91)
    if ratio < width_ratio:
        img = expand_image(img, width, height, ratio, width_ratio, ratio)
    elif ratio > height_ratio:
        img = expand_image(img, width, height, ratio, ratio, height_ratio)
    filename_new = os.path.splitext(filename)[0] + '.jpg'
    path_new = os.path.join(dir_insta, filename_new)
    img.save(path_new, 'JPEG')
    return path_new


if (__name__ == '__main__'):
    img_dir = 'images'
    dir_insta = 'images/for_instagram'
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    bot = Bot()
    bot.login(username=login, password=password)
    for entry in os.listdir(img_dir):
        path = os.path.join(img_dir, entry)
        if not os.path.isdir(path):
            path_new = get_image_for_instagram(path, entry, dir_insta)
            caption = ''
            bot.upload_photo(path_new, caption=caption)
            sec = random.random()*5 + 10
            time.sleep(sec)
