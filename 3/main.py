import pandas as pd
import tabulate
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
    sns.barplot(x=k_list, y=iteration_list, color='pink')
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

    cluster_labels = ['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5', 'Cluster 6', 'Cluster 7',
                      'Cluster 8']

    for i, cluster in enumerate(clusters):
        if len(cluster) > 0:
            ctv_cluster = list(zip(*cluster))
            sns.scatterplot(x=ctv_cluster[attr1], y=ctv_cluster[attr2], label=cluster_labels[i],
                            marker='o', facecolors='none',
                            edgecolor=['green', 'red', 'blue', 'yellow', 'brown', 'cyan', 'pink', 'purple'][i])

    for i, centroid in enumerate(centroids):
        sns.scatterplot(x=[centroid[attr1]], y=[centroid[attr2]], label=f'Centroid from {cluster_labels[i]}',
                        marker='X', s=100,
                        color=['green', 'red', 'blue', 'yellow', 'brown', 'cyan', 'pink', 'purple'][i])

    plt.xlabel(switch_example(attr1))
    plt.ylabel(switch_example(attr2))

    plt.legend(loc='upper right', fontsize='small')

    plt.title(title)

    plt.show()


column_names = ['Długość Działki Kielicha(cm)', 'Szerokość Działki Kielicha(cm)', 'Długość Płatka(cm)',
                'Szerokość Płatka(cm)', 'Gatunek']

data = pd.read_csv('data.csv', names=column_names)

data = list(zip(*[data[column_names[col]].tolist() for col in range(4)]))

centroids, clusters, iteration = kmeans.kMeans(data, 3, 1000)
# maksymalnie k to 6, wynika to tylko z tego że trzeba jawnie kolor napisać.


atributes_combinations = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

for attr1, attr2 in atributes_combinations:
    title = 'Wykres zależności'
    display(centroids, clusters, attr1, attr2, title)

wcss_list = []
iteration_list = []
k_list = []
for i in range(2, 11):
    centroids, clusters, iteration = kmeans.kMeans(data, i, 100)
    wcss_list.append(kmeans.calculateWCSS(centroids, clusters))
    iteration_list.append(iteration)
    k_list.append(i)

display_WCSS(wcss_list, k_list)
display_iteration(iteration_list, k_list)


##knn

def output_clear():
    for i in range(50):
        print(" ")
        # Metoda po prostu rysuje pustkę na konsoli


def clear_of_error_matrix():
    for i in range(species_number):
        for j in range(species_number):
            error_matrix[i][j] = 0
    # Czyścimy macierz z błędami


def success_percentage():
    numbof_succeeded = 0
    for i in range(species_number):
        numbof_succeeded += error_matrix[i][i]
    return (round((numbof_succeeded) / (len(test_list[i])) * 100, 1))
    # Liczymy procent udanych dopasowań


def choose_best_k(list_success_percentage):
    sequence_list = []
    list_of_current_sequence = []
    index_of_sequence = 0
    max_length_index = 0
    var = 1
    for i in list_success_percentage:
        if i == max(list_success_percentage):
            list_of_current_sequence.append(i)
        else:
            sequence_list.append([index_of_sequence, list_of_current_sequence.copy()])
            list_of_current_sequence = []
            index_of_sequence = var
        var += 1

    sequence_list.append([index_of_sequence, list_of_current_sequence.copy()])
    for i in sequence_list:
        if len(i[1]) > len(sequence_list[max_length_index][1]):
            max_length_index = sequence_list.index(i)
    return sequence_list[max_length_index][0] + 1


def draw_table(k, parametr1, parametr2, isForFour):
    lists_with_outputs_columns = []
    lists_with_outputs_rows = []
    for i in range(species_number):
        for j in range(species_number):
            lists_with_outputs_columns.append(error_matrix[i][j])
        lists_with_outputs_rows.append(lists_with_outputs_columns.copy())
        lists_with_outputs_columns = []

    tab_to_show = {
        "k = " + str(k) + "     Rozpoznanie --->\n   Faktyczna klasa v ": ["Setosa", "Versicolor", "Virginica"],
        "Setosa": lists_with_outputs_rows[0], "Versicolor": lists_with_outputs_rows[1],
        "Virginica": lists_with_outputs_rows[2]}
    if isForFour:
        print("Dla czterech parametrow")
    else:
        print(coll_name[parametr1] + " i " + coll_name[parametr2])
    print(tabulate.tabulate(tab_to_show, headers="keys", tablefmt="fancy_grid", showindex=False))
    clear_of_error_matrix()


