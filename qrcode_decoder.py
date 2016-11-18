#!/usr/bin/env python
from flask import Flask, Response, request
from PIL import Image
from io import BytesIO
import requests
import json
import zbarlight
import logging

logger = logging.getLogger('main-log')
logger.setLevel(logging.INFO)

fh = logging.FileHandler('log.txt')
fh.setFormatter(logging.Formatter('%(asctime)s - PID: %(process)d - ThreadID: %(thread)d - %(levelname)s - %(message)s'))
logger.addHandler(fh)

app = Flask(__name__)

@app.route('/')
def index():
    logger.info('/')
    return "Hello, World!"

@app.route('/google.html', methods=['GET'])
def acquire():
  logger.info('google verification')
  return 'google-site-verification: google.html'

@app.route('/decode', methods=['POST'])
def decode():
    response_body = request.get_json()
    url = response_body['url']
    try:
      img = fetchImage(url)
      texts = decodeQrcode(img)
    except:
      logger.info('Exception - url: %s'%url)
      return Response(status = 503)
    else:
      logger.info('url: %s, text: %s'%(url, texts))
      return Response(
          response=json.dumps({'codes': texts}),
          status=200,
          mimetype='application/json'
      )

def decodeQrcode(img):
  codes = zbarlight.scan_codes('qrcode', img)
  img.close()
  return list(map(lambda x: x.decode(), codes))

def fetchImage(url):
  response = requests.get(url=url, timeout=(5, 1))
  return Image.open(BytesIO(response.content))

if __name__ == '__main__':
    app.run(debug=True, port=80)
