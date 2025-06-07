import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class GetAllMeme(BaseEndpoint):
    @allure.step("Getting all the memes")
    def get_all_meme(self, headers):
        self.response = requests.get(url=f"{self.url}/meme", headers=headers)
