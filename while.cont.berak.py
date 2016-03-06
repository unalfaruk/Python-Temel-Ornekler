print("Programdan çıkmak için 'Ç' basınız.")
while True:
    i=input("Karekökü alınacak rakamı giriniz: ")
    if i=="ç":
        print("Çıkış yapıldı.")
        break
    if int(i)<0:
        print("Negatif sayı.")
        continue
        #continueden sonraki while içindeki ifadeler okunmaz, başa sarılır.
    k=int(i)**(1/2)
    print("Girdinizin karekökü= ", k)
        
