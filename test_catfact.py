import pytest

from catfacts import get_breeds, get_fact, get_facts


@pytest.mark.parametrize('max_length', [20, 30, 40])
def test_get_fact(max_length):
    resp = get_fact(max_length)
    assert resp.status_code == 200
    assert resp.json()['length'] <= max_length


@pytest.mark.parametrize('max_length, limit', [(20, 2), (30, 3), (40, 4)])
def test_get_facts(max_length, limit):
    resp = get_facts(max_length, limit)
    assert resp.status_code == 200
    facts = resp.json()['data']
    assert len(facts) <= limit
    for fact in facts:
        assert fact['length'] <= max_length


@pytest.mark.parametrize('limit', [20, 30, 40])
def test_get_breeds(limit):
    resp = get_breeds(limit)
    assert resp.status_code == 200
    breeds = resp.json()
    assert len(breeds) <= limit
