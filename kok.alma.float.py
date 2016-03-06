def kokAl(sayi, derece=2):
    kok = sayi**(1/derece)
    return kok

girilen = input("Karekökü alınacak sayıyı giriniz: ")
# tam sayi girmeyebilir, float komutu kullanıyoruz.
girFloat = float(girilen)
k = kokAl(girFloat)
print(k)
