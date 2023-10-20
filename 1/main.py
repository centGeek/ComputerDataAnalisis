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
# Suma = 0.0
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

plt.style.use('_mpl-gallery')


def suma(dana, pion):
    suma = 0.0
    for wiersz in dana:
        suma += wiersz[pion]
    return suma


def LiczenieWPionie(dana, pion, szukana):
    znaleziono = 0
    for wiersz in dana:
        if (wiersz[pion] == szukana):
            znaleziono += wiersz[pion]
    return znaleziono


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

print(sizeOf(dane))
print(round(LiczenieWPionie(dane, 4, 1), 2))
print(str(LiczenieWPionie(dane, 4, 1)) + " " + str(round(percentage(dane, 4, 1), 0)) + " setosa")
print(str(LiczenieWPionie(dane, 4, 1)) + " " + str(round(percentage(dane, 4, 1), 0)) + " versicolor")
print(str(LiczenieWPionie(dane, 4, 1)) + " " + str(round(percentage(dane, 4, 1), 0)) + " virginica")
fig, ax = plt.subplots()

x = [0,1,2]
asd = [LiczenieWPionie(dane,4,0),LiczenieWPionie(dane,4,1),LiczenieWPionie(dane,4,2)]



ax.bar(x, asd, width=0.5, edgecolor="white", linewidth=0.7, color='red')


plt.show()

print(dane[0][0])
print(suma(dane, 0))
