import sys
from nltk.tokenize import sent_tokenize, word_tokenize
argv = sys.argv
text = open(argv[1] ,'r').read()
sentence = sent_tokenize(text)
print(sentence)


