import sys
argv = sys.argv
line = open(argv[1] ,'r').read()

wordlist = line.strip().split()

for word in wordlist:
    print (word)

