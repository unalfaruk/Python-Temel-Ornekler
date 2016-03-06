yerler=["Bolu","İnebolu","Yozgat","Manavgat","Çanakkale","Çan","Tirebolucuk","Kırıkkale"]
def ara(kelime, altkelime):
	if altkelime[0]=="*":
		kucuk=kelime.lower()
		if kucuk.endswith(altkelime[1:].lower()):
			return kelime
	else:
		if kelime.lower()==altkelime:
			return kelime
def bul(altkelime):
    for u in yerler:
        r=ara(u, altkelime)
        if r: print(r)

aranacak=input("Yerleşim yeri: ")
bul(aranacak)
