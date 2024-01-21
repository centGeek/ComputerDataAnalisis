import pandas as pd
from matplotlib import pyplot as plt
import kmeans
import seaborn as sns
import knn
def switch_example(attr1):
    switch_dict = {
        0: "Długość działki kielicha (cm)",
        1: "Szerokośćć działki kielicha (cm)",
        2: "Długość płatka (cm)",
        3: "Szerokośc płatka (cm)"
    }
    result = switch_dict.get(attr1)
    return result

def display_iteration(iteration_list, k_list):
    sns.barplot(x=k_list, y=iteration_list, color='blue')
    plt.title('Liczba iteracji vs Liczba klastrów')
    plt.xlabel('Liczba klastrów')
    plt.ylabel('Liczba iteracji')
    plt.show()

def display_WCSS(wcss_list, k_list):
    sns.lineplot(x=k_list, y=wcss_list, marker='o')
    plt.title('WCSS (within-cluster sum of squares) vs. Liczba klastrów')
    plt.xlabel('Liczba klastrów')
    plt.ylabel('Wartość WCSS')
    plt.show()


def display(centroids, clusters, attr1, attr2, title):
    plt.figure(figsize=(10, 8))

    cluster_labels = ['Cluster 1', 'Cluster 2', 'Cluster 3']

    for i, cluster in enumerate(clusters):
        if len(cluster) > 0:
            ctv_cluster = list(zip(*cluster))
            sns.scatterplot(x=ctv_cluster[attr1], y=ctv_cluster[attr2], label=cluster_labels[i],
                            marker='o', facecolors='none', edgecolor=['green', 'red', 'blue'][i])

    for i, centroid in enumerate(centroids):
        sns.scatterplot(x=[centroid[attr1]], y=[centroid[attr2]], label=f'Centroid from {cluster_labels[i]}',
                        marker='X', s=100, color=['green', 'red', 'blue'][i])

    plt.xlabel(switch_example(attr1))
    plt.ylabel(switch_example(attr2))

    plt.legend(loc='upper right', fontsize='small')

    plt.title(title)

    plt.show()


column_names = ['Długość Działki Kielicha(cm)', 'Szerokość Działki Kielicha(cm)', 'Długość Płatka(cm)',
                'Szerokość Płatka(cm)', 'Gatunek']

data = pd.read_csv('data.csv', names=column_names)

data = list(zip(*[data[column_names[col]].tolist() for col in range(4)]))

centroids, clusters, iteration = kmeans.kMeans(data, 3, 100)


atributes_combinations = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

for attr1, attr2 in atributes_combinations:
    title = 'Wykres zależności'
    display(centroids, clusters, attr1, attr2, title)

wcss_list = []
iteration_list = []
k_list = []
for i in range(2,11):
    centroids, clusters, iteration = kmeans.kMeans(data, i, 100)
    wcss_list.append(kmeans.calculateWCSS(centroids, clusters))
    iteration_list.append(iteration)
    k_list.append(i)

display_WCSS(wcss_list, k_list)
display_iteration(iteration_list, k_list)

 ##knn

def czyszczenie_output():
    for i in range(50):
        print(" ")

def czyszczenie_macierzy_pomylek():
    for i in range(ile_gatunkow):
        for j in range(ile_gatunkow):
            macierz_pomylek[i][j] = 0


def procent_sukcesu():
    ile_udanych = 0
    for i in range(ile_gatunkow):
        ile_udanych += macierz_pomylek[i][i]
    return (round((ile_udanych) / (len(lista_testowa[i])) * 100, 1))


def wybor_najlepsze_k(lista_sukces_procent):
    lista_ciagow = []
    lista_aktualnego_ciagu = []
    indeks_ciagu = 0
    maksymalna_dlugosc_indeks = 0
    var = 1
    for i in lista_sukces_procent:
        if i == max(lista_sukces_procent):
            lista_aktualnego_ciagu.append(i)
        else:

            lista_ciagow.append([indeks_ciagu, lista_aktualnego_ciagu.copy()])
            lista_aktualnego_ciagu = []
            indeks_ciagu = var
        var += 1

    lista_ciagow.append([indeks_ciagu, lista_aktualnego_ciagu.copy()])
    for i in lista_ciagow:
        if len(i[1]) > len(lista_ciagow[maksymalna_dlugosc_indeks][1]):
            maksymalna_dlugosc_indeks = lista_ciagow.index(i)
    return lista_ciagow[maksymalna_dlugosc_indeks][0] + 1


def rysuj_tabelke(k):
    print(f"\nk = {k}     Rozpoznanie --->\n   Faktyczna klasa v ")

    data = {'': ['Setosa', 'Versicolor', 'Virginica']}
    for i in range(ile_gatunkow):
        data[nazwy_kolumn[-1][i]] = macierz_pomylek[i]

    df = pd.DataFrame(data)
    print(df.to_string(index=False))

    czyszczenie_macierzy_pomylek()

