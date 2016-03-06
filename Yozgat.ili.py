komsu= ["Kırıkkale","Kırşehir","Nevşehir","Kayseri","Sivas","Çorum","Tokat","Amasya"]
print("Yozgat ilinin komşularını öğrenelim.")
girilen=input("Lütfen ilk harfi büyük giriniz: ")
i=0
while i<len(komsu):
    if komsu[i]==girilen:
        print("Tebrikler!", girilen, ", Yozgat iline komşudur.")
        break
    i=i+1
else:
    print("Üzgünüm!", girilen, ", Yozgat iline komşu değildir.")
