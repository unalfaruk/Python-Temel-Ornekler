f=open("d:/rehber.txt")
liste=[]

    
for k in f:
    ks=k.strip()
    bul=ks.find("\x00")
    if bul==-1:
        km=ks.split()
    else:
        km=ks.split(chr(0))
    
    liste.append([km[0],km[1],km[2]])

if len(liste)==0:
    print("Boş. Çıkmak için Ç bas")
    yeni=input("Kayıt eklemek için K basınız: ")
    if yeni=="ç" or yeni=="Ç":
        print("Çıkış yaptınız.")
        f.close()        
    elif yeni=="k" or yeni=="K":        
        ad=input("İsim giriniz: ")
        soyad=input("Soyisim giriniz: ")
        num=input("Numara giriniz: ")
        liste.append([ad,soyad,num])
        #veri=ad,"%s",soyad,"%s",num % (chr(0))
        veri="{0}{1}{2}{1}{3}{1}\n".format(ad,chr(0),soyad,num)
        f.close()
        f=open("d:/rehber.txt","a")
        f.write(veri)
        print("Kayıt yapıldı.")
        f.close()
            
    
else:
    
    x=input("Adı giriniz: ")
    for isim in liste:
        
        if x==isim[0]:
            print(isim[0]," ",isim[1]," \t",isim[2])
            break
    else:   
        print("İsim bulunamadı. Çıkmak için Ç ye basınız")
        y=input("Kayıt eklemek için K giriniz: ")
        if y=="ç" or y=="Ç":
            print("Çıkış yaptınız")
            
        elif y=="k" or y=="K":
            ad=input("İsim giriniz: ")
            soyad=input("Soyisim giriniz: ")
            num=input("Numara giriniz: ")
            liste.append([ad,soyad,num])
            #veri=ad,"%s",soyad,"%s",num % (chr(0))
            veri="{0}{1}{2}{1}{3}{1}\n".format(ad,chr(0),soyad,num)
            f.close()
            f=open("d:/rehber.txt","a")
            f.write(veri)
            print("Kayıt yapıldı.")
            f.close()
        
        
        
        
    
