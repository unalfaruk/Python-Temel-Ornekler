abone={
    "342":["Melike Başer","51"],
    "624":["Ahmet Arıyan","67"],
    "173":["Selim Yıldırım","31"],
    "234":["Mustafa Akgün","89"],
    "512":["Aybüke Çoban","12"]
    }
for a in sorted(abone.keys()):
    print(a,":", end="")
    for u in enumerate(abone[a]):
        print(u[0]+1,u[1]," ",end="") #enumerate komutu örneğin 342 için "0,melike bşaer, 51"
    print()                             #listesi oluşturdu u[0]+1 ile 0 ı 1 yaptık.
