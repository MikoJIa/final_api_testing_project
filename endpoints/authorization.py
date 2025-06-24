import pickle

import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class AuthorizeUser(BaseEndpoint):

    @allure.step("Getting token for authorization")
    def authorize_user(self, body):
        self.response = requests.post(url=f"{self.url}/authorize", json=body)
        with open('token.pkl', 'wb') as file:
            pickle.dump(self.response.json()['token'], file)

    def return_token(self):
        with open('token.pkl', 'rb') as file:
            obj_token = pickle.load(file)
        return obj_token

    def print_name_user(self):
        print(self.response.json())
