dosya=open("c:/windows/win.ini")
sozluk={}
veriler=[]
for i in dosya:
    #print(i)
    if "[" in i:
        sozluk[i]=[]
        x=str(i)
    elif "=" in i:
        #print(x)
        #print(i)
        sozluk[x].append(i)
