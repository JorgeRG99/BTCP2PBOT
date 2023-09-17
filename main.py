import requests
from requests.auth import HTTPBasicAuth
import pprint
from dotenv import load_dotenv
import os
from http.client import HTTPSConnection
from base64 import b64encode

load_dotenv()

TOKEN_SHA256 = os.environ.get('TOKEN_SHA256')
PRIV_KEY = os.environ.get('PRIV_KEY')
PUB_KEY = os.environ.get('PUB_KEY')

URL = 'https://learn.robosats.com/'
CREATE_USER_ENDPOINT = "api/user/"
TOKEN = os.environ.get('TOKEN')

params2 = {
  "token_sha256": TOKEN_SHA256,
  "public_key": PUB_KEY,
  "encrypted_private_key": PRIV_KEY,
}

params = [
  {
    "id": 0,
    "expires_at": "2019-08-24T14:15:22Z",
    "type": 0,
    "currency": 0,
  }
]

def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'

response = requests.get(url=URL+CREATE_USER_ENDPOINT, params=params)

""" if response.status_code == 200:
    # Request was successful
    data = response.json()  # Assuming the response is in JSON format
    print("API response:", data)
else:
    pprint.pprint(response.reason) """