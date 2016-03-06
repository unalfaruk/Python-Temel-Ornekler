ogr=[
    [395,"Faruk","ÜNAL",19],
    [1428,"Ali","GEZER",21],
    [1923,"Burhan","ÖZKAN",17],
    [1071,"Gizem","AYHAN",25],
    [1920,"Göknur","UYGUR",10]
    ]
while 1:
    nu=input("Öğrenci numarasını giriniz: ")
    if nu not in ["ç", "Ç"]:
        for k in ogr:
            if int(nu)==k[0]:
                print(k[0]," numaralı öğrencinin adı ", k[1], k[2]," yaşı ", k[3])
                break
            else:
                print(nu," numaralı öğrenci bulunamadı.")
    else:
        break
