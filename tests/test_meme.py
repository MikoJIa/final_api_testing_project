import allure
import pytest
import requests
import pickle
import conftest
from conftest import add_new_meme
from endpoints.create_meme import CreateMeme
from endpoints.base_endpoint import BaseEndpoint
from all_test_data.test_data import valid_data_list, valid_data_json_one_meme_list
from all_test_data.test_data import invalid_data_list, valid_data_json_created_meme_list, negative_data_list
import itertools

body = {
    "info": {"colors": ["green", "white"]},
    "tags": ["face", "smile"],
    "text": "I love memes",
    "url": "https://miro.medium.com/v2/resize:fit:1200/1*OkVxoXBTygSKB8K-zbB7uQ.jpeg",

}
USER_AUTH = {
    "name": "Mikola"
}
ANOTHER_USER_AUTH = {
    "name": "Alex"
}
OBJECT_TOKEN = BaseEndpoint().obj_token
id_mem = BaseEndpoint().id_mem


@allure.feature("Authorize")
@allure.story("Authorization")
def test_authorize_user(authorization):
    authorization.authorize_user(USER_AUTH)
    authorization.check_status_code_is_200()
    authorization.checking_created_token()
    authorization.checking_token_user_name(USER_AUTH['name'])


@allure.feature("live token")
@allure.story("Checking token actuality")
def test_live_token(token):
    name1 = USER_AUTH['name']
    name2 = ANOTHER_USER_AUTH['name']
    token.check_live_token(name1)
    token.check_text_token_confirmation(name1, name2)


@allure.feature("Meme")
@allure.story("Create meme")
@pytest.mark.parametrize('valid_data', valid_data_list)
def test_created_meme(create, valid_data, auth_headers):
    create.create_new_meme(body)
    create.check_body_data(valid_data)
    create.check_user_name_meme(USER_AUTH['name'])


@allure.feature("Negative meme's")
@allure.story("Create negative meme")
@pytest.mark.parametrize('invalid_data', invalid_data_list)
def test_negative_create_meme(negative_create_meme, invalid_data):
    negative_create_meme.negative_create(invalid_data)
    negative_create_meme.check_status_code_is_400()
    negative_create_meme.invalid_data_typs()


@allure.feature("Meme's")
@allure.story("get all meme's")
def test_get_all_meme(full_get_meme):
    full_get_meme.get_all_meme()
    full_get_meme.check_response_json()
    full_get_meme.check_length_response()
    full_get_meme.check_structure_meme()


@allure.feature("Negative meme's")
@allure.story("get all negative meme's")
@pytest.mark.parametrize(
    "headers, expected",
    [
        ({"a": "b"}, 401),
        ({"Authorization": "g8JSZHkO0DOUF90"}, 401),
        ({"outhorization": f'{OBJECT_TOKEN}'}, 401)
    ])
def test_get_all_meme_negative(full_get_meme, headers, expected):
    full_get_meme.get_all_meme(headers)
    full_get_meme.check_status_code_is_401(expected)
    full_get_meme.error_responses()


@allure.feature("Meme")
@allure.story("get one meme")
@pytest.mark.parametrize('valid_data_json_one_meme', valid_data_json_one_meme_list)
def test_one_meme(get_one_meme, add_new_meme, valid_data_json_one_meme):
    get_one_meme.get_only_one_meme(add_new_meme)
    get_one_meme.check_status_code_is_200()
    get_one_meme.check_content_type_is_json()
    get_one_meme.check_id_meme(add_new_meme)
    if 'id' in valid_data_json_one_meme and callable(valid_data_json_one_meme['id']):
        valid_data_json_one_meme['id'] = add_new_meme
    get_one_meme.check_meme_data(valid_data_json_one_meme)


@allure.feature("Meme")
@allure.story("get non-existent meme")
def test_nonexistent_meme(get_one_meme):
    invalid_id = 00000
    get_one_meme.get_only_one_meme(invalid_id)
    get_one_meme.check_status_code_is_404()


two_pairs_data = list(
    itertools.product(valid_data_json_created_meme_list, valid_data_json_one_meme_list)
)


@allure.feature("Meme's")
@allure.story("Manipulates put meme's")
@pytest.mark.parametrize(
    'valid_data_json_created_meme, valid_data_json_one_meme',
    two_pairs_data
)
def test_put_meme(updated_meme, valid_data_json_created_meme, add_new_meme, valid_data_json_one_meme):
    if "id" in valid_data_json_created_meme and callable(valid_data_json_created_meme['id']):
        valid_data_json_created_meme['id'] = add_new_meme
    elif "id" in valid_data_json_one_meme and callable(valid_data_json_one_meme['id']):
        valid_data_json_one_meme['id'] = add_new_meme
    updated_meme.put_meme(add_new_meme, valid_data_json_created_meme)
    updated_meme.check_status_code_is_200()
    updated_meme.check_data_updated_meme(add_new_meme, valid_data_json_one_meme)


@allure.feature("Meme's")
@allure.story("Negative_put_meme's")
@pytest.mark.parametrize('negative_data', negative_data_list)
def test_negative_put_meme(negative_update_meme, negative_data, add_new_meme):
    if "id" in negative_data and callable(negative_data['id']):
        negative_data['id'] = add_new_meme
    negative_update_meme.put_negative(id_mem, negative_data)
    negative_update_meme.check_negative_data_update_meme_expected(404)


@allure.feature("Meme's")
@allure.story("Deleted meme's")
def test_delete_meme(delete, add_new_meme, get_one_meme):
    delete.deleting_meme(add_new_meme)
    get_one_meme.get_only_one_meme(add_new_meme)
    get_one_meme.check_status_code_is_404()


@allure.feature("Meme's")
@allure.story("Deleting a non-existent meme")
def test_delete_non_existent_meme(delete, get_one_meme):
    delete.deleted_non_existent_meme(get_one_meme.checking_non_existent_meme_id())


@allure.feature("Headers")
@allure.story("Checkin validate headers")
@pytest.mark.parametrize(
    'headers, expected',
    [
        ({"Authorization": "g8JSZHkO1DOUF90"}, 401),
        ({"Content-type": "application/json"}, 401)
    ]
)
def test_expected_auth_headers(auth_headers, headers, expected):
    auth_headers.to_apply_endpoint(headers)
    auth_headers.check_status_code_is_401(expected)
    auth_headers.output_result()


# @allure.feature("Meme's")
# @allure.story("Another user deleted")
# def test_new_auth_user_del_meme(new_auth_user, delete, create):
#     pass
