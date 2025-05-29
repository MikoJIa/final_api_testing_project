import requests
from endpoints.base_endpoint import BaseEndpoint
import allure


class DeleteMeme(BaseEndpoint):

    @allure.step("Deleting meme")
    def deleting_meme(self, id_meme):
        self.response = requests.delete(url=f"{self.url}/meme/{id_meme}", headers=self.headers)
