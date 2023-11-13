import matplotlib.pyplot as plt
from FunkcjeLiczace import *


class WykresyPudelkowe:

    def narysujBoxplot(dana, pion, Nazwa):

        kolumna1 = FunkcjeLiczace.dajKolumne(dana, pion)
        kolumna2 = FunkcjeLiczace.dajKolumne(dana, 4)

        gatunku0 = []
        gatunku1 = []
        gatunku2 = []

        for i in range(0, 150, 1):
            if (kolumna2[i] == 0):
                gatunku0.append(kolumna1[i])
            if (kolumna2[i] == 1):
                gatunku1.append(kolumna1[i])
            if (kolumna2[i] == 2):
                gatunku2.append(kolumna1[i])


        gatunki = ["setosa", "versicolor", "virginica"]
        data = [gatunku0, gatunku1, gatunku2]
        fig = plt.figure(figsize=(5, 5))
        #ax = fig.add_axes([0.12, 0.12, 0.82, 0.82])
        #plt.set_xticklabels()
        plt.boxplot(data,labels=gatunki)
        plt.grid(axis='y', color="grey")
        plt.title(Nazwa)
        plt.show()