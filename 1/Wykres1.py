import csv
import matplotlib.pyplot as plt
from FunkcjeLiczace import *


class Wykres1:

    def generuj_wykres(dane):
        setosa_count = FunkcjeLiczace.LiczenieWPionie(dane, 4, 0)
        versicolor_count = FunkcjeLiczace.LiczenieWPionie(dane, 4, 1)
        virginica_count = FunkcjeLiczace.LiczenieWPionie(dane, 4, 2)

        fig, ax = plt.subplots()

        x = ["setosa", "versicolor", "virginica"]
        counts = [setosa_count, versicolor_count, virginica_count]
        percentages = [(count * 100 / sum(counts)) for count in counts]

        ax.bar(x, counts, width=0.5, edgecolor="white", linewidth=0.7, color='red')
        ax.set_ylabel("Liczba poszczególnych gatunków")
        for i, v in enumerate(counts):
            ax.text(i, v + 5, f"{percentages[i]:.2f}%", ha="center", va="bottom")

        plt.show()
