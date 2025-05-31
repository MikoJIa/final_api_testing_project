import pickle
import allure


class BaseEndpoint:
    url = "http://167.172.172.115:52355"
    response = None
    json_meme = None
    id_meme = None
    with open('token.pkl', 'rb') as file:
        obj_token = pickle.load(file)
    headers = {
             "Authorization": f"{obj_token}"
         }

    @allure.step("Checkin the status of the code")
    def check_status_code_is_200(self):
        assert self.response.status_code == 200

    @allure.step("Checking the found id meme")
    def check_id_meme(self, id_meme):
        assert self.id_meme == id_meme

    def check_text_new_meme(self, text):
        assert self.json_meme['text'] == text
