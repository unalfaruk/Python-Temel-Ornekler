def denkCoz(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    delta = b**2 - (4*a*c)
    kok1 = (delta**(1/2) - b)/(2*a)
    kok2 = (-delta**(1/2) - b)/(2*a)
    print(delta)
    print(kok1)
    print(kok2)

xkare = input("xkare katsayı gir: ")
x = input("x katsayı gir: ")
sabit = input("sabiti gir: ")

d=float(xkare)
e=float(x)
f=float(sabit)

print("Denklem= ", d,"Xkare + ", e,"X + ", f)

sonuc = denkCoz(d,e,f)