def draw(is_for_four, parametr1, parametr2, title):
    success_percentage_list = []
    if is_for_four:
        for k in range(1, 16):  # knn dla czterzech parametrow
            for i in range(len(test_list[0])):
                result = knn.knn(
                    knn.distance_list_for_four(train_list[0], test_list[0][i], train_list[1],
                                               test_list[1][i], train_list[2], test_list[2][i],
                                               train_list[3], test_list[3][i]), train_list[4], k)
                error_matrix[test_list[4][i]][result] += 1
            success_percentage_list.append(success_percentage())
            clear_of_error_matrix()
        best_k = choose_best_k(success_percentage_list)
        for i in range(len(test_list[0])):
            result = knn.knn(
                knn.distance_list_for_four(train_list[0], test_list[0][i], train_list[1],
                                           test_list[1][i], train_list[2], test_list[2][i],
                                           train_list[3], test_list[3][i]), train_list[4],
                best_k)
            error_matrix[test_list[4][i]][result] += 1
    else:
        for k in range(1, 16):  # knn dla dwoch parametrow
            for i in range(len(test_list[0])):
                result = knn.knn(
                    knn.distance_list_for_two(train_list[parametr1], test_list[parametr1][i],
                                              train_list[parametr2], test_list[parametr2][i]),
                    train_list[4], k)
                error_matrix[test_list[4][i]][result] += 1
            success_percentage_list.append(success_percentage())
            clear_of_error_matrix()
        best_k = choose_best_k(success_percentage_list)
        for i in range(len(test_list[0])):
            result = knn.knn(
                knn.distance_list_for_two(train_list[parametr1], test_list[parametr1][i],
                                          train_list[parametr2], test_list[parametr2][i]),
                train_list[4], best_k)
            error_matrix[test_list[4][i]][result] += 1

    plt.plot(range(1, 16), success_percentage_list)
    plt.xlabel('k')
    plt.ylabel('Wynik [%]')
    plt.title(title)
    draw_table(best_k, parametr1, parametr2, is_for_four)
    plt.show()
    clear_of_error_matrix()
    output_clear()


coll_name = ['Długość Działki Kielicha(cm)', 'Szerokość Działki Kielicha(cm)', 'Długość Płatka(cm)',
             'Szerokość Płatka(cm)', 'Gatunek']

trainingSet = pd.read_csv('data_train.csv', names=coll_name)
test = pd.read_csv('data_test.csv', names=coll_name)

list_min_max = []
for i in range(trainingSet.shape[1] - 1):
    list_min_max.append(min(trainingSet[coll_name[i]]))
    list_min_max.append(max(trainingSet[coll_name[i]]))
train_list = [trainingSet[coll_name[0]].tolist(), trainingSet[coll_name[1]].tolist(),
              trainingSet[coll_name[2]].tolist(), trainingSet[coll_name[3]].tolist(),
              trainingSet[coll_name[4]].tolist()]
test_list = [test[coll_name[0]].tolist(), test[coll_name[1]].tolist(),
             test[coll_name[2]].tolist(), test[coll_name[3]].tolist(),
             test[coll_name[4]].tolist()]
for i in range(len(train_list) - 1):
    for j in range(len(train_list[i])):
        train_list[i][j] = knn.scaling(list_min_max[i * 2], list_min_max[i * 2 + 1],
                                       train_list[i][j])
for i in range(len(test_list) - 1):
    for j in range(len(test_list[i])):
        test_list[i][j] = knn.scaling(list_min_max[i * 2], list_min_max[i * 2 + 1],
                                      test_list[i][j])

species_number = knn.check_species_number(train_list[-1])
error_matrix = []
lista_pomylek_pomoc = []
for i in range(species_number):
    lista_pomylek_pomoc.append(0)
for i in range(species_number):
    error_matrix.append(lista_pomylek_pomoc.copy())

draw(True, 0, 0, "Wszystkie 4 cechy jednocześnie")

for attr1, attr2 in atributes_combinations:
    draw(False, attr1, attr2, coll_name[attr1] + " i " + coll_name[attr2])
# iterowanie po dwóch kolekcjach.
