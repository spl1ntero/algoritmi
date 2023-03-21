def heapify_min(arr, n, i):
    smallest = i 
    left = 2 * i + 1 
    right = 2 * i + 2 

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  
        heapify_min(arr, n, smallest)


def build_min_heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify_min(arr, n, i)


def heapify_max(arr, n, i):
    largest = i  
    left = 2 * i + 1 
    right = 2 * i + 2 

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 
        heapify_max(arr, n, largest)


def build_max_heap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify_max(arr, n, i)
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]

build_min_heap(arr)
print("Минимальная куча:", arr)

build_max_heap(arr)
print("Максимальная куча:", arr)