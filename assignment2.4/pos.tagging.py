import sys
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import SennaTagger
tagger = SennaTagger('/usr/share/senna-v2.0')
argv = sys.argv
text = open(argv[1] ,'r').read()
sentence = sent_tokenize(text)
count = 0
for part in sentence:
    count += 1
    if count < 2:
        word = tagger.tag(part.split())
        for i in word:
            print(i)
