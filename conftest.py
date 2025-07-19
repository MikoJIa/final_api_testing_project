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
from endpoints.expected_headers import ExpectedAuthTest
# from endpoints.new_user_authorize import NewUserAuthorization
from endpoints.base_endpoint import BaseEndpoint
from endpoints.negative_created_meme import NegativeCreateMeme
from endpoints.negative_testing_update import NegativePutTest


body = BaseEndpoint().body
USER_AUTH = {
    "name": "Mikola"
}
ANOTHER_USER_AUTH = {
    "name": "Alex"
}

base_url = BaseEndpoint.url


@allure.step("Creating new meme")
@pytest.fixture()
def add_new_meme(delete, create):
    meme = create
    id_mem = meme.create_new_meme(body).json()["id"]
    yield id_mem
    delete.deleting_meme(id_mem)


@pytest.fixture(scope='session', autouse=True)
def authorization():
    return AuthorizeUser()


@pytest.fixture()
def token():
    return LiveToken()


@pytest.fixture()
def create():
    return CreateMeme()


@pytest.fixture()
def get_one_meme():
    return GetOneMeme()


@pytest.fixture()
def full_get_meme():
    return GetAllMeme()


@pytest.fixture()
def auth_headers():
    return ExpectedAuthTest()


@pytest.fixture()
def negative_create_meme():
    return NegativeCreateMeme()


@pytest.fixture()
def updated_meme():
    return UpdateMeme()


@pytest.fixture()
def negative_update_meme():
    return NegativePutTest()


@pytest.fixture()
def delete():
    return DeleteMeme()


# @pytest.fixture(scope='class')
# def new_auth_user():
#     return NewUserAuthorization()
