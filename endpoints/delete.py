import requests
from endpoints.base_endpoint import BaseEndpoint
import allure


class DeleteMeme(BaseEndpoint):

    @allure.step("Deleting meme")
    def deleting_meme(self, id_meme):
        self.response = requests.delete(url=f"{self.url}/meme/{id_meme}", headers=self.headers)

    def check_status_code_is_valid(self, expected):
        if 200 == expected:
            print(f"Status code {expected}. Successfully!!!")
        elif 404 == expected:
            print(f"Status code {expected}. The requested URL was not found on the server.")

    @allure.step("Checking if a user can delete someone else's meme")
    def check_another_user_delete_meme(self, expected, name):
        if self.response.reason == 'OK':
            assert self.response.status_code == expected
        elif '403 Forbidden' in self.response.text:
            assert self.response.status_code == expected
            print(f"{self.response.status_code}: {name} - You are not the meme owner")
