class Knjiga:
    def __init__(self, naslov):
        self.naslov=naslov
        self.izposojena=False
    def prikazi(self):
        print(f"Knjiga {self.naslov} - {'Na voljo' if self.izposojena==False else 'Izposojena'}")
    def izposodi(self):
        if self.izposojena==False:
            self.izposojena=True
            print("Izposodil si si knjigo")
        else:
            print("Knjiga je ze izposojena")
    def vrni(self):
        if self.izposojena==True:
            self.izposojena=False
            print("Vrnil si knjigo")
        else:
            print("Knjiga je ze na voljo")

class Knjiznica:
    def __init__(self):
        self.seznam=[]
    def dodaj_knjigo(self, knjiga):
        self.seznam.append(knjiga)
    def prikazi_knjige(self):
        for k in self.seznam:
            k.prikazi()
    def izposodi_knjigo(self, naslov):
        for k in self.seznam:
            if k.naslov==naslov:
                k.izposodi()
                break
        else: print("Knjiga ne obstaja")
    def vrni_knjigo(self, naslov):
        for k in self.seznam:
            if k.naslov==naslov:
                k.vrni()
                break
        else: print("Knjiga ne obstaja")

knjiga1=Knjiga("Harry potter")
knjiga2=Knjiga("Gospodar prstanov")
knjiga2.izposodi()
knjiga1.vrni()
knjiznica=Knjiznica()
knjiznica.dodaj_knjigo(knjiga1)
knjiznica.dodaj_knjigo(knjiga2)
knjiznica.vrni_knjigo("Gospodar prstanov")
knjiznica.prikazi_knjige()
