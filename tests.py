import unittest
import os
import sys
# sys.path.append('..')
from translator import Translator

english  = 'data/short.en'
foreign  = 'data/short.de'
wordList = 'data/devwords'

class TestTranslationFunctions(unittest.TestCase):	

	
	def test_init(self):
		t = Translator(['',english, foreign, wordList])
		self.assertIn('the dog', t.en_dict)
		self.assertIsNot(t.en_words, [])
		self.assertIn('le chien', t.de_dict)
		self.assertIsNot(t.de_words, [])

	def test_tef_init(self):
		t = Translator(['',english, foreign, wordList])
		self.assertFalse(t.transmissions)# empty object
		t.initTef()
		self.assertEquals(t.transmissions, {'bus': {"l'": 0.5, 'autobus': 0.5}\
			, 'the': {"l'": 0.2, 'chien': 0.2, 'le': 0.2, 'autobus': 0.2, 'chat': 0.2}, \
			'dog': {'chien': 0.5, 'le': 0.5}, 'cat': {'le': 0.5, 'chat': 0.5}})# contains probable matches

	def test_EM_transitions(self):
		t = Translator(['',english, foreign, wordList])
		self.assertFalse(t.countef)# empty object for counting mappings
		self.assertFalse(t.totalf)# empty object
		t.initTef()
		t.iterateEM(10)
		self.assertTrue(t.transmissions)
		#self.assertTrue(t.totalf)


