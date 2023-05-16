def find_connectivity(matrix):
    num_vertices = len(matrix)
    visited = [False] * num_vertices
    connectivity = 0

    def dfs(vertex):
        visited[vertex] = True
        for i in range(num_vertices):
            if matrix[vertex][i] == 1 and not visited[i]:
                dfs(i)

    for i in range(num_vertices):
        if not visited[i]:
            dfs(i)
            connectivity += 1

    return connectivity


# Граф с матрицей смежности (пример)
adjacency_matrix = [
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0]
]

connectivity = find_connectivity(adjacency_matrix)
print("Число связности графа (с помощью матрицы смежности):", connectivity)
