import pandas as pd
from matplotlib import pyplot as plt
import kmeans

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
    plt.bar(k_list, iteration_list, color='blue')
    plt.title('Liczba iteracji vs Liczba klastrów')
    plt.xlabel('Liczba klastrów')
    plt.ylabel('Liczba iteracji')
    plt.xticks(range(min(k_list), max(k_list) + 1, 1))
    plt.show()

def display_WCSS(wcss_list, k_list):
    plt.plot(k_list, wcss_list, marker='o')
    plt.title('WCSS (within-cluster sum of squares) vs. Liczba klastrów')
    plt.xlabel('Liczba klastrów')
    plt.ylabel('wartosc WCSS')
    plt.show()


def display(centroids, clusters, attr1, attr2, title):
    plt.figure(figsize=(10, 8))

    cluster_labels = ['Cluster 1', 'Cluster 2', 'Cluster 3']

    for i, cluster in enumerate(clusters):
        if len(cluster) > 0:
            ctv_cluster = list(zip(*cluster))
            plt.scatter(ctv_cluster[attr1], ctv_cluster[attr2], label=cluster_labels[i], marker='o', facecolors='none',
                        edgecolors=['green', 'red', 'blue'][i])

    for i, centroid in enumerate(centroids):
        plt.scatter(centroid[attr1], centroid[attr2], label=f'Centroid from {cluster_labels[i]}', marker='X', s=100,
                    color=['green', 'red', 'blue'][i])

    plt.xlabel(switch_example(attr1))
    plt.ylabel(switch_example(attr2))

    plt.legend(loc='upper right', fontsize='small')

    plt.title(title)

    plt.show()


nazwy_kolumn = ['Długość Działki Kielicha(cm)', 'Szerokość Działki Kielicha(cm)', 'Długość Płatka(cm)',
                'Szerokość Płatka(cm)', 'Gatunek']

data = pd.read_csv('data.csv', names=nazwy_kolumn)

data = list(zip(*[data[nazwy_kolumn[col]].tolist() for col in range(4)]))

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


