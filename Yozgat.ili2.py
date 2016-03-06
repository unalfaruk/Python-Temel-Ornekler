komsu= ["Kırıkkale","Kırşehir","Nevşehir","Kayseri","Sivas","Çorum","Tokat","Amasya"]
print("Yozgat ilinin komşularını öğrenelim.")
girilen=input("Lütfen ilk harfi büyük giriniz: ")
i=0

if girilen in komsu:
    print("Tebrikler!", girilen, ", Yozgat iline komşudur.")   
else:
    print("Üzgünüm!", girilen, ", Yozgat iline komşu değildir.")
