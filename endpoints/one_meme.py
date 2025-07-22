import allure
import requests
import uuid
from endpoints.base_endpoint import BaseEndpoint
from src.enums.error_enums_global import GlobalErrorMessages


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
        assert self.response.status_code == 404, GlobalErrorMessages.WRONG_STATUS_CODE_404.value

    @allure.step("Check for deletion of non-existent meme")
    def checking_non_existent_meme_id(self):
        self.random_id = str(uuid.uuid4())
        get_meme = self.get_only_one_meme(self.random_id)
        if "404 Not Found" in get_meme.text:
            print("There is no meme with this id.")
            return self.random_id
        else:
            return "Such an id exists"
