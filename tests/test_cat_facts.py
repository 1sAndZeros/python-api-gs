from lib.cat_facts import *
from unittest.mock import Mock

def test_provide():
    req_mock = Mock()
    res_mock = Mock()
    res_mock.json.return_value = {"fact":"A cat's normal temperature varies around 101 degrees Fahrenheit.","length":64}
    req_mock.get.return_value = res_mock
    cat_facts = CatFacts(req_mock)
    assert cat_facts.provide() == "Cat fact: A cat's normal temperature varies around 101 degrees Fahrenheit."
