from FunkcjeLiczace import *
import matplotlib.pyplot as plt

class WykresyPunktowe:
    def policzPudła(dane, pion_x, pion_y, xlabel, ylabel):

        dane_z_pion_x, dane_z_pion_y, wynik, x_av, x_odch, y_av, y_odch  = WykresyPunktowe.liczymy_r(dane, pion_x, pion_y)

        #rownanie regresji
        x_min, x_max = FunkcjeLiczace.szukajMinimum(dane, pion_x), FunkcjeLiczace.szukajMaksimum(dane, pion_x)
        y_min, y_max = FunkcjeLiczace.szukajMinimum(dane, pion_y), FunkcjeLiczace.szukajMaksimum(dane, pion_y)
        a = wynik * (y_odch / x_odch)
        b = y_av - a * x_av

        WykresyPunktowe.narysujPudła(dane_z_pion_x, dane_z_pion_y, x_min, x_max, y_min, y_max, a, b, wynik, xlabel, ylabel)

    def narysujPudła(pion_x, pion_y, x_min, x_max, y_min, y_max, a, b, wynik, xlabel, ylabel):

        plt.scatter(pion_x, pion_y, c=pion_x, cmap='viridis')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.plot([x_min, x_max], [a * x_min + b, a * x_max + b], color='blue', label=f"y = {round(a, 1)}x + {round(b, 1)}")
        if round(b, 1) > 0:
            wyrazenie = "+"
        else:
            wyrazenie = "-"

        plt.title(f"r = {wynik:.2f}; y = {round(a, 1)}x {wyrazenie} {abs(round(b, 1))}")
        plt.xticks()


        plt.xlim(x_min-0.4, x_max+0.2)
        plt.ylim(y_min-0.2, y_max+0.2)

        plt.show()


    def liczymy_r(dane, pion_x, pion_y):
        n = FunkcjeLiczace.sizeOf(dane)

        x_av, x_odch = FunkcjeLiczace.liczSredniaArytmetyczna(dane, pion_x)
        y_av, y_odch = FunkcjeLiczace.liczSredniaArytmetyczna(dane, pion_y)

        sum = 0
        for wiersz in dane:
            lewy = wiersz[pion_x] * wiersz[pion_y]
            prawy = (x_av * y_av)
            sum += lewy - prawy
        sum_n = sum / n

        dane_z_pion_x = FunkcjeLiczace.dajKolumne(dane, pion_x)
        dane_z_pion_y = FunkcjeLiczace.dajKolumne(dane, pion_y)

        wynik = sum_n / (x_odch * y_odch)
        return dane_z_pion_x, dane_z_pion_y, wynik, x_av, x_odch, y_av, y_odch

