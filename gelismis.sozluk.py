sozluk={
    "bald":["dazlak,kel"],
    "daze":["göz kamaştırmak, büyülemek"],
    "adhere":["yapışmak"]
    }
sozluk["daze"].append("şaşkınlık")
sozluk["bald"]=sozluk["bald"]+["sade","aşikar","besbelli"]

for a in sorted(sozluk.keys()):
    print (a,":",end="")
    for u in enumerate(sozluk[a]):
        print(u[0]+5,u[1]," ",end="")
    print()
    
