class secim:
    def __init__(self, adi="",secenekler=None, secili=None):
        self.adi=adi
        self.secenekler=secenekler
        self.secili=secili

    def css(self):
        csssecim="secimCSS"
        self.css=csssecim
        
    def __repr__(self):
        eleman="<select name='%s' class='%s'>\n" %(self.adi, self.css)

        for s in self.secenekler:
            secim=' selected' if str(self.secili)==str(s[0]) else ''
            eleman=eleman+"<option value='%s'%s>%s</option>\n" %(str(s[0]), secim, str(s[1]))
        eleman=eleman+"</select>"
        return eleman
    
        
