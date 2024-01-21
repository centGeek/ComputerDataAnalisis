def normalizacja(minimum, maksimum, argument):
    return (argument - minimum) / (maksimum - minimum) #normalizacja min max dla zakresu <0;1>


def odleglosc_dla_dwoch(x1, x2, y1, y2):
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5


def odleglosc_dla_cztererch(x1, x2, y1, y2, z1, z2, v1, v2):
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2) + ((v1 - v2) ** 2)) ** 0.5


def lista_odleglosci_dla_dwoch(trening_1, testowa_1, trening_2, testowa_2):
    lista_odleglosci = []
    for i in range(len(trening_1)):
        lista_odleglosci.append(odleglosc_dla_dwoch(trening_1[i], testowa_1, trening_2[i], testowa_2))
    return lista_odleglosci


def lista_odleglosci_dla_czterech(trening_1, testowa_1, trening_2, testowa_2, trening_3, testowa_3, trening_4,
                                  testowa_4):
    lista_odleglosci = []
    for i in range(len(trening_1)):
        lista_odleglosci.append(
            odleglosc_dla_cztererch(trening_1[i], testowa_1, trening_2[i], testowa_2, trening_3[i], testowa_3,
                                    trening_4[i], testowa_4))
    return lista_odleglosci


def sprawdz_ile_gatunkow(lista): #sprawdzenie ile jest roznych gatunkow
    lista_ile_roznych = []
    for i in lista:
        if i not in lista_ile_roznych:
            lista_ile_roznych.append(i)
    return len(lista_ile_roznych)


def knn(lista_odleglosci, lista_gatunkow, k):
    indeksy_o_najmniejszych_odleglosciach = []
    ilosc_dla_gatunku = []
    for i in range(sprawdz_ile_gatunkow(lista_gatunkow)): #wypełnienie listy ile jest możliwych gatunków
        ilosc_dla_gatunku.append(0)
    for i in range(k):                                    #wypełnienie tablicy tak, żeby było k elementów, działamy na indeksach, które mają odniesienie do listy odległości
        indeksy_o_najmniejszych_odleglosciach.append(i)
    for i in range(k - 1):
        for j in range(k - i - 1):
            if lista_odleglosci[indeksy_o_najmniejszych_odleglosciach[j]] > lista_odleglosci[   #sortowanie tablicy od najmniejszej wartości odległości
                indeksy_o_najmniejszych_odleglosciach[j + 1]]:
                var = indeksy_o_najmniejszych_odleglosciach[j]
                indeksy_o_najmniejszych_odleglosciach[j] = indeksy_o_najmniejszych_odleglosciach[j + 1]
                indeksy_o_najmniejszych_odleglosciach[j + 1] = var
    for i in range(k, len(lista_odleglosci)):
        for j in range(k):
            if lista_odleglosci[i] < lista_odleglosci[indeksy_o_najmniejszych_odleglosciach[j]]:
                for l in range(k - 1, j, -1):
                    indeksy_o_najmniejszych_odleglosciach[l] = indeksy_o_najmniejszych_odleglosciach[l - 1]
                indeksy_o_najmniejszych_odleglosciach[j] = i                                                    #sprawdzenie, czy badany element jest mniejszy od któregoś z elementów tablicy indeksów, jeśli tak to przesuwamy wszystkie elementy większe o jeden w prawo (oprócz ostatniego, który znika z tablicy) i wkładamy w odpiowiednie miejsce nr indeksowy tego elementu
                break
    for i in range(k):
        ilosc_dla_gatunku[lista_gatunkow[indeksy_o_najmniejszych_odleglosciach[i]]] += 1 #podliczamy, z jakiej klasy są elementy o najmniejszych odległościach
    if ilosc_dla_gatunku.count(max(ilosc_dla_gatunku)) == 1: #jeśli mamy remis, to sprawdzamy knn dla k o jeden mniejszego, w przeciwnym wypadku zwracamy nr odpowiedniego gatunku
        return ilosc_dla_gatunku.index(max(ilosc_dla_gatunku))
    else:
        return knn(lista_odleglosci, lista_gatunkow, k - 1)
