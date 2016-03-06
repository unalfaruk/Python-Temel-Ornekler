f=open("c:/ders.txt","r")
s=f.read()
k=s.split()
m={}
for i in k:
    if i in m:
        m[i]=m[i]+1
    else:
        m[i]=1
print("İSTATİSTİKLER")
for i in sorted(m):
    print(i, "-->", m[i])
print("\nBoşluk dahil toplam %d çeşit harf vardır." % len(m))
