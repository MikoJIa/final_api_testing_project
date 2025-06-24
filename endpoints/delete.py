import requests
import json
from endpoints.base_endpoint import BaseEndpoint
import allure
from endpoints.one_meme import GetOneMeme


class DeleteMeme(BaseEndpoint):

    @allure.step("Deleting meme")
    def deleting_meme(self, id_meme):
        self.response = requests.delete(url=f"{self.url}/meme/{id_meme}", headers=self.headers)
        return self.response

    @allure.step("Checking if a user can delete someone else's meme")
    def check_another_user_delete_meme(self, name):
        assert self.response.status_code == 403
        print(f"{self.response.status_code}: {name} - You are not the meme owner")

    @allure.step("Meme removal check")
    def check_deleted_meme(self, id_meme):
        assert "404 Not Found" in GetOneMeme().get_only_one_meme(id_meme).text
        print('The requested URL was not found on the server.')

    @allure.step("Check for deletion of non-existent meme")
    def deleted_non_existent_meme(self, id_meme):
        assert self.deleting_meme(id_meme).status_code == 404
        print("The requested URL was not found on the server")
