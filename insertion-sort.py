

from readline import insert_text


def insertion(listA):
    indexing_length = range(1, len(listA))

    for i in indexing_length:
        value_to_sort = listA[i]

        while listA[i-1] > value_to_sort and i>0:
            listA[i], listA[i-1] = listA[i-1], listA[i]
            i = i - 1
    return listA

print(insertion([3,5,7,1,34,8,9,5]))