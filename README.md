Model 1 Machine Translation
===========================
A probabilistic foreign language translator. Based off the IBM model 1 machine translation algorithm. Uses 2 identical texts, an english corpus and a foreign corpus, then computes the probability that a specific english word maps to a specific foreign word based on our statistical model.


###To run a quick demo:
```bash
python model1.py data/short.en data/short.de data/devwords 
```


##Useage:
The script requires: 
1. An english corpus of text
2. A matching foreign corpus of text
3. A list of english words that you would like to translate. 



