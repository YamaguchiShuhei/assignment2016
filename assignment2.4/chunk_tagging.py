import sys
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import SennaChunkTagger
chktagger = SennaChunkTagger('/usr/share/senna-v2.0')
argv = sys.argv
text = open(argv[1] ,'r').read()
sentence = sent_tokenize(text)
count = 0
word2 = []
for part in sentence:
    count += 1
    if count < 2:
        word = word_tokenize(part)
word1 = chktagger.tag(word)
for i in range(len(word1)):
    if "-" in word1[i][1]:
        word2 = word2 + [[word1[i][0],word1[i][1].split("-")]]
    else:
        word2 = word2 + [[word1[i][0],[word1[i][1],word1[i][1]]]]
for i in range(len(word2)):
    if i == 0:
        print(word2[i][0]+" ", end="")
    else:
        if (word2[i][1][1] == word2[i-1][1][1] and word2[i][1][1] != "O"):
            print(word2[i][0]+" ", end="")
        elif (word2[i][1][1] != word2[i-1][1][1]):
            if(word2[i][1][1] == "O"):
                print(" "+word2[i-1][1][1])
            elif(word2[i-1][1][1] == "O"):
                print(word2[i][0]+" ", end="")
            else:
                print(" "+word2[i-1][1][1])
                print(word2[i][0]+" ", end="")

