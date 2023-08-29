import requests

from do_request import do_request


class Catfact:
    base_url = 'https://catfact.ninja'
    facts = '/facts'
    fact = '/fact'
    breeds = '/breeds'

    def get_fact(self, maximum_length: int) -> requests:
        resp = do_request(method='get',
                          base_url=self.base_url,
                          url=self.fact,
                          params={'max_length': maximum_length})
        return resp

    def get_facts(self, maximum_length: int, limit: int) -> requests:
        resp = do_request(method='get',
                          base_url=self.base_url,
                          url=self.facts,
                          params={'max_length': maximum_length, 'limit': limit})
        return resp

    def get_breeds(self, limit: int) -> requests:
        resp = do_request(method='get',
                          base_url=self.base_url,
                          url=self.breeds,
                          params={'limit': limit})
        return resp
