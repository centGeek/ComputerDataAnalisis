import math

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

    def liczSredniaArytmetyczna(dana, pion):
        wartosci = [wiersz[pion] for wiersz in dana]

        srednia = round(FunkcjeLiczace.suma(dana, pion) / FunkcjeLiczace.sizeOf(dana), 2)
        odchylenie_std = 0
        zsumowanie = 0.0
        for wiersz in dana:
            x = wiersz[pion] - srednia
            x = x * x
            zsumowanie = zsumowanie + x
        zsumowanie = zsumowanie/FunkcjeLiczace.sizeOf(dana)
        zsumowanie = round(math.sqrt(zsumowanie),2)
        return srednia, zsumowanie

    def sizeOf(dana):
        size = 0
        for _ in dana:
            size += 1
        return size

    def percentage(dana, pion, szukana):
        return (FunkcjeLiczace.LiczenieWPionie(dana, pion, szukana)) * 100 / FunkcjeLiczace.sizeOf(dana)

    def sortowanie_babelkowe(lista,pion):
        n = FunkcjeLiczace.sizeOf(lista)
        for i in range(n):
            zamiana = False
            for j in range(0, n - i - 1):
                if lista[j][pion] > lista[j + 1][pion]:
                    lista[j][pion], lista[j + 1][pion] = lista[j + 1][pion], lista[j][pion]
                    zamiana = True
            if not zamiana:
                break
        return lista