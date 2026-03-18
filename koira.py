class Lelu:
    def __init__(self, nimi):
        self.nimi = nimi

class Koira:
    def __init__(self, nimi, ikä, hauberks="vuh vuh"):
        # luokan muuttujat voivat olla missä tahansa järjestyksessä
        # hyvä käytäntö kuitenkin on että järjestys seuraa parametrien järjestystä
        self.ikä = ikä
        self.haukahdus = hauberks
        self.nimi = nimi
        self.lelu = ""

    def aseta_lempilelu(self, lelu):
        self.lelu = lelu

    def hauku(self):
        print(f"{self.nimi} haukkuu {self.haukahdus}")
        if self.lelu:
            print(f"Lempilelu: {self.lelu.nimi}")


class Hoitola:
    def __init__(self):
        self.koirat = []

    def lisää_koira(self, koira):
        self.koirat.append(koira)

    def poista_ensimmäinen_koira(self):
        self.koirat.remove(self.koirat[0])

    def poista_koira(self, indeksi):
        if indeksi >= 0 and indeksi < len(self.koirat):
            if self.koirat[indeksi] in self.koirat:
                self.koirat.remove(self.koirat[indeksi])

    def poista_koira(self, koira):
        if koira in self.koirat:
            self.koirat.remove(koira)

    #def poista_koira(self, nimi):
    #    for koira in self.koirat:
    #        if koira.nimi == nimi:
    #            self.koirat.remove(koira)

    def kierros(self):
        self.koirat[0].hauku()
        for koira in self.koirat:
            print(f"{koira.nimi} {koira.ikä}")
            koira.hauku()

koira = Koira("Musti", 15, "väsynyt hauk")
koira2 = Koira("Pekka", 5)
koira3 = Koira("Nipsu", 4, "nipsutus")

koira.aseta_lempilelu(Lelu("pallo"))

hoitola = Hoitola()
hoitola.lisää_koira(koira)
hoitola.lisää_koira(koira2)
hoitola.lisää_koira(koira3)

hoitola.kierros()

hoitola.poista_koira(koira)
hoitola.poista_koira(Koira("juha", 100))
#hoitola.poista_koira(0)
#hoitola.poista_koira("Musti")

print("---------")

hoitola.kierros()
