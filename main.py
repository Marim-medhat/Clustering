import pandas as pd
from numpy.ma import equal
import copy

from pandas import read_excel
import random


def ManhattanDistance(x, y):
    S = 0;
    for i in range(len(x)):
        S += abs(int(x[i])- int(y[i]))

    return S


# Classify item to the mean with minimum distance
def Classify(means, item):
    minimum =10000;
    for i in range(len(means)):

        # Find distance from item to mean
        dis = ManhattanDistance(item, means[i]);

        if (dis < minimum):
            minimum = dis;
            index = i;

    return index;


def FindClusters(means):
    clusters = {} # Init clusters

    for i in range(200):
        item = [df.values[i - 1, j] for j in range(1, 32)]

        # Classify item into a cluster
        index = Classify(means, item);

        # Add item to cluster
        if index in clusters.keys():
            clusters[index].append([df.values[i - 1, j] for j in range(0, 32)])
        else:
            clusters[index] = []
            clusters[index].append([df.values[i - 1, j] for j in range(0, 32)])

    for key, value in clusters.items():
            print(key, ' : ', value)

    return(clusters)


def getnewMeans(clusters):
    c = list(clusters.values())  #cluster without keys
    for lis in c:
        for l in lis:
            del l[0]  #delete name of product
    means = list()
    for lis in c:
        mean = list()
        for j in range(0, len(lis[0])):
            tmp = 0
            for i in range(0, len(lis)):
                tmp = tmp + lis[i][j]
            mean.append(tmp / len(lis))

        means.append(mean)
    return means







if __name__ == '__main__':
    df = pd.read_excel('Sales.xlsx', sheet_name='Sheet1')


# get first means (randomle from the taple)
    #k = 5
    k = int(input("Enter your k: "))
    list_random = []
    for i in range(k):
        num = random.randint(1, 200)
        if (num in list_random):
            num = random.randint(1, 200)

        list_random.append(num)


#//////////////////////////////////////

#get list of these values in mean

    means = []
    for i in list_random:
        means.append([df.values[i - 1, j] for j in range(1, 32)])



    cluster= FindClusters(means)
##########################v#####
    while True:
        print ("////////////////////////////////////////////////////////////////////////////////////////")
        clustercopy = copy.deepcopy(cluster)
        newmeans=getnewMeans(clustercopy)
        newcluster = FindClusters(newmeans)
        print(equal(newcluster, cluster))

        if (equal(newcluster, cluster)):
            break
        else:
            cluster=copy.deepcopy(newcluster)


