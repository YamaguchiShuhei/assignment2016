import sys
argv = sys.argv
f = open(argv[1] ,'r')
word = argv[2]
for line in f:
    if word in line:
        print(line,end="")
f.close()
