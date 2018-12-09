import os
import requests
import json


def fetch_hubble_image(url, id):
    response = requests.get(url + str(id))
    json_data = json.loads(response.text)['image_files']
    json_data_max = max(
        json_data,
        key=lambda size: size['width'] * size['height']
    )
    return json_data_max['file_url']


def download_image(url, dir, filename):
    response = requests.get(url)
    if not os.path.isdir(dir):
        os.mkdir(dir)
    with open(os.path.join(dir, filename), 'wb') as file:
        file.write(response.content)


def get_file_ext(url):
    return os.path.splitext(url)[1]


if (__name__ == '__main__'):
    img_dir = 'images'
    hubble_api_img = 'http://hubblesite.org/api/v3/image/'
    hubble_api_collection = 'http://hubblesite.org/api/v3/images'
    params = {'page': 1, 'collection_name': 'news'}
    response = requests.get(hubble_api_collection, params=params)
    for img in json.loads(response.text):
        hubble_img_url = fetch_hubble_image(hubble_api_img, img['id'])
        hubble_img_ext = get_file_ext(hubble_img_url)
        filename = 'hubble_{}{}'.format(str(img['id']), hubble_img_ext)
        download_image(hubble_img_url, img_dir, filename)
        print('{} was saved as {}'.format(hubble_img_url, filename))
