import copy

import allure
import pytest
import requests

from endpoints.create_meme import CreateMeme
from endpoints.base_endpoint import BaseEndpoint


USER_AUTH = {
    "name": "Mikola"
}
ANOTHER_USER_AUTH = {
    "name": "Alex"
}
id_meme = CreateMeme().create_new_meme().json()['id']


@allure.feature("Authorize")
@allure.story("Authorization")
def test_authorize_user(authorization, token):
    name = USER_AUTH['name']
    if token.check_live_token(name) is True:
        token.check_text_token_confirmation(name)
    else:
        authorization.authorize_user(USER_AUTH)
        authorization.check_status_code_is_200()


@allure.feature("Meme")
@allure.story("Create meme")
def test_created_meme(create, add_new_meme):
    create.create_new_meme()
    create.check_id_meme(create.create_new_meme().json()['id'])
    create.print_text()


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
    negative_create_meme.create_negative(param_body)
    negative_create_meme.print_failed_text()
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
    #full_get_meme.check_status_code_is_200()


@allure.feature("Meme")
@allure.story("get one meme")
def test_one_meme(add_new_meme, get_one_meme):
    get_one_meme.get_only_one_meme(add_new_meme)
    get_one_meme.check_id_meme(add_new_meme)
    get_one_meme.check_status_code_is_200()


@allure.feature("Meme's")
@allure.story("Manipulates put meme's")
def test_put_meme(updated_meme, add_new_meme):
    updated_meme.put_meme(add_new_meme)
    updated_meme.check_updated_meme_text()


@allure.feature("Negative meme's")
@allure.story("Manipulate negative put meme's")
@pytest.mark.parametrize(
        'parameters_meme, expected',
        [
            ({
                "id": id_meme,
                "url": "https://slang.net/img/slang/lg/meme_4580.png",
                "tags": ["child", "pose", "fist"],
                "info": {"color": ["purple", "blue", "green", "rose"]},
            }, 400),
            ({
                "id": id_meme,
                "text": "im 1 of the most popular memes ever",
                "url": "https://slang.net/img/slang/lg/meme_4580.png",
                "tags": ["child", "pose", "fist"],
                "info": {"color": ["purple", "blue", "green", "rose"]},
            }, 200),
        ]
    )
def test_negative_put_meme(negative_test_put, parameters_meme, expected):
    negative_test_put.put_negative(parameters_meme, id_meme)
    negative_test_put.print_response()
    negative_test_put.check_status_code_is_valid(expected)


@allure.feature("Meme's")
@allure.story("Deleted meme's")
@pytest.mark.parametrize(
        "id_m, expected",
    [
        (999, 404),
        (id_meme, 200)
    ]
)
def test_delete_meme(delete, id_m, expected):
    delete.deleting_meme(id_m)
    delete.check_status_code_is_valid(expected)


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
@pytest.mark.parametrize(
    'id_another, expected', [
        (1300, 403),
        (id_meme, 200)
    ])
def test_new_auth_user_del_meme(new_auth_user, delete, token, id_another, expected, create):
    another_name = ANOTHER_USER_AUTH['name']
    if token.check_live_token(another_name) is True:
        token.check_text_token_confirmation(another_name)
    else:
        new_auth_user.new_authorize_user(ANOTHER_USER_AUTH)
        delete.deleting_meme(id_another)
        delete.check_another_user_delete_meme(expected, USER_AUTH)
