import allure
import pytest
import requests
import pickle
import conftest
from conftest import add_new_meme
from endpoints.create_meme import CreateMeme
from endpoints.base_endpoint import BaseEndpoint

USER_AUTH = {
    "name": "Mikola"
}
ANOTHER_USER_AUTH = {
    "name": "Alex"
}
body = {
    "text": "I love memes",
    "url": "https://miro.medium.com/v2/resize:fit:1200/1*OkVxoXBTygSKB8K-zbB7uQ.jpeg",
    "tags": ["face", "smile"],
    "info": {"colors": ["green", "white"]}
}
id_mem = BaseEndpoint.id_mem
id_mem_alex = BaseEndpoint.id_mem_alex


@allure.feature("Authorize")
@allure.story("Authorization")
def test_authorize_user(authorization, token):
    authorization.authorize_user(USER_AUTH)
    authorization.check_status_code_is_200()


@allure.feature("live token")
@allure.story("Checking token actuality")
def test_live_token(token):
    name = USER_AUTH['name']
    token.check_live_token(name)
    token.check_text_token_confirmation(name)


@allure.feature("Meme")
@allure.story("Create meme")
def test_created_meme(create):
    # id_mem = create.create_new_meme(body).json()['id']
    # create.check_id_meme(id_mem)
    create.create_new_meme(body)
    create.check_body_text()


@allure.feature("Negative meme's")
@allure.story("Create negative meme")
@pytest.mark.parametrize(
    'param_body, expected',
    [
        ({
             "text": "Типичный зумер в офисе",
             "url": "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_679e6cfac2817216f51a8f30_679f76b2c07b444f32dc509c/scale_1200",
             "tags": {"cat": "women"},
             "info": {"color": ["white", "green", "black"]}
         }, 400),
        ({
             "text": "Типичный зумер в офисе",
             "url": "https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_679e6cfac2817216f51a8f30_679f76b2c07b444f32dc509c/scale_1200",
             "info": {"color": ["white", "green", "black"]}
         }, 400)
    ])
def test_negative_create_meme(negative_create_meme, param_body, expected):
    negative_create_meme.negative_create(param_body)
    negative_create_meme.check_status_code_is_valid(expected)


@allure.feature("Meme's")
@allure.story("get all meme's")
@pytest.mark.parametrize("headers, expected",
                         [
                             (BaseEndpoint.headers, 200),
                             ({"Authorization": f"g8JSZHkO0DOUF90"}, 401)
                         ])
def test_get_all_meme(full_get_meme, headers, expected):
    full_get_meme.get_all_meme(headers)
    full_get_meme.check_status_code_is_valid(expected)
    # full_get_meme.check_status_code_is_200()


@allure.feature("Meme")
@allure.story("get one meme")
def test_one_meme(get_one_meme, add_new_meme):
    get_one_meme.get_only_one_meme(add_new_meme)
    get_one_meme.check_id_meme(add_new_meme)
    get_one_meme.check_status_code_is_200()


@allure.feature("Meme's")
@allure.story("Manipulates put meme's and negative put")
@pytest.mark.parametrize(
    'parameters_meme, expected',
    [
        ({
             "id": id_mem_alex,
             "url": "https://slang.net/img/slang/lg/meme_4580.png",
             "tags": ["child", "pose", "fist"],
             "info": {"color": ["purple", "blue", "green", "rose"]},
         }, 400),
        ({
            "id": id_mem_alex,
            "text": "im 1 of the most popular memes ever",
            "url": "https://slang.net/img/slang/lg/meme_4580.png",
            "info": {"color": ["purple", "blue", "green", "rose"]},
        }, 400),
        ({
            "id": id_mem_alex,
            "text": "im 1 of the most popular memes ever",
            "url": "https://slang.net/img/slang/lg/meme_4580.png",
            "tags": ["child", "pose", "fist"],
            "info": {"color": ["purple", "blue", "green", "rose"]},
        }, 200)
    ]
)
def test_put_meme(updated_meme, parameters_meme, expected, add_new_meme):
    #id_m = add_new_meme
    updated_meme.put_meme(id_mem_alex, parameters_meme)
    updated_meme.check_status_code_is_valid(expected)
    updated_meme.print_user_name()


@allure.feature("Meme's")
@allure.story("Deleted meme's")
def test_delete_meme(delete, add_new_meme):
    delete.deleting_meme(add_new_meme)
    delete.check_status_code_is_200()
    delete.check_deleted_meme(add_new_meme)
    delete.deleted_non_existent_meme(9999)


@allure.feature("Headers")
@allure.story("Checkin validate headers")
@pytest.mark.parametrize(
    'headers, expected',
    [
        (BaseEndpoint.headers, 200),
        ({"Authorization": "g8JSZHkO1DOUF90"}, 401)
    ]
)
def test_expected_auth_headers(auth_headers, headers, expected):
    auth_headers.to_apply_endpoint(headers)
    auth_headers.check_status_code_is_valid(expected)
    auth_headers.output_result()


@allure.feature("Meme's")
@allure.story("Another user deleted")
def test_new_auth_user_del_meme(new_auth_user, delete):
    new_auth_user.new_authorize_user(ANOTHER_USER_AUTH)
    delete.deleting_meme(id_mem)
    delete.check_another_user_delete_meme(USER_AUTH)
