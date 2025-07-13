import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class GetOneMeme(BaseEndpoint):
    @allure.step("Getting only one meme")
    def get_only_one_meme(self, id_meme, path="/"):
        self.response = requests.get(url=f"{self.url}{path}meme{path}{id_meme}", headers=self.headers)
        return self.response

    @allure.step("Checking Content-Type is application/json")
    def check_content_type_is_json(self):
        assert self.response.headers["Content-type"] == "application/json"

    @allure.step("Checking the found meme data")
    def check_meme_data(self, params):
        for key, value in params.items():
            assert self.response.json()[key] == value
            assert self.response.json()[key] == value
            assert self.response.json()[key] == value
            assert self.response.json()[key] == value

    @allure.step("Check 404 status for non-existent meme")
    def check_status_code_is_404(self):
        assert self.response.status_code == 404