def rysuj(czy_dla_czterech, parametr1, parametr2):
    lista_sukces_procent = []
    if czy_dla_czterech:
        for k in range(1, 16):  # knn dla czterzech parametrow
            for i in range(len(lista_testowa[0])):
                wynik = knn.knn(
                    knn.lista_odleglosci_dla_czterech(lista_treningowa[0], lista_testowa[0][i], lista_treningowa[1],
                                                      lista_testowa[1][i], lista_treningowa[2], lista_testowa[2][i],
                                                      lista_treningowa[3], lista_testowa[3][i]), lista_treningowa[4], k)
                macierz_pomylek[lista_testowa[4][i]][wynik] += 1
            lista_sukces_procent.append(procent_sukcesu())
            czyszczenie_macierzy_pomylek()
        najlepsze_k = wybor_najlepsze_k(lista_sukces_procent)
        for i in range(len(lista_testowa[0])):
            wynik = knn.knn(
                knn.lista_odleglosci_dla_czterech(lista_treningowa[0], lista_testowa[0][i], lista_treningowa[1],
                                                  lista_testowa[1][i], lista_treningowa[2], lista_testowa[2][i],
                                                  lista_treningowa[3], lista_testowa[3][i]), lista_treningowa[4],
                najlepsze_k)
            macierz_pomylek[lista_testowa[4][i]][wynik] += 1
    else:
        for k in range(1, 16):  # knn dla dwoch parametrow
            for i in range(len(lista_testowa[0])):
                wynik = knn.knn(
                    knn.lista_odleglosci_dla_dwoch(lista_treningowa[parametr1], lista_testowa[parametr1][i],
                                                   lista_treningowa[parametr2], lista_testowa[parametr2][i]),
                    lista_treningowa[4], k)
                macierz_pomylek[lista_testowa[4][i]][wynik] += 1
            lista_sukces_procent.append(procent_sukcesu())
            czyszczenie_macierzy_pomylek()
        najlepsze_k = wybor_najlepsze_k(lista_sukces_procent)
        for i in range(len(lista_testowa[0])):
            wynik = knn.knn(
                knn.lista_odleglosci_dla_dwoch(lista_treningowa[parametr1], lista_testowa[parametr1][i],
                                               lista_treningowa[parametr2], lista_testowa[parametr2][i]),
                lista_treningowa[4], najlepsze_k)
            macierz_pomylek[lista_testowa[4][i]][wynik] += 1

    plt.plot(range(1, 16), lista_sukces_procent)
    plt.xlabel('k')
    plt.ylabel('Wynik [%]')
    rysuj_tabelke(najlepsze_k)
    plt.show()
    czyszczenie_macierzy_pomylek()
    czyszczenie_output()

nazwy_kolumn = ['Długość Działki Kielicha(cm)', 'Szerokość Działki Kielicha(cm)', 'Długość Płatka(cm)',
                'Szerokość Płatka(cm)', 'Gatunek']

treningowy = pd.read_csv('data_train.csv', names=nazwy_kolumn)
testowy = pd.read_csv('data_test.csv', names=nazwy_kolumn)

lista_minimum_maksimum = []
for i in range(treningowy.shape[1] - 1):
    lista_minimum_maksimum.append(min(treningowy[nazwy_kolumn[i]]))
    lista_minimum_maksimum.append(max(treningowy[nazwy_kolumn[i]]))
lista_treningowa = [treningowy[nazwy_kolumn[0]].tolist(), treningowy[nazwy_kolumn[1]].tolist(),
                    treningowy[nazwy_kolumn[2]].tolist(), treningowy[nazwy_kolumn[3]].tolist(),
                    treningowy[nazwy_kolumn[4]].tolist()]
lista_testowa = [testowy[nazwy_kolumn[0]].tolist(), testowy[nazwy_kolumn[1]].tolist(),
                 testowy[nazwy_kolumn[2]].tolist(), testowy[nazwy_kolumn[3]].tolist(),
                 testowy[nazwy_kolumn[4]].tolist()]
for i in range(len(lista_treningowa) - 1):
    for j in range(len(lista_treningowa[i])):
        lista_treningowa[i][j] = knn.normalizacja(lista_minimum_maksimum[i * 2], lista_minimum_maksimum[i * 2 + 1],
                                                  lista_treningowa[i][j])
for i in range(len(lista_testowa) - 1):
    for j in range(len(lista_testowa[i])):
        lista_testowa[i][j] = knn.normalizacja(lista_minimum_maksimum[i * 2], lista_minimum_maksimum[i * 2 + 1],
                                               lista_testowa[i][j])

ile_gatunkow = knn.sprawdz_ile_gatunkow(lista_treningowa[-1])
macierz_pomylek = []
lista_pomylek_pomoc = []
for i in range(ile_gatunkow):
    lista_pomylek_pomoc.append(0)
for i in range(ile_gatunkow):
    macierz_pomylek.append(lista_pomylek_pomoc.copy())

rysuj(True, 0, 0)
rysuj(False, 0, 1)
rysuj(False, 0, 2)
rysuj(False, 0, 3)
rysuj(False, 1, 2)
rysuj(False, 1, 3)
rysuj(False, 2, 3)

