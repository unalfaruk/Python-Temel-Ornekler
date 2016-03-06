class secim:
    def __init__(self, adi="",secenekler=None):
        self.adi=adi
        self.secenekler=secenekler
    def __repr__(self):
        eleman="<select name='%s'>\n" %self.adi
        for s in self.secenekler:
            eleman=eleman+"<option value='%s'>%s</option>\n" %(str(s[0]), str(s[1]))
        eleman=eleman+"</select>"
        return eleman

secim_kutusu=secim("renk", [(1, "Mavi"),(2, "Sarı")])
