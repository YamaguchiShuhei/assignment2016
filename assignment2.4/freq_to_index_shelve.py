import sys
import shelve
from nltk.tokenize import sent_tokenize, word_tokenize
argv = sys.argv
text = open(argv[1] ,'r').read()
sentence = sent_tokenize(text)
wordlist = []
freq = {}
count = 0
for part in sentence:
    wordlist += word_tokenize(part)
index = shelve.open('index_shelve.db')
for word in wordlist:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
        count += 1
        index[word] = count
index.close()
