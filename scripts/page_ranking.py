from __future__ import division

import json
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)


def countInitialVector(pagesAmount):

    if pagesAmount == 0:
        pagesAmount = 1

    initialVector = []

    for i in range(pagesAmount):
        initialVector.append(1 / pagesAmount)

    initialVector = np.array(initialVector)

    return initialVector


def countHMatrix(data, pagesAmount):

    HMatrix = [[0 for x in range(pagesAmount)] for y in range(pagesAmount)]

    amount = len((data[0])['outlinks'])
    averageValue = 1 / amount

    for i in range(pagesAmount):
        # print((data[i])['outlinks'])
        amount = len((data[i])['outlinks'])
        averageValue = 1 / amount
        # print(averageValue)
        for j in range(pagesAmount):
            # print(i, j)
            if (data[j])['link'] in (data[i])['outlinks']:
                HMatrix[i][j] = averageValue

    HMatrix = np.array(HMatrix)
    return HMatrix




def countDanglingVector(data, pagesAmount):
    danglingVector = [0 for x in range(pagesAmount)]

    for i in range(pagesAmount):
        if len((data[i])['outlinks']) == 0:
            danglingVector[i] = 1

    danglingVector = np.array(danglingVector)

    return danglingVector



def countEVector(pagesAmount):


    return [1 for i in range(pagesAmount)]

def countPageRankingVector(data, pagesAmount):
    initialVector = countInitialVector(pagesAmount)
    HMatrix = countHMatrix(data, pagesAmount)
    danglingVector = countDanglingVector(data, pagesAmount)
    evector = countEVector(pagesAmount)
    alpha = 0.85


    result = initialVector


    for i in range(50):
        result = (alpha * np.transpose(result)).dot(HMatrix) + \
                 ((alpha * np.transpose(result)).dot(danglingVector) + 1 - alpha) * (
                     np.transpose(evector)) / pagesAmount


    with open('../data/page_ranking.json', "w") as outputResult:
        outputResult.write(str(list(result)))



def readingJsonFromFile():
    with open('../data/spider.json') as json_file:
        data = json.load(json_file)
        pagesAmount = len(data)

        return data, pagesAmount




if __name__== "__main__":
    data, pagesAmount = readingJsonFromFile()
    countPageRankingVector(data, pagesAmount)



