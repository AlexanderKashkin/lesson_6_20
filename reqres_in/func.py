import requests

from .req import ReqresApi
from .user import User


def generate_user_data(name: str = 'Alexey', job: str = 'QA') -> dict:
    return User(name, job).get_data()


def get_user(user_id: int) -> requests.Response:
    return ReqresApi().get_user(user_id)


def get_users(num_page: int) -> requests.Response:
    return ReqresApi().get_users(num_page)


def create_user(user_data: dict) -> requests.Response:
    return ReqresApi().create_user(user_data)


def update_user(user_data: dict, user_id: str) -> requests.Response:
    return ReqresApi().update_user(user_data, user_id)


def delete_user(user_id: str) -> requests.Response:
    return ReqresApi().delete_user(user_id)
