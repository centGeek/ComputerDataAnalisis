import numpy as np
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

    def sortowanie_babelkowe(lista):
        n = len(lista)
        for i in range(n):
            zamiana = False

            for j in range(0, n - i - 1):

                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    zamiana = True

            if not zamiana:
                break

        return list
    def liczSredniaArytmetyczna(dana, pion):
        wartosci = [wiersz[pion] for wiersz in dana]
        srednia = round(np.mean(wartosci), 2)
        odchylenie_std = round(np.std(wartosci), 2)
        return srednia, odchylenie_std

    def sizeOf(dana):
        size = 0
        for _ in dana:
            size += 1
        return size

    def percentage(dana, pion, szukana):
        return (LiczenieWPionie(dana, pion, szukana)) * 100 / sizeOf(dana)

