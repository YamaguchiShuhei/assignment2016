import sys
from nltk.tokenize import sent_tokenize, word_tokenize
argv = sys.argv
text = open(argv[1] ,'r').read()
sentence = sent_tokenize(text)
wordlist = []
dic = {}
count = 0
for part in sentence:
    wordlist += word_tokenize(part)
for word in wordlist:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
for key, value in sorted(dic.items(), key=lambda x:(x[1],x[0]), reverse=True):
    count += 1
    if(count<11):
        print('     '+ str(value), key)
