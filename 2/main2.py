import csv
from WykresyPunktowe import *
dane = []

with open("./data.csv", newline='') as plik_csv:
    czytnik_csv = csv.reader(plik_csv)
    for wiersz in czytnik_csv:
        wiersz_float = [float(wartość) for wartość in wiersz]
        dane.append(wiersz_float)

    WykresyPunktowe.policzPudła(dane, 0, 1, "Długość działki kielicha (cm)", "Szerokość działki kielicha (cm)")
    WykresyPunktowe.policzPudła(dane, 0, 2, "Długość działki kielicha (cm)", "Długość płatka (cm)")
    WykresyPunktowe.policzPudła(dane, 0, 3, "Długość działki kielicha (cm)", "Szerokość płatka (cm)")
    WykresyPunktowe.policzPudła(dane, 1, 2, "Szerokość działki kielicha (cm)", "Długość płatka (cm)")
    WykresyPunktowe.policzPudła(dane, 1, 3, "Szerokość działki kielicha (cm)", "Szerokość płatka (cm)")
    WykresyPunktowe.policzPudła(dane, 2, 3, "Długość płatka (cm)", "Szerokość płatka (cm)")
