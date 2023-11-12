from FunkcjeLiczace import *
import matplotlib.pyplot as plt


class HistogramySlupkowe:
    def oblicz_histogram(dane, pion, krok=0.5):
        dane_pion = FunkcjeLiczace.dajKolumne(dane, pion)

        min_wartosc = FunkcjeLiczace.szukajMinimum(dane, pion)
        max_wartosc = FunkcjeLiczace.szukajMaksimum(dane, pion)
        min_wartosc = math.floor(min_wartosc)
        max_wartosc = math.ceil(max_wartosc)
        liczba_przedzialow = int((max_wartosc - min_wartosc) / krok) + 1
        przedzialy = [min_wartosc + i * krok for i in range(liczba_przedzialow)]
        histogram = [0] * (liczba_przedzialow - 1)

        for wartość in dane_pion:
            for i in range(len(przedzialy) - 1):
                if przedzialy[i] <= wartość < przedzialy[i + 1]:
                    histogram[i] += 1
                    break

        return histogram, przedzialy

    def narysujHistogram(dane, xlabel, title, pion,podanyKrok=0.5):
        ticks = []
        tick = 0.0
        histogram, przedzialy = HistogramySlupkowe.oblicz_histogram(dane, pion, podanyKrok)
        szerokosc_slupkow = [przedzialy[i + 1] - przedzialy[i] for i in range(len(przedzialy) - 1)]
        punkty_slupkow = [przedzialy[i] + szerokosc_slupkow[i] / 2 for i in range(len(przedzialy) - 1)]
        for i in range(len(przedzialy) - 1):
            tick+=podanyKrok
            ticks.append(tick)

        plt.xticks(przedzialy)
        plt.bar(punkty_slupkow, histogram, width=szerokosc_slupkow, edgecolor="white", align='center')
        plt.xlabel(xlabel)
        plt.ylabel("Liczebność")
        plt.title(title)
        plt.show()

