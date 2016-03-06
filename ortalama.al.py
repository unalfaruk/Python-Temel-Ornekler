def ortalama(*sayilar):
    toplam=0
    for i in sayilar:
        toplam=toplam+i

    x=len(sayilar)
    y=toplam/x
    return y
