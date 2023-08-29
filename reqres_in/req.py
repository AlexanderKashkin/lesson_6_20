import requests

from do_request import do_request


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
