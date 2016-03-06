isimler=[]

def sirala():
    sorted(isimler)
    for i in isimler:
        print(i)
    

x=input("Kaç değer gireceksiniz?")
a=0
while int(a)<int(x):
    a+=1
    b=input("İsim gir: ")
    isimler.append(b)
