def harf_notu(x):
    if x<54:
        print("FF")
    elif 54<x<59:
        print("FD")
    elif 60<x<69:
        print("DD")
    elif 70<x<74:
        print("CC")
    elif 75<x<79:
        print("CB")
    elif 80<x084:
        print("BB")
    elif 85<x<89:
        print("BA")
    elif 90<x<100:
        print("AA")

print("Çıkmak için Ç")
while 1:
    a=input("Lütfen notunuzu giriniz: ")
    if (a=="ç") or (a=="Ç"):
        print("Çıkış tamamlandı.")
        break
    else:
        a=int(a)
        harf_notu(a)
    
