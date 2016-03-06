musteriler=[]
x=input("Müşteri Adı: ")
y=input("Müşteri Adı: ")
z=input("Müşteri Adı: ")

mus=musteriler
mus.append(x)
mus.append(y)
mus.append(z)
mus.sort()

for isim in musteriler:
    print(isim)
