import requests
import json
from endpoints.base_endpoint import BaseEndpoint
import allure
from endpoints.one_meme import GetOneMeme


class DeleteMeme(BaseEndpoint):

    @allure.step("Deleting meme")
    def deleting_meme(self, id_meme, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(url=f"{self.url}/meme/{id_meme}", headers=headers)
        return self.response

    @allure.step("Check for deletion of non-existent meme")
    def check_non_existent_meme_deleted(self, checking_non_existent_meme_id):
        if checking_non_existent_meme_id != "Such an id exists":
            random_id = checking_non_existent_meme_id
            assert self.deleting_meme(random_id).status_code == 404
            print("The requested URL was not found on the server")
        else:
            print("such an id exists")
