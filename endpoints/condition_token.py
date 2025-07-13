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
    def check_text_token_confirmation(self, name1, name2):
        if self.check_live_token(name1):
            assert self.response.text == f"Token is alive. Username is {name1}"
            print(name1)
        elif self.check_live_token(name2):
            assert self.response.text == f"Token is alive. Username is {name2}"
            print(name2)
        else:
            print("Another account")
