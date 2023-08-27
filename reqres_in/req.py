import json

import allure
import requests
from allure_commons.types import AttachmentType
from curlify import to_curl
from requests import sessions


def do_request(method: str, base_url: str, url: str, **kwargs) -> requests:
    current_url = base_url + url
    with allure.step(f'{method.upper()} {url}'):
        with sessions.Session() as session:
            resp = session.request(method=method, url=current_url, **kwargs)
            message = to_curl(resp.request)
            allure.attach(body=message.encode('utf8'), name='Curl',
                          attachment_type=AttachmentType.TEXT, extension='txt')
            if resp.text == '':  # в случае ответа, когда тело пустое, то падаем на json.dumps()
                allure.attach(body='{}'.encode('utf8'), name='empty_response',
                              attachment_type=AttachmentType.JSON, extension='json')
                return resp
            allure.attach(body=json.dumps(resp.json(), indent=4).encode('utf8'), name='response',
                          attachment_type=AttachmentType.JSON, extension='json')
    return resp


class ReqresApi:
    base_url = 'https://reqres.in/api'
    url_users = '/users'
    url_with_user_id = '/{user_id}'

    def get_users(self, num_page: int) -> requests:
        resp = do_request(method='get',
                          base_url=self.base_url,
                          url=self.url_users,
                          params={'page': num_page})
        return resp

    def get_user(self, user_id: int) -> requests:
        resp = do_request(method='get',
                          base_url=self.base_url,
                          url=self.url_users + self.url_with_user_id.format(user_id=user_id))
        return resp

    def create_user(self, user_data: dict) -> requests:
        resp = do_request(method='post',
                          base_url=self.base_url,
                          url=self.url_users,
                          data=user_data)
        return resp

    def update_user(self, user_data: dict, user_id: str) -> requests:
        resp = do_request(method='put',
                          base_url=self.base_url,
                          url=self.url_users + self.url_with_user_id.format(user_id=user_id),
                          data=user_data)
        return resp

    def delete_user(self, user_id: str) -> requests:
        resp = do_request(method='delete',
                          base_url=self.base_url,
                          url=self.url_users + self.url_with_user_id.format(user_id=user_id))
        return resp
