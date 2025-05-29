import pytest


USER_AUTH = {
    "name": "Mikola"
}


def test_authorize_user(authorization, token):
    name = USER_AUTH['name']
    if token.check_live_token(name) is True:
        token.check_text_token_confirmation()
    else:
        authorization.authorize_user(USER_AUTH)
        authorization.check_status_code_is_200()


def test_get_all_meme(full_get_meme):
    full_get_meme.get_all_meme()
    full_get_meme.check_status_code_is_200()


def test_one_meme(add_new_meme, get_one_meme):
    get_one_meme.get_only_one_meme(add_new_meme)
    get_one_meme.check_id_meme(add_new_meme)
    get_one_meme.check_status_code_is_200()


def test_put_meme(updated_meme, add_new_meme):
    updated_meme.put_meme(add_new_meme)
    updated_meme.check_updated_meme_text()


def test_delete_meme(delete, add_new_meme):
    delete.deleting_meme(add_new_meme)
    delete.check_status_code_is_200()
