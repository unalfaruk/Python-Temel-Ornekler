gir= ""
while(gir !="ç"):
    gir = input("Bir sayı giriniz. Çıkmak için 'ç': ")
    if(gir=="ç"):
        print("Program sonlandı.")
    else:
        gir=float(gir)
        print("Girdinizin karekökü: ", gir**(1/2))
        
