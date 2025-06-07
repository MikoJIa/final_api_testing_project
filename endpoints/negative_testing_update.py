import pytest
import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


class NegativePutTest(BaseEndpoint):

    def put_negative(self, parameters_meme, id_m):

        self.response = requests.put(url=f'{self.url}/meme/{id_m}',
                                     json=parameters_meme,
                                     headers=self.headers)

    def print_response(self):
        if self.response.status_code == 400:
            print("400 Bad Request.Invalid parameters!!!")
        else:
            print("The request was successful")
