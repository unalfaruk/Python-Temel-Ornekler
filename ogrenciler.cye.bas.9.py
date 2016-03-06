ogrenciler=[]
a=1
a=int(a)
while 1:
    print("Çıkmak için öğrenci adını girme kısmında Ç ye basınız.")
    x=input("Öğrencinin adını giriniz: ")
    if x=="Ç" or x=="ç":
        print("Çıkış yapıldı")
        ogrenciler.sort()
        for sira in ogrenciler:
            print(sira)
        break
    y=input("Öğrencinin soyadını giriniz: ")
    z=input("Öğrencinin telefon numarasını giriniz: ")
    ogrenciler.append([y,x,a,z])
    a=a+1
ogrenciler.sort()
