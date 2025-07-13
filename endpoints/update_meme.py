import allure
import pytest
import requests
from endpoints.base_endpoint import BaseEndpoint
from endpoints.one_meme import GetOneMeme
from src.enums.error_enums_global import GlobalErrorMessages


class UpdateMeme(BaseEndpoint):

    @allure.step("Meme update")
    def put_meme(self, id_meme, parameters_meme):
        self.response = requests.put(url=f"{self.url}/meme/{id_meme}",
                                     json=parameters_meme,
                                     headers=self.headers)
        return self.response

    def check_data_updated_meme(self, id_meme, new_update_data):
        self.response_2 = requests.get(url=f"{self.url}/meme/{id_meme}", headers=self.headers)
        for field, new_value in new_update_data.items():
            if field in self.response_2.json():
                assert self.response_2.json()[field] != new_value
            else:
                print(GlobalErrorMessages.WRONG_FIELD.value)

    def check_negative_data_update_meme_expected(self, expected):
        assert self.response.status_code == expected
