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
from endpoints.negative_testing_update import NegativePutTest
from endpoints.negative_testing_create import NegativeCreateTest
from endpoints.expected_headers import ExpectedAuthTest
from endpoints.new_user_authorize import NewUserAuthorization


@allure.step("Creating new meme")
@pytest.fixture()
def add_new_meme(delete, create, new_auth_user):
    meme = create
    yield meme.create_new_meme().json()["id"]
    delete.deleting_meme(meme.create_new_meme().json()["id"])


@pytest.fixture()
def negative_create_meme():
    return NegativeCreateTest()


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
def updated_meme():
    return UpdateMeme()


@pytest.fixture()
def negative_test_put():
    return NegativePutTest()


@pytest.fixture()
def delete():
    return DeleteMeme()


@pytest.fixture()
def new_auth_user():
    return NewUserAuthorization()
