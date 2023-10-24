import csv
import matplotlib.pyplot as plt
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

with open("./data.csv", newline='') as plik_csv:
    czytnik_csv = csv.reader(plik_csv)
    for wiersz in czytnik_csv:
        wiersz_float = [float(wartość) for wartość in wiersz]
        dane.append(wiersz_float)

setosa_count = funkcje.LiczenieWPionie(dane, 4, 0)
versicolor_count = funkcje.LiczenieWPionie(dane, 4, 1)
virginica_count = funkcje.LiczenieWPionie(dane, 4, 2)

maks_dlugosc_dzialki_kielicha = funkcje.szukajMaksimum(dane, 0)
maks_szerokosc_dzialki_kielicha = funkcje.szukajMaksimum(dane, 1)
maks_dlugosc_platka = funkcje.szukajMaksimum(dane, 2)
maks_szerokosc_platka = funkcje.szukajMaksimum(dane, 3)

min_dlugosc_dzialki_kielicha = funkcje.szukajMinimum(dane, 0)
min_szerokosc_dzialki_kielicha = funkcje.szukajMinimum(dane, 1)
min_dlugosc_platka = funkcje.szukajMinimum(dane, 2)
min_szerokosc_platka = funkcje.szukajMinimum(dane, 3)

total_count = setosa_count + versicolor_count + virginica_count
setosa_percentage = (setosa_count * 100 / total_count)
versicolor_percentage = (versicolor_count * 100 / total_count)
virginica_percentage = (virginica_count * 100 / total_count)

# dlugosc_dzialki_medi = mediana(dane, 0)
# szerokosc_dzialki_medi = mediana(dane, 1)
# dlugosc_platka_medi = mediana(dane, 2)
# szerokosc_platka_medi = mediana(dane, 3)

print(f"setosa: {setosa_count} ({setosa_percentage:.2f}%)")
print(f"versicolor: {versicolor_count} ({versicolor_percentage:.2f}%)")
print(f"virginica: {virginica_count} ({virginica_percentage:.2f}%)")
print(funkcje.sizeOf(dane))
print(round(funkcje.LiczenieWPionie(dane, 4, 1), 2))

fig, ax = plt.subplots()

x = ["setosa", "versicolor", "virginica"]
counts = [setosa_count, versicolor_count, virginica_count]
percentages = [setosa_percentage, versicolor_percentage, virginica_percentage]

ax.bar(x, counts, width=0.5, edgecolor="white", linewidth=0.7, color='red')
ax.set_ylabel("Liczba poszczególnych gatunków")
for i, v in enumerate(counts):
    ax.text(i, v + 5, f"{percentages[i]:.2f}%", ha="center", va="bottom")

plt.show()

print(dane[0][0])
print(funkcje.suma(dane, 0))
dlugosc_dzialki_avg = funkcje.liczSredniaArytmetyczna(dane, 0)
szerokosc_dzialki_avg = funkcje.liczSredniaArytmetyczna(dane, 1)
dlugosc_platka_avg = funkcje.liczSredniaArytmetyczna(dane, 2)
szerokosc_platka_avg = funkcje.liczSredniaArytmetyczna(dane, 2)
data = [
    ["Cecha", "Minimum", "Śr. arytmetyczna", "Mediana (Q1 - Q3)", "Maksimum"],
    ["Długość działki kielicha (cm)", min_dlugosc_dzialki_kielicha, dlugosc_dzialki_avg, "5.80 (5.10 - 6.40)", "7.90"],
    ["Szerokość działki kielicha (cm)", min_szerokosc_dzialki_kielicha, szerokosc_dzialki_avg, "", ""],
    ["Długość płatka (cm)", min_dlugosc_platka, dlugosc_platka_avg, "", ""],
    ["Szerokość płatka (cm)", min_szerokosc_platka, szerokosc_platka_avg, "", ""]
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
