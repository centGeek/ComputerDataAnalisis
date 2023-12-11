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


    def liczSredniaArytmetycznaIOdchylenie(dana, pion):
        srednia = round(FunkcjeLiczace.suma(dana, pion) / FunkcjeLiczace.sizeOf(dana), 2)
        odchylenie = 0.0
        for wiersz in dana:
            x = wiersz[pion] - srednia
            x = x * x
            odchylenie = odchylenie + x
        odchylenie = odchylenie / FunkcjeLiczace.sizeOf(dana)
        odchylenie = round(math.sqrt(odchylenie), 2)
        return srednia, odchylenie

    def sizeOf(dana):
        size = 0
        for _ in dana:
            size += 1
        return size

    def percentage(dana, pion, szukana):
        return (FunkcjeLiczace.LiczenieWPionie(dana, pion, szukana)) * 100 / FunkcjeLiczace.sizeOf(dana)

    def sortowanie_babelkowe(dane, pion):
        n = FunkcjeLiczace.sizeOf(dane)
        kolumna = FunkcjeLiczace.dajKolumne(dane, pion)
        for i in range(n):
            for j in range(0, n - i - 1):
                if kolumna[j] > kolumna[j + 1]:
                    kolumna[j], kolumna[j + 1] = kolumna[j + 1], kolumna[j]
        return [row[pion] for row in dane]


    def q1(dana, pion):
        sorted_numbers =FunkcjeLiczace.sortowanie_babelkowe(dana, pion)
        n = FunkcjeLiczace.sizeOf(sorted_numbers)
        if n % 4 == 0:
            return (sorted_numbers[n // 4 - 1] + sorted_numbers[n // 4]) / 2
        else:
            return sorted_numbers[n // 4]

    def q2(dana, pion):
        sorted_numbers =FunkcjeLiczace.sortowanie_babelkowe(dana, pion)
        n =  FunkcjeLiczace.sizeOf(sorted_numbers)
        if n % 2 == 1:
            return sorted_numbers[n // 2]
        else:
            middle1 = sorted_numbers[n // 2 - 1]
            middle2 = sorted_numbers[n // 2]
            return (middle1 + middle2) / 2

    def q3(dana, pion):
        sorted_numbers =FunkcjeLiczace.sortowanie_babelkowe(dana, pion)
        n = FunkcjeLiczace.sizeOf(sorted_numbers)

        if n % 4 == 0:
            return (sorted_numbers[3 * n // 4 - 1] + sorted_numbers[3 * n // 4]) / 2
        else:
            return sorted_numbers[3 * n // 4]

    def q1q2q3(dana, pion):
        q2_value = "{:.2f}".format(FunkcjeLiczace.q2(dana, pion))
        q1_value = "{:.2f}".format(FunkcjeLiczace.q1(dana, pion))
        q3_value = "{:.2f}".format(FunkcjeLiczace.q3(dana, pion))
        return "{} ({} - {})".format(q2_value, q1_value, q3_value)

    def sredniaodchylenie(dana, pion):
        srednia, odchylenie = FunkcjeLiczace.liczSredniaArytmetycznaIOdchylenie(dana, pion)
        sred_value = "{:.2f}".format(srednia)
        odchyl_value = "{:.2f}".format(odchylenie)
        return "{} (±{})".format(sred_value, odchyl_value)

    def dajTylkoGatunku(dane, pion, cyfraGatunku):
        kolumna = []
        for wiersz in dane:
            if pion < len(wiersz):
                if (wiersz[4] == cyfraGatunku):
                    kolumna.append(wiersz[pion])
        return kolumna
