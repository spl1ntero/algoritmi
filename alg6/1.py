import sys


def find_min_spanning_tree(graph):
    num_vertices = len(graph)
    # Список для хранения вершин, которые уже включены в минимальное остовное дерево
    visited = [False] * num_vertices
    # Начинаем с первой вершины
    visited[0] = True

    min_spanning_tree = []
    min_spanning_distance = 0

    for _ in range(num_vertices - 1):
        min_distance = sys.maxsize
        min_vertex1 = None
        min_vertex2 = None

        # Проходим по всем вершинам, уже включенным в остовное дерево
        for i in range(num_vertices):
            if visited[i]:
                # Ищем ближайшую вершину, еще не включенную в остовное дерево
                for j in range(num_vertices):
                    if not visited[j] and graph[i][j] < min_distance:
                        min_distance = graph[i][j]
                        min_vertex1 = i
                        min_vertex2 = j

        # Добавляем ребро с минимальным расстоянием в остовное дерево
        min_spanning_tree.append((min_vertex1, min_vertex2, min_distance))
        min_spanning_distance += min_distance
        visited[min_vertex2] = True

    return min_spanning_tree, min_spanning_distance


def print_min_spanning_tree(min_spanning_tree, min_spanning_distance):
    print("Маршрут с минимальной общей длиной:")
    for edge in min_spanning_tree:
        vertex1, vertex2, distance = edge
        print(f"Из кампуса {vertex1 + 1} в кампус {vertex2 + 1}, расстояние: {distance}")
    print(f"Общая длина маршрута: {min_spanning_distance}")


# Граф с расстояниями между кампусами
graph = [
    [0, 1.97, 21.6, 10.7, 22.3, 10.4],
    [1.97, 0, 22.3, 11.4, 23, 11.1],
    [21.6, 22.3, 0, 11.5, 5.2, 12],
    [10.7, 1.4, 11.5, 0, 13.4, 0.68],
    [22.3, 23, 5.2, 13.4, 0, 13.8],
    [10.4, 11.1, 12, 0.68, 13.8, 0]
]

min_spanning_tree, min_spanning_distance = find_min_spanning_tree(graph)
print_min_spanning_tree(min_spanning_tree, min_spanning_distance)
