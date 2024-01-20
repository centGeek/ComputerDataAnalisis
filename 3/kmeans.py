import math

import numpy as np



def setCentroids(data, k):
    centroids = []
    indexy = set()

    for _ in range(k):
        index = np.random.choice(len(data))

        while index in indexy:
            index = np.random.choice(len(data))

        indexy.add(index)
        centroids.append(data[index])

    return centroids
def calculateDistance(data, centroid):
    distanceToPowerOf2 = sum((centroid[i] - data[i]) ** 2 for i in range(4))
    distance = math.sqrt(distanceToPowerOf2)

    return distance
def setClusters(data, centroids):
    listOfClusters = [[] for _ in range(len(centroids))]
    # Iteruje przez każdy punkt danych
    for i in range(len(data)):
        minValue = calculateDistance(data[i], centroids[0])
        minIndex = 0
        # Inicjalizuje wartości minimalnej odległości i indeksu centroidu
        for j in range(1, len(centroids)):
            tempValue = calculateDistance(data[i], centroids[j])
            # Aktualizuje wartość minimalnej odległości i indeksu centroidu
            if minValue > tempValue:
                minValue = tempValue
                minIndex = j
        # Przypisuje punkt do klastra odpowiadającego centroidowi o minimalnej odległości
        listOfClusters[minIndex].append(data[i])
    return listOfClusters

def positionUpdateOfCentroids(clusters):
    centroids = []
    # Sprawdza, czy klaster zawiera punkty danych
    for cluster in clusters:
        if len(cluster) > 0:
            dimensions = len(cluster[0])
            meanValues = [0] * dimensions

            # Sumuje współrzędne punktów w klastrze
            for point in cluster:
                for i in range(dimensions):
                    meanValues[i] += point[i]
            # Oblicza średnie wartości współrzędnych
            meanValues = tuple(value / len(cluster) for value in meanValues)
            centroids.append(meanValues)

    return centroids

def kMeans(data, k, maxIteration):
    iteration = 0

    centroids = setCentroids(data, k)
    clusters = setClusters(data, centroids)

    for i in range(maxIteration):
        iteration += 1

        centroids = positionUpdateOfCentroids(clusters)
        clustersToCompare = setClusters(data, centroids)

        if clusters == clustersToCompare and clustersToCompare is not None:
            break

        clusters = clustersToCompare

    return centroids, clusters, iteration

def calculateWCSS(centroids, clusters):
    wcss = 0
    for i in range(len(centroids)):
        for j in range(len(clusters[i])):
            # Dodaje sumę kwadratów odległości między punktem a centroidem
            wcss += sum((centroids[i][k] - clusters[i][j][k]) ** 2 for k in range(4))
    return wcss