from .cat import Catfact


def get_fact(maximum_length: int):
    return Catfact().get_fact(maximum_length)


def get_facts(maximum_length: int, limit: int):
    return Catfact().get_facts(maximum_length, limit)


def get_breeds(limit: int):
    return Catfact().get_breeds(limit)
