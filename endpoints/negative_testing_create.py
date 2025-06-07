import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


class NegativeCreateTest(BaseEndpoint):

    @allure.step("Negative creating meme")
    def create_negative(self, param_body):
        self.response = requests.post(url=f"{self.url}/meme", json=param_body, headers=self.headers)

    @allure.step("Printout of the text with possible errors")
    def print_failed_text(self):
        if "Invalid parameters" in self.response.text:
            print("400 Bad Request. Invalid parameters")
        elif "or proxy" in self.response.text:
            print("The browser (or proxy) sent a request that this server could not understand.")
