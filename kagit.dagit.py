simgeler=["Karo","Maça","Sinek","Kupa"]
sayilar=[1,2,3,4,5,6,7,8,9,10,"Bacak","Kız","Papaz"]
kagitlar=[]
for i in simgeler:
    for j in sayilar:
        kagitlar.append(i+""+str(j))
kisiler=["Kişi1", "Kişi2", "Kişi3", "Kişi4"]
import random
def dagit():
    x=int(0)
    for k in kisiler:
        print(k,"\n")
        for m in kagitlar:
            x+=1
            t=random.choice(kagitlar)
            print(t)
            print(x)
            if x==13:
                break
        print("\t")
        x=0
