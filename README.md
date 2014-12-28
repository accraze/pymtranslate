pymtranslate <img src="https://travis-ci.org/accraze/model1NLP.svg?branch=master"/>
===========================
A probabilistic foreign language translator. Based off the IBM model 1 machine translation algorithm. Uses 2 identical texts, an english corpus and a foreign corpus, then computes the probability that a specific english word maps to a specific foreign word based on our statistical model.


###Try it out:
```bash
$ git clone https://github.com/accraze/pymtranslate.git 
$ cd pymtranslate
$ python translator.py data/short.en data/short.de data/devwords 

```


##Useage:
The script requires:
 
1. An english corpus of text
2. A matching foreign corpus of text
3. A list of english words that you would like to translate. 

To run the script use the following syntax:
```
python translator.py <english corpus> <foreign corpus> <list of words to translate>
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

###Notes:
There are various sized english/german corpus files provided in the data folder. Make sure you use the same sized files (i.e. 2kcorpus.en, 2kcorpus.de) otherwise your results will be skewed. Also remember, the larger the corpus you are trying to crunch, the more resources will be eaten up by your CPU. Machine Translation can be a RAM-intensive task, however you can often get more meaningful results with a larger corpus.



