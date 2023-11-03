import csv
import matplotlib.pyplot as plt
from FunkcjeLiczace import *


class Wykres2:

    def generuj_tabele(dane):
        maks_dlugosc_dzialki_kielicha = FunkcjeLiczace.szukajMaksimum(dane, 0)
        maks_szerokosc_dzialki_kielicha = FunkcjeLiczace.szukajMaksimum(dane, 1)
        maks_dlugosc_platka = FunkcjeLiczace.szukajMaksimum(dane, 2)
        maks_szerokosc_platka = FunkcjeLiczace.szukajMaksimum(dane, 3)

        min_dlugosc_dzialki_kielicha = FunkcjeLiczace.szukajMinimum(dane, 0)
        min_szerokosc_dzialki_kielicha = FunkcjeLiczace.szukajMinimum(dane, 1)
        min_dlugosc_platka = FunkcjeLiczace.szukajMinimum(dane, 2)
        min_szerokosc_platka = FunkcjeLiczace.szukajMinimum(dane, 3)

        dlugosc_dzialki_medi = FunkcjeLiczace.q1q2q3(dane, 0)
        szerokosc_dzialki_medi = FunkcjeLiczace.q1q2q3(dane, 1)
        dlugosc_platka_medi = FunkcjeLiczace.q1q2q3(dane, 2)
        szerokosc_platka_medi = FunkcjeLiczace.q1q2q3(dane, 3)

        print(dane[0][0])
        print(FunkcjeLiczace.suma(dane, 0))
        dlugosc_dzialki_avg = FunkcjeLiczace.liczSredniaArytmetyczna(dane, 0)
        szerokosc_dzialki_avg = FunkcjeLiczace.liczSredniaArytmetyczna(dane, 1)
        dlugosc_platka_avg = FunkcjeLiczace.liczSredniaArytmetyczna(dane, 2)
        szerokosc_platka_avg = FunkcjeLiczace.liczSredniaArytmetyczna(dane, 2)

        data = [
            ["Cecha", "Minimum", "Śr. arytmetyczna", "Mediana (Q1 - Q3)", "Maksimum"],
            ["Długość działki kielicha (cm)", min_dlugosc_dzialki_kielicha, dlugosc_dzialki_avg, dlugosc_dzialki_medi,
             maks_dlugosc_dzialki_kielicha],
            ["Szerokość działki kielicha (cm)", min_szerokosc_dzialki_kielicha, szerokosc_dzialki_avg,
             szerokosc_dzialki_medi, maks_szerokosc_dzialki_kielicha],
            ["Długość płatka (cm)", min_dlugosc_platka, dlugosc_platka_avg, dlugosc_platka_medi, maks_dlugosc_platka],
            ["Szerokość płatka (cm)", min_szerokosc_platka, szerokosc_platka_avg, szerokosc_platka_medi,
             maks_szerokosc_platka]
        ]

        # Tworzenie wykresu
        fig, ax = plt.subplots(figsize=(10, 6))
        # Tworzenie tabeli
        table = ax.table(cellText=data, loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 1.5)

        table.auto_set_column_width([0, 1, 2, 3, 4])

        ax.axis('off')

        plt.show()
