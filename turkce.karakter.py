ceviri={
    "ş":"s",
    "ğ":"g"
    }
x="şebeği getirin"
for i in x:
   if i in ceviri:
        y=ceviri[i]
        x=x.replace(i,y)
        #z=x.find(i)
        #print(z)
        #print(ceviri[i])
        #print(x[z])
        #x[z]==ceviri[i]
        

print(x)
