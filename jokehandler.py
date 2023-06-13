import requests
import datetime

class Jokehandler:
    def __init__(self, adress):
        self.adress = adress
        self.nu = datetime.datetime.now()

    def get_joke(self):
        req = requests.get(self.adress)
        json_data = req.json()
        joke = json_data["joke"]
        funcnu = datetime.datetime.now()

        return joke
