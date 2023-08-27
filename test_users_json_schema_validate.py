import json

import pytest
from jsonschema.validators import validate

from reqres_in import create_user, delete_user, generate_user_data, get_user, get_users, update_user


@pytest.mark.parametrize('num_page, status_code', [(1, 200),
                                                   (23, 200)])
def test_validate_json_users(num_page, status_code):
    with open('json_schema/users.json') as file:
        schema = json.loads(file.read())

    validate(get_users(num_page=num_page).json(), schema)


@pytest.mark.parametrize('user_id, status_code', [(1, 200)])
def test_validate_json_user(user_id, status_code):
    with open('json_schema/user.json') as file:
        schema = json.loads(file.read())

    validate(get_user(user_id).json(), schema)


def test_validate_json_create_user():
    user_data = generate_user_data()

    with open('json_schema/create_user.json') as file:
        schema = json.loads(file.read())

    validate(create_user(user_data).json(), schema)


def test_validate_json_update_user():
    resp_create_user = create_user(generate_user_data())
    assert resp_create_user.status_code == 201
    id_user = resp_create_user.json()['id']
    user_data_new = generate_user_data(name='Alexander',
                                       job='Teacher')

    with open('json_schema/update_user.json') as file:
        schema = json.loads(file.read())

    validate(update_user(user_data_new, id_user).json(), schema)


def test_validate_resp_delete_user():
    resp_create_user = create_user(generate_user_data())
    assert resp_create_user.status_code == 201
    id_user = resp_create_user.json()['id']

    assert delete_user(id_user).text == ''
