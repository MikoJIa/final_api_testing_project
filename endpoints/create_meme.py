import requests
import allure
from endpoints.base_endpoint import BaseEndpoint
from endpoints.condition_token import LiveToken


class CreateMeme(BaseEndpoint):

    @allure.step("Creating a new meme")
    def create_new_meme(self):
        body = {
            "text": "I love memes",
            "url": "https://miro.medium.com/v2/resize:fit:1200/1*OkVxoXBTygSKB8K-zbB7uQ.jpeg",
            "tags": ["face", "smile"],
            "info": {"colors": ["green", "white"]}
        }
        self.response = requests.post(url=f"{self.url}/meme", json=body, headers=self.headers)
        self.id_meme = self.response.json()['id']
        self.json_meme = self.response.json()
        return self.response

    @allure.step("Conclusion about the successful or failed creation of a meme")
    def print_text(self):
        if self.check_id_meme:
            print("Successfully")
            print(self.id_meme)
        else:
            print("No")
