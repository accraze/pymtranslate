import unittest
import os
import sys

from translator import Translator, NoMatchError

english = 'pymtranslate/data/short.en'
foreign = 'pymtranslate/data/short.de'


class TestTranslationFunctions(unittest.TestCase):

    def test_EM_transitions(self):
        t = Translator()
        self.assertFalse(t.countef)  # empty object for counting mappings
        self.assertFalse(t.totalf)  # empty object
        t.train(english, foreign)
        self.assertTrue(t.transmissions)

    def test_no_match_found(self):
        t = Translator()
        self.assertFalse(t.countef)  # empty object for counting mappings
        self.assertFalse(t.totalf)  # empty object
        t.train(english, foreign)
        # self.assertEquals(t.translate('bro'), NoMatchError('no matches found'))
        self.assertRaises(NoMatchError, t.translate, 'bro')

    def test_match_found(self):
        t = Translator()
        self.assertFalse(t.countef)  # empty object for counting mappings
        self.assertFalse(t.totalf)  # empty object
        t.train(english, foreign)
        self.assertEquals(t.translate('dog'), [('der', 0.1287760647333088), ('Hund', 0.8712239352666912)])
