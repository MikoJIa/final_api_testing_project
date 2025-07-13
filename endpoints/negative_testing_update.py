import pytest
import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


class NegativePutTest(BaseEndpoint):

    def put_negative(self, parameters_meme, id_m):

        self.response = requests.put(url=f'{self.url}/meme/{id_m}',
                                     json=parameters_meme,
                                     headers=self.headers)

    def check_negative_data_update_meme_expected(self, expected):
        assert self.response.status_code == expected
