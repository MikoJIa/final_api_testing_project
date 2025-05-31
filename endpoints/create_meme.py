import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


class CreateMeme(BaseEndpoint):

    def create_new_meme(self):
        body = {
            "text": "I love memes",
            "url": "https://miro.medium.com/v2/resize:fit:1200/1*OkVxoXBTygSKB8K-zbB7uQ.jpeg",
            "tags": ["face", "smile"],
            "info": {"colors": ["green", "white"]}
        }
        self.response = requests.post(url=f"{self.url}/meme", json=body, headers=self.headers)
        self.id_meme = self.response.json()['id']
        return self.response

    def print_text(self):
        print(self.id_meme)
