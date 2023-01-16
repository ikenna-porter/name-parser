import unittest
from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble

class TestNERClient(unittest.TestCase):

    def test_get_ents_returns_dictionary_given_empty_input(self):
        model = NerModelTestDouble('eng')
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)
    
    def test_get_ents_returns_list_given_nonempty_string(self):
        model = NerModelTestDouble('eng')
        ner = NamedEntityClient(model)
        ents = ner.get_ents("New York is the biggest city in the US.")
        self.assertIsInstance(ents, dict)

