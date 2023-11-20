import csv
from FunkcjeLiczace import *
import matplotlib.pyplot as plt
dane = []

with open("./data.csv", newline='') as plik_csv:
    czytnik_csv = csv.reader(plik_csv)
    for wiersz in czytnik_csv:
        wiersz_float = [float(wartość) for wartość in wiersz]
        dane.append(wiersz_float)

n = FunkcjeLiczace.sizeOf(dane)

x_av,x_odch = FunkcjeLiczace.liczSredniaArytmetyczna(dane, 0)
y_av,y_odch = FunkcjeLiczace.liczSredniaArytmetyczna(dane, 1)

sum = 0
for wiersz in dane:
    lewy = wiersz[0] * wiersz[1]
    prawy = (x_av * y_av)
    sum += lewy - prawy
sum_n = sum / n

pion_x = FunkcjeLiczace.dajKolumne(dane,0)
pion_y = FunkcjeLiczace.dajKolumne(dane,1)

wynik = sum_n / (x_odch * y_odch)

plt.scatter(pion_x,pion_y, c=pion_x)
plt.plot([169, 189], [7.23, 11.48])
#plt.xlim(0, 1)

plt.show()
print(wynik)