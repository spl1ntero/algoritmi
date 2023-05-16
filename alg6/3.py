import sys


def nearest_neighbor(matrix):
    num_vertices = len(matrix)
    visited = [False] * num_vertices

    # Выбираем случайную начальную вершину
    start_vertex = 0
    visited[start_vertex] = True
    path = [start_vertex]
    total_distance = 0

    # Пока не посетим все вершины
    while len(path) < num_vertices:
        current_vertex = path[-1]
        min_distance = sys.maxsize
        nearest_vertex = None

        # Ищем ближайшую непосещенную вершину
        for i in range(num_vertices):
            if matrix[current_vertex][i] < min_distance and not visited[i]:
                min_distance = matrix[current_vertex][i]
                nearest_vertex = i

        # Добавляем вершину и соответствующее ребро в путь
        path.append(nearest_vertex)
        total_distance += min_distance
        visited[nearest_vertex] = True

    # Замыкаем путь, возвращаемся в начальную вершину
    path.append(start_vertex)
    total_distance += matrix[path[-2]][start_vertex]

    return path, total_distance


# Взвешенный граф с матрицей смежности (пример)
weight_matrix = [
    [0, 2, 5, 6, 8, 3, 10],
    [2, 0, 4, 1, 9, 7, 3],
    [5, 4, 0, 2, 6, 4, 8],
    [6, 1, 2, 0, 3, 2, 5],
    [8, 9, 6, 3, 0, 5, 2],
    [3, 7, 4, 2, 5, 0, 6],
    [10, 3, 8, 5, 2, 6, 0]
]

path, total_distance = nearest_neighbor(weight_matrix)
print("Субоптимальное решение задачи коммивояжера (алгоритм ближайшего соседа):")
print("Путь:", path)
print("Общее расстояние:", total_distance)
