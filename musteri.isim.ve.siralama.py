musteriler=[]
mus=musteriler
a=input("Kaç müşteri girilecek? :")
i=0
a=int(a)
i=int(i)
while i<=a:
    b=input("Müşteri ismi giriniz: ")
    mus.append(b)
    i=i+1
    
mus.sort()

for isim in musteriler:
    print(isim)

