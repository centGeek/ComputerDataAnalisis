def scaling(minimum, maksimum, argument):
    return (argument - minimum) / (maksimum - minimum) #normalizacja min max dla zakresu <0;1>




def distance_list_for_two(trening_1, test_1, trening_2, test_2):
    list_of_distances = []
    for i in range(len(trening_1)):
        list_of_distances.append(distance_for_two(trening_1[i], test_1, trening_2[i], test_2))
    return list_of_distances


def distance_list_for_four(trening_1, test_1, trening_2, test_2, trening_3, test_3, trening_4,
                           test_4):
    lista_odleglosci = []
    for i in range(len(trening_1)):
        lista_odleglosci.append(
            distance_for_four(trening_1[i], test_1, trening_2[i], test_2, trening_3[i], test_3,
                              trening_4[i], test_4))
    return lista_odleglosci


def check_species_number(lista): #sprawdzenie ile jest roznych gatunkow
    list_of_num_differences = []
    for i in lista:
        if i not in list_of_num_differences:
            list_of_num_differences.append(i)
    return len(list_of_num_differences)


def distance_for_two(x1, x2, y1, y2):
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5


def distance_for_four(x1, x2, y1, y2, z1, z2, v1, v2):
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2) + ((v1 - v2) ** 2)) ** 0.5

def knn(list_of_distances, list_of_species, k):
    indexes_that_are_closest = []
    num_for_species = []
    for i in range(check_species_number(list_of_species)): #wypełnienie listy ile jest możliwych gatunków
        num_for_species.append(0)
    for i in range(k):                            #wypełnienie tablicy tak, żeby było k elementów, działamy na indeksach, które mają odniesienie do listy odległości
        indexes_that_are_closest.append(i)
    for i in range(k - 1):
        for j in range(k - i - 1):
            if list_of_distances[indexes_that_are_closest[j]] > list_of_distances[   #sortowanie tablicy od najmniejszej wartości odległości
                indexes_that_are_closest[j + 1]]:
                var = indexes_that_are_closest[j]
                indexes_that_are_closest[j] = indexes_that_are_closest[j + 1]
                indexes_that_are_closest[j + 1] = var
    for i in range(k, len(list_of_distances)):
        for j in range(k):
            if list_of_distances[i] < list_of_distances[indexes_that_are_closest[j]]:
                for l in range(k - 1, j, -1):
                    indexes_that_are_closest[l] = indexes_that_are_closest[l - 1]
                indexes_that_are_closest[j] = i                                                    #sprawdzenie, czy badany element jest mniejszy od któregoś z elementów tablicy indeksów, jeśli tak to przesuwamy wszystkie elementy większe o jeden w prawo (oprócz ostatniego, który znika z tablicy) i wkładamy w odpiowiednie miejsce nr indeksowy tego elementu
                break
    for i in range(k):
        num_for_species[list_of_species[indexes_that_are_closest[i]]] += 1 #podliczamy, z jakiej klasy są elementy o najmniejszych odległościach
    if num_for_species.count(max(num_for_species)) == 1: #jeśli mamy remis, to sprawdzamy knn dla k o jeden mniejszego, w przeciwnym wypadku zwracamy nr odpowiedniego gatunku
        return num_for_species.index(max(num_for_species))
    else:
        return knn(list_of_distances, list_of_species, k - 1)
