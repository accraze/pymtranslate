pymtranslate <a href="https://travis-ci.org/accraze/pymtranslate" target="_blank"><img src="https://travis-ci.org/accraze/pymtranslate.svg?branch=master"/></a> <a href="https://pypi.python.org/pypi/pymtranslate" target="_blank"><img src="https://img.shields.io/pypi/v/pymtranslate.svg"/></a>
===========================
A probabilistic foreign language translator. Based off the IBM model 1 machine translation algorithm. Uses 2 identical texts, an english corpus and a foreign corpus, then computes the probability that a specific english word maps to a specific foreign word based on our statistical model.


### Install
Works for Python 2.7 (have not tested w/ Python 3)
```bash
$ pip install pymtranslate
```

##Useage:
The script requires:
 
1. An english corpus of text
2. A matching foreign corpus of text
3. A list of english words that you would like to translate.

Then use translate:
```
$ python
>>> from pymtranslate.translator import Translator
>>>
>>> english = 'pymtranslate/data/short.en'
>>> foreign = 'pymtranslate/data/short.de'
>>>
>>> t = Translator(english, foreign)
>>> t.initTef() # initialize transmissions
>>> t.iterateEM(10) # get expected max estimates
>>> t.translate('dog') # print probable translations

[('der', 0.1287760647333088), ('Hund', 0.8712239352666912)]
>>> t.translate('man') # print probable translations
no matches found

```

####Example English Corpus
```
the dog
the cat
the bus
```

####Example Foreign Corpus
```
le chien
le chat
l' autobus
```

####Example Translation words
```
dog
man
bus
bill
cat
```
If you attempt to translate a word that is not in our statistical model, the script will tell you that no match was found.

###Notes:
There are various sized english/foreign corpus files provided in the data folder. Make sure you use the same sized files (i.e. 2kcorpus.en, 2kcorpus.de) otherwise your results will be skewed. Also remember, the larger the corpus you are trying to crunch, the more resources will be eaten up by your CPU. Machine Translation can be a RAM-intensive task, however you can often get more meaningful results with a larger corpus.



