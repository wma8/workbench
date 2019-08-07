def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def partition(array, low, high):
    pivot = array[high]
    i = low-1

    for j in range(low, high):
        if array[j] < pivot:
            i+=1
            swap(array, i, j)
    
    swap(array, high, i+1)
    return (i+1)

def quicksort(array, low, high):
    if array is None or len(array) == 0:
        return
    if low < high: 
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)

if __name__ == '__main__':
    array = [5, 3, 9, 13, 25, 32, 8, 10, 23, 15, 13]
    quicksort(array, 0, len(array)-1)
    print(array)



