import pickle
import allure

import conftest
from src.enums.error_enums_global import GlobalErrorMessages


class BaseEndpoint:
    url = "http://167.172.172.115:52355"
    response = None
    response_2 = None
    json_meme = None
    id_meme = None
    new_id = None
    with open('token.pkl', 'rb') as file:
        obj_token = pickle.load(file)
    headers = {
             "Authorization": f"{obj_token}"
         }
    body = {
        "text": "I love memes",
        "url": "https://miro.medium.com/v2/resize:fit:1200/1*OkVxoXBTygSKB8K-zbB7uQ.jpeg",
        "tags": ["face", "smile"],
        "info": {"colors": ["green", "white"]}
    }
    with open('id_meme.txt', 'r') as file:
        id_mem = int(file.read())
    with open('id_meme_alex.txt', 'r') as file:
        id_mem_alex = int(file.read())

    @allure.step("Checkin the status of the code")
    def check_status_code_is_200(self):
        assert self.response.status_code == 200

    @allure.step("Checking the found id meme")
    def check_id_meme(self, id_m):
        assert self.response.json()['id'] == id_m

    @allure.step("Verifying the correctness of the text of a new meme")
    def check_text_new_meme(self, text):
        assert self.json_meme['text'] == text

    @allure.step("Checking the correct status")
    def check_status_code_is_valid(self, expected):
        assert self.response.status_code == expected

    @allure.step("Code status check for failure 400")
    def check_status_code_is_400(self, expected):
        assert self.response.status_code == expected, GlobalErrorMessages.WRONG_STATUS_CODE.value



