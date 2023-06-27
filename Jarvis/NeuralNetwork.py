import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

Stemmer = PorterStemmer()

def tokenizer(sentence):
    return nltk.word_tokenize(sentence)


def stem(word):
    return Stemmer.stem(word.lower())


def bag_of_word(tokenized_sentence,word):
    sentence_word=[stem(word) for  word in tokenized_sentence]
    bag = np.zeros(len(word),dtype=np.float32)
    for indx , w in enumerate(word):
        if w in sentence_word:
            bag[indx]=1


        



    return bag


