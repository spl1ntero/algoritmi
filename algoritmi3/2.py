class MaxHeap:
    def __init__(self, arr=None):
        self.heap = []
        if arr:
            self.build_heap(arr)

    def build_heap(self, arr):
        self.heap = arr
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i)

    def heapify_down(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify_down(largest)

    def heapify_up(self, i):
        parent = (i - 1) // 2
        if parent >= 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self.heapify_up(parent)

    def search(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)
        return self.get_heap()

    def delete_max(self):
        max_val = self.heap[0]
        last_val = self.heap.pop()
        if self.heap:
            self.heap[0] = last_val
            self.heapify_down(0)
        return max_val, self.get_heap()

    def merge(self, other_heap):
        self.heap.extend(other_heap.heap)
        self.build_heap(self.heap)
        return self.get_heap()

    def get_heap(self):
        return self.heap

arr = [4, 6, 3, 9, 2, 5, 1, 8, 7]
heap = MaxHeap(arr)
print("Исходный список:", arr)
print("Текущее состояние кучи:", heap.get_heap())

max_val, heap_after_delete = heap.delete_max()
print("Максимальный элемент:", max_val)
print("Куча после удаления максимального элемента:", heap_after_delete)

new_heap = MaxHeap([10, 11, 12])
merged_heap = heap.merge(new_heap)
print("Объединение двух куч:", merged_heap)

search_result = heap.search(13)
print("Добавление элемента 13 в кучу:", search_result)