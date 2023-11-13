import matplotlib.pyplot as plt
from FunkcjeLiczace import *


class Wykres1:

    def generuj_wykres(dane):
        setosa_count = FunkcjeLiczace.LiczenieWPionie(dane, 4, 0)
        versicolor_count = FunkcjeLiczace.LiczenieWPionie(dane, 4, 1)
        virginica_count = FunkcjeLiczace.LiczenieWPionie(dane, 4, 2)

        fig, ax = plt.subplots()
        napis = ["Gatunek","Liczebność(%)"]
        setosa = ["setosa",str(setosa_count)+" ("+str(round(FunkcjeLiczace.percentage(dane,4,0),1))+"%)"]
        versicolor = ["versicolor",str(versicolor_count)+" ("+str(round(FunkcjeLiczace.percentage(dane,4,1),1))+"%)"]
        virginica = ["virginica", str(virginica_count)+" ("+str(round(FunkcjeLiczace.percentage(dane,4,2),1))+"%)"]
        dol = ["Razem" , str(FunkcjeLiczace.sizeOf(dane))+" (" +str(round((FunkcjeLiczace.sizeOf(dane)/FunkcjeLiczace.sizeOf(dane)),2)*100)+"%)"]

        data = [napis,setosa,versicolor,virginica,dol]

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
