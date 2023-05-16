def find_connectivity(matrix):
    num_vertices = len(matrix)
    num_edges = len(matrix[0])
    visited = [False] * num_vertices
    connectivity = 0

    def dfs(vertex):
        visited[vertex] = True
        for i in range(num_edges):
            for j in range(num_vertices):
                if matrix[j][i] == 1 and not visited[j]:
                    dfs(j)

    for i in range(num_vertices):
        if not visited[i]:
            dfs(i)
            connectivity += 1

    return connectivity


# Граф с матрицей инцидентности (пример)
incidence_matrix = [
    [1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 1, 1]
]

connectivity = find_connectivity(incidence_matrix)
print("Число связности графа (с помощью матрицы инцидентности):", connectivity)
