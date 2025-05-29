import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class GetOneMeme(BaseEndpoint):
    @allure.step("Getting only one meme")
    def get_only_one_meme(self, id_meme, path="/"):
        self.response = requests.get(url=f"{self.url}{path}meme{path}{id_meme}", headers=self.headers)
        self.id_meme = self.response.json()['id']

    @allure.step("Checking the found id meme")
    def check_id_meme(self, id_meme):
        assert self.id_meme == id_meme
