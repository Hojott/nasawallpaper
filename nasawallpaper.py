import os
import requests, json
from dotenv import load_dotenv

# Loads .env file and creates vars
load_dotenv()
API_KEY = os.getenv('NASA_API_KEY')
if API_KEY is None:
    print("ERROR: NASA_API_KEY not defined.\nPlease visit https://api.nasa.gov/ and get your API Key, then create .env and add it there:\nNASA_API_KEY=...")
    exit()

NAME = os.getenv('NASA_NAME')
if NAME is None:
    NAME = "nasawallpaper"

DIR = os.getenv('NASA_DIR')
if DIR is None:
    DIR = str(os.path.dirname(os.path.realpath(__file__)))+"/"
else:
    if DIR[-1] != '/':
        DIR = DIR+'/'

FORMAT = os.getenv('NASA_FORMAT')
if FORMAT is None:
    FORMAT = "png"

nasalink = "https://api.nasa.gov/planetary/apod?api_key="+API_KEY
image = DIR+NAME+'.'+FORMAT

# Gets from NASA API and writes it to file
api_response = requests.get(nasalink)
api_json = api_response.text
api_dict = json.loads(api_json)
imagelink = api_dict["hdurl"]

img_response = requests.get(imagelink)
if img_response.status_code:
    img = open(image, 'wb')
    img.write(img_response.content)
    img.close()
    print("Image created in", image)
