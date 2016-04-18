import sys
import shelve
from nltk.tokenize import sent_tokenize, word_tokenize
import os
argv = sys.argv
files = os.listdir(argv[1])
files.sort()
for txt in files:
    text = open(argv[1]+txt,'r').read()
    sentence = sent_tokenize(text)
    wordlist = []
    freq = {}
    for part in sentence:
        wordlist += word_tokenize(part)
    index = shelve.open('index_shelve.db')
    count = len(index)
    for word in wordlist:
        if word in freq:
            freq[word] += 1
        elif word in index and  word not in freq:
            freq[word] = 1
        else:
            freq[word] = 1
            count += 1
            index[word] = count
    vect = [0] * len(index)
    for i in freq.keys():
        vect[index[i]-1] = freq[i]
    index.close
    for i in range(len(vect)):
        if vect[i] != 0:
            print(str(i+1)+":"+str(vect[i])+" ", end="")
    print()

