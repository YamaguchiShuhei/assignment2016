import sys
import difflib
argv = sys.argv
line = open(argv[1] ,'r').read()

wordlist = line.strip().split()
dict = {}
count = 0

for word in wordlist:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
for key, value in sorted(dict.items(), key=lambda x:(x[1],x[0]), reverse=True):
    count +=1
    if(count < 11):
        print('     '+str(value), key)
