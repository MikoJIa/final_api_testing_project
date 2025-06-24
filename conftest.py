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
from endpoints.new_user_authorize import NewUserAuthorization
from endpoints.base_endpoint import BaseEndpoint
from endpoints.negative_created_meme import NegativeCreateMeme

body = BaseEndpoint().body


@allure.step("Creating new meme")
@pytest.fixture()
def add_new_meme(delete, create, new_auth_user):
    meme = create
    id_mem = meme.create_new_meme(body).json()["id"]
    yield id_mem
    delete.deleting_meme(id_mem)


@pytest.fixture()
def auth_headers():
    return ExpectedAuthTest()


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
def negative_create_meme():
    return NegativeCreateMeme()


@pytest.fixture()
def updated_meme():
    return UpdateMeme()


@pytest.fixture(scope='module')
def delete():
    return DeleteMeme()


@pytest.fixture(scope='session')
def new_auth_user():
    return NewUserAuthorization()
