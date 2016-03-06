q="adi=mustafa&soyadi=baser&yas=41&il=yozgat"
veriler={}
a=q.split("&")
#print(a)
for i in a:
    z=i.split("=")
    veriler[z[0]]=z[1]
print(veriler)
    
