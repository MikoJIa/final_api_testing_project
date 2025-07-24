import pickle
import allure

import conftest
from src.enums.error_enums_global import GlobalErrorMessages


class BaseEndpoint:
    url = "http://167.172.172.115:52355"

    def __init__(self):
        self.response = None
        self.response_2 = None
        self.json_meme = None
        self.id_meme = None
        self.new_id = None

        with open('token.pkl', 'rb') as file:
            self.obj_token = pickle.load(file)
        self.headers = {
                 "Authorization": f"{self.obj_token}"
             }

        with open('id_meme.txt', 'r') as file:
            self.id_mem = int(file.read())
        # with open('id_meme_alex.txt', 'r') as file:
        #     id_mem_alex = int(file.read())

    @allure.step("Checkin the status of the code")
    def check_status_code_is_200(self):
        assert self.response.status_code == 200

    @allure.step("Checking the found id meme")
    def check_id_meme(self, id_m):
        assert self.response.json()['id'] == id_m

    @allure.step("Verifying the correctness of the text of a new meme")
    def check_text_new_meme(self, text):
        assert self.json_meme['text'] == text

    @allure.step("Code status check for failure 400")
    def check_status_code_is_400(self):
        assert self.response.status_code == 400, GlobalErrorMessages.WRONG_STATUS_CODE.value

    def check_status_code_is_401(self, expected):
        assert self.response.status_code == expected

    def check_status_code_is_403(self):
        assert self.response.status_code == 403
