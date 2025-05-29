import pickle

import allure

from endpoints.base_endpoint import BaseEndpoint
import requests


class LiveToken(BaseEndpoint):

    @allure.step("Verification of the viability of the token")
    def check_live_token(self, name):
        with open('token.pkl', 'rb') as file:
            token = pickle.load(file)
        self.response = requests.get(url=f"{self.url}/authorize/{token}")
        if name in self.response.text:
            return True
        return False

    @allure.step("Verifying the validity of the token's lifetime confirmation text")
    def check_text_token_confirmation(self):
        assert self.response.text == "Token is alive. Username is Mikola"
