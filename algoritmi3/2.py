class MaxHeap:
    def __init__(self, arr=None):
        self.heap = []
        if arr:
            self.build_heap(arr)

    def build_heap(self, arr): #Постройка двоичной кучи
        self.heap = arr
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i)

    def insert(self, val): #Вставка элементов
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def delete_max(self): #Удаление максимальных элементов
        max_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            self.heapify_down(0)
        return max_val

    def heapify_up(self, i): #поддержание свойства кучи при вставке
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def heapify_down(self, i): #поддержаниe свойства кучи при удалении
        n = len(self.heap)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            max_child = i
            if left < n and self.heap[left] > self.heap[max_child]:
                max_child = left
            if right < n and self.heap[right] > self.heap[max_child]:
                max_child = right
            if max_child == i:
                break
            self.heap[i], self.heap[max_child] = self.heap[max_child], self.heap[i]
            i = max_child

    def merge(self, other_heap):
        self.heap.extend(other_heap.heap)
        self.build_heap(self.heap)
