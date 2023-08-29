import json

import pytest

from catfacts import get_breeds, get_fact, get_facts
from jsonschema.validators import validate


@pytest.mark.parametrize('max_length', [20, 30, 40])
def test_get_fact(max_length):
    with open('json_schema/fact.json') as file:
        schema = json.loads(file.read())

    validate(get_fact(max_length).json(), schema)


@pytest.mark.parametrize('max_length, limit', [(20, 2), (30, 3), (40, 4)])
def test_get_facts(max_length, limit):
    with open('json_schema/fact.json') as file:
        schema = json.loads(file.read())

    resp = get_facts(max_length, limit)
    assert resp.status_code == 200
    facts = resp.json()['data']
    for fact in facts:
        validate(fact, schema)


@pytest.mark.parametrize('limit', [20, 30, 40])
def test_get_breeds(limit):
    with open('json_schema/breed.json') as file:
        schema = json.loads(file.read())

    resp = get_breeds(limit)
    assert resp.status_code == 200
    breeds = resp.json()['data']
    for breed in breeds:
        validate(breed, schema)
