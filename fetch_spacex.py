import os
import requests
import json


def fetch_spacex_latest_images(url):
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data['links']['flickr_images']


def download_image(url, dir, filename):
    response = requests.get(url)
    if not os.path.isdir(dir):
        os.mkdir(dir)
    with open(os.path.join(dir, filename), 'wb') as file:
        file.write(response.content)


if (__name__ == '__main__'):
    img_dir = 'images'
    spacex_api = 'https://api.spacexdata.com/v3/launches/latest'
    for num, url_img in enumerate(fetch_spacex_latest_images(spacex_api), 1):
        print(url_img)
        filename = 'spacex_latest_{}.jpg'.format(str(num))
        download_image(url_img, img_dir, filename)
