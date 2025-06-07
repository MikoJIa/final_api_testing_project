import allure
import requests
from endpoints.authorization import AuthorizeUser
from endpoints.base_endpoint import BaseEndpoint
from endpoints.create_meme import CreateMeme


class NewUserAuthorization(AuthorizeUser):

    @allure.step("Authorization another user")
    def new_authorize_user(self, body):
        self.authorize_user(body=body)
