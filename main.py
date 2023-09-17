import requests
from requests.auth import HTTPBasicAuth
import pprint
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN_SHA256 = os.environ.get('TOKEN_SHA256')
PRIV_KEY = os.environ.get('PRIV_KEY')
PUB_KEY = os.environ.get('PUB_KEY')

URL = 'https://learn.robosats.com/'
CREATE_USER_ENDPOINT = "api/user/"
TOKEN = os.environ.get('TOKEN')
USER = 'FunnyTitanium24'

params = {
  "token_sha256": TOKEN_SHA256,
  "public_key": PUB_KEY,
  "encrypted_private_key": PRIV_KEY,
}

response = requests.get(url=URL+CREATE_USER_ENDPOINT, auth=HTTPBasicAuth(USER, TOKEN), params=params)

""" if response.status_code == 200:
    # Request was successful
    data = response.json()  # Assuming the response is in JSON format
    print("API response:", data)
else:
    pprint.pprint(response.reason) """