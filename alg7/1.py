import sys

def dijkstra(graph, start):
    # Инициализация
    distances = {node: float('inf') for node in graph}  # Расстояния от начальной вершины до остальных
    distances[start] = 0
    visited = set()  # Посещенные вершины
    previous_nodes = {node: None for node in graph}  # Предыдущая вершина на кратчайшем пути
    current_node = start

    while current_node:
        visited.add(current_node)
        neighbors = graph[current_node]

        for neighbor in neighbors:
            distance = distances[current_node] + neighbors[neighbor]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node

        # Выбор следующей вершины с наименьшим расстоянием
        next_node = None
        for node in graph:
            if node not in visited and distances[node] < float('inf'):
                if next_node is None or distances[node] < distances[next_node]:
                    next_node = node

        current_node = next_node

    return distances, previous_nodes

# Пример графа
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 1},
    'D': {'B': 3, 'C': 1, 'E': 4},
    'E': {'D': 4}
}

start_node = 'A'
distances, previous_nodes = dijkstra(graph, start_node)

# Вывод результатов
for node in distances:
    path = []
    current_node = node
    while current_node:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    print(f"Кратчайший путь от {start_node} до {node}: {path}, Дистанция = {distances[node]}")
