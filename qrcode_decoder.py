#!/usr/bin/env python
from flask import Flask
from flask import request
import json

from PIL import Image
import requests
from io import BytesIO

import zbarlight

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/google.html', methods=['GET'])
def acquire():
  print('google verification')
  return 'google-site-verification: google.html'

@app.route('/decode', methods=['POST'])
def decode():
    response_body = request.get_json()
    print(response_body)
    url = response_body['url']
    try:
      img = fetchImage(url)
      text = decodeQrcode(img)
    except:
      print('Exception - url: %s'%url)
      return ''
    else:
      print('url: %s\ntext: %s'%(url, text))
      return text

def decodeQrcode(img):
  gray_image = img.convert('L')
  code = zbarlight.qr_code_scanner(gray_image.tobytes(), *gray_image.size)
  text = code.decode()
  return text


def fetchImage(url):
  response = requests.get(url=url, timeout=(3, 0.3))
  return Image.open(BytesIO(response.content))


if __name__ == '__main__':
    app.run(debug=True, port=80)
