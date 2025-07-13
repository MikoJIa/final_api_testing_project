import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class GetAllMeme(BaseEndpoint):
    @allure.step("Getting all the memes")
    def get_all_meme(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(url=f"{self.url}/meme", headers=headers)

    def check_response_json(self):
        response_json = self.response.json()["data"]
        assert isinstance(response_json, list)

    def check_length_response(self):
        assert len(self.response.json()["data"]) > 0

    def check_structure_meme(self):
        if len(self.response.json()["data"]) > 0:
            first_meme = self.response.json()["data"][0]
            assert "updated_by" in first_meme

    def error_responses(self):
        assert "401 Unauthorized" in self.response.text
        print("Not authorized")
