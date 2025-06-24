import allure
import pytest
import requests
from endpoints.base_endpoint import BaseEndpoint


class UpdateMeme(BaseEndpoint):

    @allure.step("Meme update")
    def put_meme(self, id_meme, parameters_meme):
        self.response = requests.put(url=f"{self.url}/meme/{id_meme}",
                                     json=parameters_meme,
                                     headers=self.headers)
        return self.response

    def print_user_name(self):
        self.response