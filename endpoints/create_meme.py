import requests
import json
import allure
import pickle
from endpoints.base_endpoint import BaseEndpoint
from endpoints.condition_token import LiveToken
from src.enums.error_enums_global import GlobalErrorMessages


class CreateMeme(BaseEndpoint):

    @allure.step("Creating a new meme")
    def create_new_meme(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(url=f"{self.url}/meme", json=body, headers=headers)
        if self.response.status_code == 200:
            with open('id_meme.txt', 'w') as file:
                file.write(str(self.response.json()['id']))
            print(self.headers["Authorization"])
        return self.response

    def check_body_data(self, valid_data):
        for data, class_data in valid_data.items():
            assert isinstance(self.response.json()[data], class_data)

    def check_user_name_meme(self, user_name):
        assert self.response.json()['updated_by'] == user_name
        print(self.response.json()['updated_by'])

    def check_status_code_headers(self, body):
        response = self.create_new_meme(body=body, headers={})
        assert response.status_code == 401
