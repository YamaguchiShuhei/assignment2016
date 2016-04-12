i = 0;

f = open("cv000_29590.txt","r",encoding="utf-8")

for x in f:
    i += 1
    print (i,"\t",x,end=""),
f.close()
