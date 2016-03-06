abone=[
    [395, "Faruk Ünal", 50],
    [1428, "Furkan Gezer", 100],
    [555, "Burhan Özkan", 75],
    [777, "Gizem Ayhan", 95]
]
guncelliste=[]
while 1:
    x=input("Abone Nu.: ")
    if x=="ç" or x=="Ç":
        print("Çıkış yaptınız.")
        for m in guncelliste:
            print(m)
        break
    for k in abone:
        if int(x)==k[0]:
            print(k[1]," İlk endeks: ",k[2])
            y=input("Son endeksi giriniz: ")
            y=int(y)
            guncelliste.append([k[0],k[1],k[2],y,(y-int(x))*1.2])
            break
        else:
            print("Abone bulunamadı.")
            break
    
