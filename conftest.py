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
    print("Created")
    yield id_mem
    delete.deleting_meme(id_mem)
    print("deleted")


@pytest.fixture(scope='session')
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


@pytest.fixture(scope='class')
def new_auth_user():
    return NewUserAuthorization()


@pytest.fixture(params=[
    {"info": []},
    {"tags": {}},
    {"text": 1},
    {"url": None},
    {},  # Пустое поле
    {"meme": "items"}  # Лишнее поле которого нет

])
def invalid_data(request):
    return request.param


@pytest.fixture(params=[
    {"info": dict},
    {"tags": list},
    {"text": str},
    {"url": str}
])
def valid_data(request):
    return request.param


@pytest.fixture(params=[
    {"id": add_new_meme},
    {"info": {"colors": ["green", "white"]}},
    {"tags": ["face", "smile"]},
    {"text": "I love memes"},
    {"url": "https://miro.medium.com/v2/resize:fit:1200/1*OkVxoXBTygSKB8K-zbB7uQ.jpeg"},
])
def valid_data_json_one_meme(request):
    return request.param


@pytest.fixture(params=[
    {
        "id": add_new_meme,
        "info": {"color": ["purple", "blue", "green", "rose"]},
        "tags": ["child", "pose", "fist"],
        "text": "im 1 of the most popular memes ever",
        "url": "https://slang.net/img/slang/lg/meme_4580.png"
    }
])
def valid_data_json_created_meme(request):
    return request.param


@pytest.fixture(params=[
    {
        "id": add_new_meme,
        "url": "https://slang.net/img/slang/lg/meme_4580.png",
        "tags": ["child", "pose", "fist"],
        "info": {"color": ["purple", "blue", "green", "rose"]},
    },
    {
        "id": add_new_meme,
        "text": "im 1 of the most popular memes ever",
        "url": "https://slang.net/img/slang/lg/meme_4580.png",
        "info": {"color": ["purple", "blue", "green", "rose"]},
    },
    {
        "id": add_new_meme,
        "text": 1234,
        "url": True,
        "tags": dict,
        "info": "is_not_dict"
    }
])
def negative_data(request):
    return request.param
