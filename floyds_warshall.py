def floyds_warshall(graph):
    n = len(graph)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                graph[i][j] = min(graph[i][j] , graph[i][k] + graph[k][j])
graph = [
    [0, 3, float('inf'), float('inf')],
    [float('inf'), 0, 1, float('inf')],
    [float('inf'), float('inf'), 0, 7],
    [float('inf'), float('inf'), float('inf'), 0]
]
floyds_warshall(graph)
for i in graph:
    print(i)
    
        