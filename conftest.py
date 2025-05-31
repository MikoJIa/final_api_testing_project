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
from endpoints.create_meme import CreateMeme


# url = "http://167.172.172.115:52355/meme"

# headers = {
#     "Authorization": f"{AuthorizeUser.obj_token}"
# }


@allure.step("Creating new meme")
@pytest.fixture()
def add_new_meme(delete, create):
    meme = create
    yield meme.create_new_meme().json()["id"]
    delete.deleting_meme(meme.create_new_meme().json()["id"])


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
def create():
    return CreateMeme()


@pytest.fixture()
def updated_meme():
    return UpdateMeme()


@pytest.fixture()
def delete():
    return DeleteMeme()
