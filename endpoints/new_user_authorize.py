import allure
import requests
from endpoints.authorization import AuthorizeUser
from endpoints.base_endpoint import BaseEndpoint
from endpoints.create_meme import CreateMeme


ANOTHER_USER_AUTH = {
    "name": "Alex"
}


# class NewUserAuthorization(AuthorizeUser):
#
#     @allure.step("Authorization another user")
#     def new_authorize_user(self, body):
#         return self.authorize_user(body=body)

