
from operator import index


def bubble(listA):
    indexing_length = len(listA) - 1
    sorted = False

    while not sorted:
        sorted = True

        for i in range(0, indexing_length):
            if listA[i] > listA[i+1]:
                sorted = False
                listA[i], listA[i+1] = listA[i+1], listA[i]
    return listA

print(bubble([4,6,8,3,2,5,7,8,9]))