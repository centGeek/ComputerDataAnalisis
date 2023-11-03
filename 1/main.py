import csv
from FunkcjeLiczace import *

funkcje = FunkcjeLiczace

dane = []

# 1. długość działki kielicha (ang. sepal length) [cm]
# 2. szerokość działki kielicha (ang. sepal width) [cm]
# 3. długość płatka (ang. petal length) [cm]
# 4. szerokość płatka (ang. petal width) [cm]
# 5. gatunek (ang. species):
#    0 - setosa
#    1 - versicolor
#    2 - virginica

# ładowanie danych z pliku
with open("./data.csv", newline='') as plik_csv:
    czytnik_csv = csv.reader(plik_csv)
    for wiersz in czytnik_csv:
        wiersz_float = [float(wartość) for wartość in wiersz]
        dane.append(wiersz_float)
#import klas
from Wykres1 import *
from Wykres2 import *
from HistogramySlupkowe import *

#generowanie tabel i wykresow
Wykres1.generuj_wykres(dane)
Wykres2.generuj_tabele(dane)

HistogramySlupkowe.dlugoscDzialkiKielichaHistogram(dane)
HistogramySlupkowe.szerokoscDzialkiKielichaHistogram(dane)
HistogramySlupkowe.dlugoscPlatkaHistogram(dane)
HistogramySlupkowe.szerokoscPlatkaHistogram(dane)