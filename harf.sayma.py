girdi=input("Giriniz: ")
s={}
for i in girdi:
    if i in s:
        s[i]=s[i]+1
    else:
        s[i]=1

print("İstatistik")
for i in sorted(s):
    print(i, "-->", s[i])
print("\n Boşluk dahil toplam %d çeşit harf vardır." % len(s))
