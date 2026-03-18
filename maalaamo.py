class Auto:
    def __init__(self, väri):
        self.väri = väri

    # TODO: älä käytä tätä
    # tämä metodi ei välttämättä ole haluttu tapa vaihtaa auton väriä
    def vaihda_väri(self, uusi_väri):
        self.väri = uusi_väri

class Maalaamo:
    def maalaa(self, auto, uusi_väri):
        #auto.väri = uusi_väri
        auto.vaihda_väri(uusi_väri)

class Parkkipaikka:
    lista = []

    def lisää_auto(self, auto):
        self.lista.append(auto)

    def tulosta_autot(self):
        print(f"Parkkipaikalla on {len(self.lista)} autoa")
        for auto in self.lista:
            print(auto.väri)

    # TODO: tulee ongelmia jos tyhjä lista
    def ota_ensimmäinen_auto(self):
        auto = self.lista[0]
        self.lista.remove(auto)
        return auto

audi = Auto("sininen")

maalamo = Maalaamo()

print("alkuperäinen väri " + audi.väri)

maalamo.maalaa(audi, "hot pink")

print("uusi väri " + audi.väri)

parkkipaikka = Parkkipaikka()

parkkipaikka.tulosta_autot()

parkkipaikka.lisää_auto(audi)

parkkipaikka.tulosta_autot()

auto = parkkipaikka.ota_ensimmäinen_auto()

parkkipaikka.tulosta_autot()
maalamo.maalaa(auto, "Oranssi")

print("uusi väri (audi) " + audi.väri)
print("uusi väri (auto) " + auto.väri)
