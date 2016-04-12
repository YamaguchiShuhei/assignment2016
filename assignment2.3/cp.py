import sys
argv = sys.argv
f1 = open(argv[1] ,'r')
f2 = open(argv[2] ,'w')
for line in f1:
    f2.write(line)
f1.close()
f2.close()
