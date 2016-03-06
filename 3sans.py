print("Faruk'un soyadı nedir?")
print("3 kere yanlış cevaplarsan kaybedersin.")
gir=""
i=1
while i<=3:
    gir=input("Cevap: ")
    if gir=="ünal":
        print("Tebrikler")
        break
    i=i+1
else:
    print("Üzgünüm.")

#while koşulu sağlanmadığında else kısmı çalışır.
