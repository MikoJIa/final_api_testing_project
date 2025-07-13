import allure
import requests

from endpoints.base_endpoint import BaseEndpoint
from endpoints.create_meme import CreateMeme


class NegativeCreateMeme(CreateMeme):

    @allure.step("Checking negative meme")
    def negative_create(self, param_body):
        self.response = requests.post(url=f"{self.url}/meme", json=param_body, headers=self.headers)
        return self.response

    def invalid_data_typs(self):
        assert "Invalid parameters" in self.response.text
