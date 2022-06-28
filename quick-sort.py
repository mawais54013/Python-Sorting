
from operator import index


def quick(arr):
    index_length = len(arr)
    if index_length <= 1:
        return arr
    else:
        pivot = arr.pop()
    
    item_greater = []
    item_lesser = []

    for i in arr:
        if i > pivot:
            item_greater.append(i)
        else:
            item_lesser.append(i)
        
    return quick(item_lesser) + [pivot] + quick(item_greater)

print(quick([4,1,6,7,1,9,5,6,0,7]))