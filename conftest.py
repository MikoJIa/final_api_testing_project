import pickle
import allure
import pytest
import requests
from endpoints.authorization import AuthorizeUser
from endpoints.condition_token import LiveToken
from endpoints.all_meme import GetAllMeme
from endpoints.one_meme import GetOneMeme
from endpoints.delete import DeleteMeme
from endpoints.update_meme import UpdateMeme


url = "http://167.172.172.115:52355/meme"
with open('token.pkl', 'rb') as file:
    obj_token = pickle.load(file)
headers = {
    "Authorization": f"{obj_token}"
}


@allure.step("Creating new meme")
@pytest.fixture()
def add_new_meme(delete):
    body = {
        "text": "I love memes",
        "url": "https://miro.medium.com/v2/resize:fit:1200/1*OkVxoXBTygSKB8K-zbB7uQ.jpeg",
        "tags": ["face", "smile"],
        "info": {"colors": ["green", "white"]}
    }
    response = requests.post(url=url, json=body, headers=headers)
    id_meme = response.json()['id']
    yield id_meme
    delete.deleting_meme(id_meme)


@pytest.fixture()
def get_one_meme():
    return GetOneMeme()


@pytest.fixture()
def authorization():
    return AuthorizeUser()


@pytest.fixture()
def token():
    return LiveToken()


@pytest.fixture()
def full_get_meme():
    return GetAllMeme()


@pytest.fixture()
def updated_meme():
    return UpdateMeme()


@pytest.fixture()
def delete():
    return DeleteMeme()
