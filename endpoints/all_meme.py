import allure
import requests
from endpoints.base_endpoint import BaseEndpoint
import json


class GetAllMeme(BaseEndpoint):
    @allure.step("Getting all the memes")
    def get_all_meme(self):
        self.response = requests.get(url=f"{self.url}/meme", headers=self.headers)
