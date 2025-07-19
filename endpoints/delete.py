import requests
import uuid
import json
from endpoints.base_endpoint import BaseEndpoint
import allure
from endpoints.one_meme import GetOneMeme


class DeleteMeme(BaseEndpoint):

    @allure.step("Deleting meme")
    def deleting_meme(self, id_meme):
        self.response = requests.delete(url=f"{self.url}/meme/{id_meme}", headers=self.headers)
        return self.response

    @allure.step("Check if the meme has really been deleted")
    def check_deleted_meme(self, id_meme):
        if self.check_status_code_is_200:
            get_del_mem = GetOneMeme.get_only_one_meme(id_meme)
            assert "404 Not found" in get_del_mem.text
        else:
            print("The status of the code does not match the expected one.")

    @allure.step("Meme removal check")
    def check_deleted_meme(self, id_meme):
        assert "404 Not Found" in GetOneMeme().get_only_one_meme(id_meme).text
        print('The requested URL was not found on the server.')

    @allure.step("Check for deletion of non-existent meme")
    def checking_non_existent_meme_id(self):
        self.random_id = str(uuid.uuid4())
        get_meme = GetOneMeme().get_only_one_meme(self.random_id)
        assert "404 Not Found" in get_meme.text
        if "404 Not Found" in get_meme.text:
            print("There is no meme with this id.")
            return True
        else:
            return False

    @allure.step("Check for deletion of non-existent meme")
    def deleted_non_existent_meme(self):
        if self.checking_non_existent_meme_id:
            assert self.deleting_meme(self.random_id).status_code == 404
            print("The requested URL was not found on the server")
        else:
            print("such an id exists")
