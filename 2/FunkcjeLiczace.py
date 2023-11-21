import math


class FunkcjeLiczace:
    def suma(dana, pion):
        suma = 0.0
        for wiersz in dana:
            suma += wiersz[pion]
        return suma

    def LiczenieWPionie(dana, pion, szukana):
        znaleziono = 0
        for wiersz in dana:
            if (wiersz[pion] == szukana):
                znaleziono = znaleziono + 1
        return znaleziono

    def dajKolumne(dana, pion):
        kolumna = []
        for wiersz in dana:
            if pion < len(wiersz):
                kolumna.append(wiersz[pion])
        return kolumna

    def szukajMaksimum(dana, pion):
        znaleziono = 0
        for wiersz in dana:
            if (wiersz[pion] > znaleziono):
                znaleziono = wiersz[pion]
        return znaleziono

    def szukajMinimum(dana, pion):
        znaleziono = 100
        for wiersz in dana:
            if (wiersz[pion] < znaleziono):
                znaleziono = wiersz[pion]
        return znaleziono



    def liczSredniaArytmetyczna(dana, pion):
        srednia = round(FunkcjeLiczace.suma(dana, pion) / FunkcjeLiczace.sizeOf(dana), 10)
        zsumowanie = 0.0
        for wiersz in dana:
            x = wiersz[pion] - srednia
            x = x * x
            zsumowanie = zsumowanie + x
        zsumowanie = zsumowanie / FunkcjeLiczace.sizeOf(dana)
        zsumowanie = round(math.sqrt(zsumowanie), 10)
        return srednia, zsumowanie

    def sizeOf(dana):
        size = 0
        for _ in dana:
            size += 1
        return size


