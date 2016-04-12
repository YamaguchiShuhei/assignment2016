import sys
argv = sys.argv
f = open(argv[1])
for line in f:
    print(line,end="")
f.close()

