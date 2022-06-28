
def selection(listA):
    indexing_length = range(0, len(listA)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(listA)):
            if listA[j] < listA[min_value]:
                min_value = j

        if min_value != i:
            listA[min_value], listA[i] = listA[i], listA[min_value]
    
    return listA

print(selection([7,8,8,2,4,5,1,7]))