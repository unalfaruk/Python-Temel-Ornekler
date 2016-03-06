F=open("d:/kitap.txt")
kitaplar=[]
for i in F:
	l=i.split(":")
	a=int(l[0])
	b=int(l[4])
	kitaplar.append([a,l[1],l[2],l[3],b])

print(kitaplar)
