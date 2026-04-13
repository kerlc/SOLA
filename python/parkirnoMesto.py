class parkirnoMesto:
    def __init__(self, st, zasedeno="Prosto"):
        self.st=st
        self.zasedeno=zasedeno
        
    def prikazi(self):
        print(f"Parkirno mesto {self.st} - {self.zasedeno}")
    
    def zasedi(self):
        if self.zasedeno=="Zasedeno":
            print(f"Mesto {self.st} je že zasedeno")
        elif self.zasedeno=="Prosto":
            self.zasedeno="Zasedeno"
            print(f"Zasedel si mesto {self.st}")
        else:
            print(f"Mesto {self.st} ne obstaja")
    def sprosti(self):
        if self.zasedeno=="Zasedeno":
            self.zasedeno="Prosto"
            print(f"Parkirno mesto {self.st} je bilo sproščeno")
        elif self.zasedeno=="Prosto":
            print(f"Mesto {self.st} je že prosto.")


class Parkirisce(parkirnoMesto):
    def __init__(self, seznam=[]):
        self.seznam=seznam
    def dodaj_mesto(self, mesto):
        self.seznam.append(parkirnoMesto(mesto))
        print(f"Dodal si parkirno mesto {mesto}")
    def prikazi_seznam(self):
        #print(self.seznam)
        for p in self.seznam: p.prikazi()
    def zasedi_mesto(self, stevilka):
        for i in self.seznam:
            if i.st==stevilka:
                i.zasedi()
                break
        else:print("Mesto ne obstaja")
    def sprosti_mesto(self, stevilka):
        for i in self.seznam:
            if i.st==stevilka:
                i.sprosti()
                break
        else:print("Mesto ne obstaja")
        
pm1=parkirnoMesto(1)
pm2=parkirnoMesto(2)
pm1.prikazi()
pm1.zasedi()
pm1.sprosti()

parking=Parkirisce()
parking.dodaj_mesto(3)
parking.dodaj_mesto(4)
parking.dodaj_mesto(5)
parking.dodaj_mesto(6)
parking.dodaj_mesto(7)
parking.prikazi_seznam()
parking.zasedi_mesto(10) #Mesto ne obstaja
parking.zasedi_mesto(5)
parking.sprosti_mesto(5)