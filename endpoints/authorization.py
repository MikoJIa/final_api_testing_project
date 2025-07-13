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
        print(obj_token)
        return obj_token

    def checking_created_token(self):
        assert self.response.json()['token'] == self.return_token()

    def checking_token_user_name(self, name):
        assert self.response.json()['user'] == name
