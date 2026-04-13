class Avto:
    def __init__(self, znamka, hitrost=0):
        self.znamka=znamka
        self.hitrost=hitrost
    def prikazi(self):
        print(f"Avto '{self.znamka}' - hitrost: {self.hitrost} km/h")
    def pospesi(self, gas):
        self.hitrost=gas
        print(f"Avto je pospesil na {gas} km/h")
    def ustavi(self):
        if self.hitrost==0:
            print("Avto že stoji")
        else:
            self.hitrost=0
            print("Ustavil si avto.")

class Garaza:
    def __init__(self):
        self.seznam=[]
    def dodaj_avto(self, avto):
        self.seznam.append(avto)
        print("Dodal si avto")
    def prikazi_vse_avte(self):
        for a in self.seznam:
            a.prikazi()
    def pospesi_avto(self, znamka, gas):
        for a in self.seznam:
            if a.znamka==znamka:
                a.pospesi(gas)
                break
        else:print("Avto ne obstaja.")
    def ustavi_avto(self, znamka):
        for a in self.seznam:
            if a.znamka==znamka:
                a.ustavi()
                break
        else:print("Avto ne obstaja.")


audi=Avto("Audi")
bmw=Avto("BMW", 120)
audi.prikazi()
audi.pospesi(100)
garaza=Garaza()
garaza.dodaj_avto(audi)
garaza.dodaj_avto(bmw)

garaza.prikazi_vse_avte()
garaza.pospesi_avto("Audi", 30)
garaza.ustavi_avto("Audi")
garaza.ustavi_avto("Aston") #Avto ne obstaja.