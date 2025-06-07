import allure
import pytest
import requests
from endpoints.base_endpoint import BaseEndpoint


class UpdateMeme(BaseEndpoint):

    @allure.step("Meme update")
    def put_meme(self, id_meme):
        body = {
            "id": id_meme,
            "text": "im 1 of the most popular memes ever",
            "url": "https://slang.net/img/slang/lg/meme_4580.png",
            "tags": ["child", "pose", "fist"],
            "info": {"color": ["purple", "blue", "green", "rose"]}
        }
        self.response = requests.put(url=f"{self.url}/meme/{id_meme}", json=body, headers=self.headers)
        self.json_meme = self.response.json()

    @allure.step("Checking the text of the updated meme")
    def check_updated_meme_text(self):
        assert self.json_meme["text"] == "im 1 of the most popular memes ever"
