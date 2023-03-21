def connect_ropes(ropes):
    # Построим мин-кучу вручную
    n = len(ropes)
    for i in range(n // 2 - 1, -1, -1):
        heapify(ropes, n, i)
    
    cost = 0
    
    # Пока в куче не останется только один канат
    while n > 1:
        # Извлекаем два каната с наименьшими значениями из кучи
        first_rope = ropes[0]
        ropes[0] = ropes[n - 1]
        n -= 1
        heapify(ropes, n, 0)
        
        second_rope = ropes[0]
        ropes[0] = ropes[n - 1]
        n -= 1
        heapify(ropes, n, 0)
        
        # Складываем их длины и создаем новый канат с этой длиной
        new_rope = first_rope + second_rope
        
        # Добавляем новый канат в кучу
        ropes[n] = new_rope
        n += 1
        heapify(ropes, n, n - 1)
        
        # Увеличиваем суммарные затраты на длину нового каната
        cost += new_rope
    
    # Возвращаем порядок связывания канатов и суммарные затраты
    return ropes[0], cost


def heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)

ropes = [4, 3, 2, 6]
result, cost = connect_ropes(ropes)

print("Связывание канатов в порядке:", result)
print("Общая стоимость:", cost)