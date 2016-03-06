import os
klasor="C:/Windows/System32"
klasor2="d:/sunumlar"
x=int(0)
for i in os.walk(klasor):
    print(i[0]," aranıyor")
    #print(i)
    #print(i[2])
    for k in i[2]:
        m=k.split(".")
        say=len(m)
        sayi=say-1
        #print(m[sayi])
        if m[sayi]=="ini":
            x+=1
print("İni dosyası sayısı: ", x)
    #dosya=os.path.join(klasor,i)
    #durum=os.stat(dosya)
    #if os.path.isfile(dosya):       
        #print(i," klasörüne bakılıyor.")
    
