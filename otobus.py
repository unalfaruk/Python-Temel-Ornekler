f=open("d:/otobus.txt")
x=f.read()
y=x.split("\n")
print(x)
#print(y)
koltuk=input("Koltuk numarası girin: ")
koltuk=int(koltuk)
sira=koltuk//4
artan=koltuk%4

sirayial=y[int(sira+1)]
son=sirayial.replace(" ","")
list=list(son)
list[artan]="x"
list.insert(2," ")
son="".join(list)

y[int(sira+1)]=son
print(koltuk," numaralı koltuk alınmıştır. Teşekkürler.\n")
sonhal="\n".join(y)

f.close()
a=open("d:/otobus.txt","w")
for k in sonhal:
    a.write(k)
a.close()



