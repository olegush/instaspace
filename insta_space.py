import os
import requests
import json
from dotenv import load_dotenv
from instabot import Bot
from PIL import Image
import time
import random


def fetch_spacex_latest_images(url):
    request = requests.get(url)
    json_data = json.loads(request.text)
    return json_data['links']['flickr_images']


def fetch_hubble_image(url, id):
    request = requests.get(url + str(id))
    json_data = json.loads(request.text)['image_files']
    json_data_max = max(json_data, key=lambda size: size['width'] * size['height'])
    return json_data_max['file_url']


def download_image(url, dir, filename):
    request = requests.get(url)
    if not os.path.isdir(dir):
        os.mkdir(dir)
    with open(os.path.join(dir, filename), 'wb') as file:
        file.write(request.content)


def get_file_ext(url):
    filename = os.path.split(url)[1]
    return os.path.splitext(filename)[1]


if (__name__ == '__main__'):
    dir = 'images'

    '''
    # download spaceX images
    spacex_api = 'https://api.spacexdata.com/v3/launches/latest'
    for num, url_img in enumerate(fetch_spacex_latest_images(spacex_api), 1):
        print(url_img)
        filename = 'spacex_latest_' + str(num) + '.jpg'
        download_image(url_img, dir, filename)
    
    #download hubble images
    hubble_api_img = 'http://hubblesite.org/api/v3/image/'
    hubble_api_collection = 'http://hubblesite.org/api/v3/images'
    params = {'page': 1, 'collection_name': 'news'}
    request = requests.get(hubble_api_collection, params=params)
    
    for img in json.loads(request.text):
        hubble_img_url = fetch_hubble_image(hubble_api_img, img['id'])
        hubble_img_ext = get_file_ext(hubble_img_url)
        filename = 'hubble_' + str(img['id']) + hubble_img_ext
        download_image(hubble_img_url, dir, filename)
        print('{} was saved as {}'.format(hubble_img_url, filename))
    '''


    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    bot = Bot()
    bot.login(username=login, password=password)
    for entry in os.listdir(dir):
        path = os.path.join(dir, entry)
        #if not os.path.isdir(path):
            #img = Image.open(path)
            #img_res = img.resize(300, 400, Image.ANTIALIAS)
            #img_res.save('image/1.jpg')
            #caption = ''
            #bot.upload_photo(path, caption=caption)
            #sec = random.random()*5 + 10
            #time.sleep(sec)

