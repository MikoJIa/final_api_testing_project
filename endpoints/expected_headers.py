import pytest

from endpoints.base_endpoint import BaseEndpoint
import requests
import allure


class ExpectedAuthTest(BaseEndpoint):

    @allure.step("Checkin authorization")
    def to_apply_endpoint(self, headers):
        self.response = requests.get(url=f"{self.url}/meme", headers=headers)

    @allure.step("Checking status authorization")
    def output_result(self):
        if self.response.status_code == 401:
            print('401 Unauthorized')
        else:
            print("authorize is valid")
