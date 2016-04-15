import sys
from nltk.tokenize import sent_tokenize, word_tokenize
argv = sys.argv
text = open(argv[1] ,'r').read()
sentence = sent_tokenize(text)
wordlist = []
dic = {}
index = {}
count = 0
for part in sentence:
    wordlist += word_tokenize(part)
for word in wordlist:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
        count += 1
        index[word] = count
print(index)

