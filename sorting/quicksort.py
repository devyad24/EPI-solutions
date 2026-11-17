def partition(arr, l, h):
    pivot = arr[h]

    i = l - 1

    for j in range(l, h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    #swap the pivot itsefl
    arr[i+1], arr[h] = arr[h], arr[i+1]
    return i + 1



def quicksort(arr, l, h):
    if l < h:
        pivot = partition(arr, l, h)
        quicksort(arr, l, pivot-1)
        quicksort(arr, pivot+1, h)

arr = []
n = len(arr)

quicksort(arr, 0, n - 1)
print(arr)


