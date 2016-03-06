abone=[
    [395, "Faruk Ünal", 50],
    [1428, "Furkan Gezer", 100],
    [555, "Burhan Özkan", 75],
    [777, "Gizem Ayhan", 95]
]
F=open("d:/abonesu.csv","w")
for k in abone:
    F.write(str(k[0])+","+str(k[1])+","+str(k[2])+"\n")
print("Tamam")
F.close()
