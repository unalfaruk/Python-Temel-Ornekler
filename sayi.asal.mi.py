x=input("1-500 arası sayı giriniz: ")
f=2
x=int(x)

while f<x:
    a=x%f
    if a==0:
        print("Sayı asal değildir.")
        break
    else:
        f=f+1
else:
    print("Sayı asaldır.")
