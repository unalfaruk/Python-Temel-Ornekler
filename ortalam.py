def ort(x, y):
    z = (x+y)/2
    return z

a=input("İlk sayıyı giriniz: ")
print(a)
b=input("İkinci sayıyı giriniz: ")
print(b)
f=float(a)
r=float(b)

d = ort(f, r)
print("Ortalama: " , d)
