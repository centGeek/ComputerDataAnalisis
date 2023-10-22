# import csv
#
# data = list(csv.reader(open("./data.csv")))
# print(data[1][0])
#
# for miejsce in data:
#     miejsce[0] = float(miejsce[0])
# for miejsce in data:
#     miejsce[1] = float(miejsce[1])
# for miejsce in data:
#     miejsce[2] = float(miejsce[2])
# for miejsce in data:
#     miejsce[3] = float(miejsce[3])
# for miejsce in data:
#     miejsce[4] = float(miejsce[4])
#
# for aaa in data:
#     for bbb in aaa:
#         print(aaa)
#
# Suma = 0.0                                              czy mozna to usunac Maćku?
#
# for aaa in data:
#     Suma += aaa[0]
#
# print(Suma)

# array123 = [int(numeric_string) for numeric_string in data]

# asd = (data[1][0]+data[1][1])
# for row in data:
#   ads+=row[0]


import csv
import matplotlib.pyplot as plt
import numpy as np



def suma(dana, pion):
    suma = 0.0
    for wiersz in dana:
        suma += wiersz[pion]
    return suma


def LiczenieWPionie(dana, pion, szukana):
    znaleziono = 0
    for wiersz in dana:
        if (wiersz[pion] == szukana):
            znaleziono = znaleziono+1
    return znaleziono
def szukajMaksimum(dana, pion):
    znaleziono = 0
    for wiersz in dana:
        if (wiersz[pion]>znaleziono):
             znaleziono = wiersz[pion]
    return znaleziono
def szukajMinimum(dana, pion):
    znaleziono = 100
    for wiersz in dana:
        if (wiersz[pion]<znaleziono):
            znaleziono = wiersz[pion]
    return znaleziono

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


setosa_count = LiczenieWPionie(dane, 4, 0)
versicolor_count = LiczenieWPionie(dane, 4, 1)
virginica_count = LiczenieWPionie(dane, 4, 2)

maks_dlugosc_dzialki_kielicha = szukajMaksimum(dane, 0)
maks_szerokosc_dzialki_kielicha = szukajMaksimum(dane, 1)
maks_dlugosc_platka = szukajMaksimum(dane, 2)
maks_szerokosc_platka = szukajMaksimum(dane, 3)

min_dlugosc_dzialki_kielicha = szukajMinimum(dane, 0)
min_szerokosc_dzialki_kielicha = szukajMinimum(dane, 1)
min_dlugosc_platka = szukajMinimum(dane, 2)
min_szerokosc_platka = szukajMinimum(dane, 3)


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
print(sizeOf(dane))
print(round(LiczenieWPionie(dane, 4, 1), 2))

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
print(suma(dane, 0))
dlugosc_dzialki_avg = liczSredniaArytmetyczna(dane, 0)
szerokosc_dzialki_avg = liczSredniaArytmetyczna(dane, 1)
dlugosc_platka_avg = liczSredniaArytmetyczna(dane, 2)
szerokosc_platka_avg = liczSredniaArytmetyczna(dane, 2)
data = [
    ["Cecha", "Minimum", "Śr. arytmetyczna", "Mediana (Q1 - Q3)", "Maksimum"],
    ["Długość działki kielicha (cm)", min_dlugosc_dzialki_kielicha,dlugosc_dzialki_avg, "5.80 (5.10 - 6.40)", "7.90"],
    ["Szerokość działki kielicha (cm)", min_szerokosc_dzialki_kielicha, szerokosc_dzialki_avg, "", ""],
    ["Długość płatka (cm)", min_dlugosc_platka, dlugosc_platka_avg, "", ""],
    ["Szerokość płatka (cm)", min_szerokosc_platka,szerokosc_platka_avg, "", ""]
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