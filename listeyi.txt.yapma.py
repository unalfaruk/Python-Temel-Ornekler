F=open("d:/abone.txt","w")
abone=[
    [395,"Faruk ÜNAL", 51],
    [1428,"Furkan GEZER", 47],
    [148, "Burhan ÖZKAN", 77]
]
for a in abone:
    for i in a:
        F.write(str(i)+":")
    F.write("\n")
F.close()
