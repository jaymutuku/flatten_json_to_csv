import requests
from config import client_id, client_secret

token_url = "<URL_ENDPOINT>"


payload = {
    "username": "<USERNAME>",
    "password": "<PASSWORD>",
    "grant_type": "password",
}


def generateToken():
    response = requests.post(token_url, auth=(client_id, client_secret), data=payload)

    if response.ok:
        bearer_token = response.json()["access_token"]
        print("new token : ", bearer_token)
        return bearer_token
    else:
        raise Exception("Cannot fetch access token:{}".format(response.status_code))


token = generateToken()
