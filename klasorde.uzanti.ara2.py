import shutil,os
klasor="C:\\Program Files"
klasor2="d:/sunumlar"
x=int(0)
for i in os.walk(klasor):
    kaynak=[]
    #print(len(i[1]))
    #print(i[0]," aranıyor")
    #print(i)
    #print(i[2])
    for k in i[2]:
        m=k.split(".")
        say=len(m)
        sayi=say-1
        #print(m[sayi])
        if m[sayi]=="jpg":
            #os.mkdir("d:/kopyalama/jpg")
            #if len(i[1])==1:
            kaynak.append(i[0]+"/"+k)
            #os.acces("d:/kopyalama/jpg/", os.W_OK)
            for yol in kaynak:
                yol2='"'+yol+'"'
                print(yol2," kopyalandı.")
                shutil.copy(yol, "d:/kopyalama/jpg/", follow_symlinks=True)
                
                #print(kaynak)
                #yol2=os.path.join(kaynak)
                #print(yol2)
            x+=1
        
                
            #else:
                #print(i[0],"/",i[1],"/",k)
print("Jpg dosyası sayısı: ", x)
    #dosya=os.path.join(klasor,i)
    #durum=os.stat(dosya)
    #if os.path.isfile(dosya):       
        #print(i," klasörüne bakılıyor.")
    
