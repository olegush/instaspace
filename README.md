# Space Instagram

First script, the **fetch_spacex.py** fetches photos of the latest launch of [SpaceX program](https://www.spacex.com/). The second, **fetch_hubble.py** fetches photos of [The Hubble Telescope](http://hubblesite.org/), collection "news". And the third, **upload_to_instagram.py** prepares and publishes photos to Instagram account.


### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

.env file with enviroment variables should contain your password and login to Instagram.
```
LOGIN=your_login
PASSWORD=your_passwod
```


### Quickstart

Run **fetch_spacex.py** or/and **fetch_hubble.py** to fetch photos, wich will be save in **image** folder. Then run **upload_to_instagram.py** it prepares photos in the **images/for_instagram** folder and uploads them to Instagram account.


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
