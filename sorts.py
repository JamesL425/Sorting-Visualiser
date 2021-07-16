def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr
def selectionSort(arr):
    for i in range(len(arr)):
        indx = i
        for j in range(i+1, len(arr)):
            if arr[indx] > arr[j]:
                indx = j
        
        arr[i], arr[indx] = arr[indx], arr[i]
        yield arr
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-= 1
            arr[j+1] = key
            yield arr

