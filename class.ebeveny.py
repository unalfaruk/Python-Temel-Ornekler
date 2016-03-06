class Ebeveyn:
	def anne_sac(self):
		return "sarı"
	def baba_goz(self):
		return "mavi"

class dayı:
        def boy(self):
                return "uzun"

class cocuk(Ebeveyn, dayı):

        def __init__(self, adi=""):
                self.adi=adi
        def boyu(self):
                print(self.adi,"nin boyu muhtemelen",self.boy(), "olacaktır.")
        def sac_rengi(self):
                print(self.adi,"nin saç rengi muhtemelen ",self.anne_sac(), "olacaktır.")
        def goz_rengi(self):
                print(nuri.adi," nin göz rengi muhtemelen ",nuri.baba_goz(), "olacaktır.")

    
