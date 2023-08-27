import pytest

from reqres_in import create_user, generate_user_data, get_user, get_users, update_user, delete_user


@pytest.mark.parametrize('num_page, status_code', [(1, 200),
                                                  (23, 200)])
def test_get_users(num_page, status_code):
    assert get_users(num_page=num_page).status_code == status_code


@pytest.mark.parametrize('user_id, status_code', [(1, 200),
                                                  (23, 404)])
def test_get_user(user_id, status_code):
    resp = get_user(user_id)
    assert resp.status_code == status_code


def test_create_user():
    user_data = generate_user_data()
    resp = create_user(user_data)
    assert resp.status_code == 201
    assert user_data['name'] == resp.json()['name']
    assert user_data['job'] == resp.json()['job']


def test_update_user():
    resp_create_user = create_user(generate_user_data())
    assert resp_create_user.status_code == 201
    id_user = resp_create_user.json()['id']
    user_data_new = generate_user_data(name='Alexander',
                                       job='Teacher')

    resp_update_user = update_user(user_data_new, id_user)
    assert resp_update_user.status_code == 200
    assert user_data_new['name'] == resp_update_user.json()['name']
    assert user_data_new['job'] == resp_update_user.json()['job']


def test_delete_user():
    resp_create_user = create_user(generate_user_data())
    assert resp_create_user.status_code == 201
    id_user = resp_create_user.json()['id']

    assert delete_user(id_user).status_code == 204
