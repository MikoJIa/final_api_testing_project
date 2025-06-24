import requests
import json
import allure
import pickle
from endpoints.base_endpoint import BaseEndpoint
from endpoints.condition_token import LiveToken


class CreateMeme(BaseEndpoint):

    @allure.step("Creating a new meme")
    def create_new_meme(self, body):
        self.response = requests.post(url=f"{self.url}/meme", json=body, headers=self.headers)
        if self.response.json()["updated_by"] == "Mikola":
            with open('id_meme.txt', 'w') as file:
                file.write(str(self.response.json()['id']))
        else:
            with open('id_meme_alex.txt', 'w') as file:
                file.write(str(self.response.json()['id']))
        return self.response

    def check_body_text(self):
        assert self.response.json()['text'] == "I love memes"
