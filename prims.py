def prims(graph):
    n = len(graph)
    visited = [False]*n
    visited[0] = True
    cost = 0
    edge = 0
    while edge < n-1 :
        min = float('inf')
        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and graph[i][j] != 0:
                        if graph[i][j] < min:
                            min =  graph[i][j]
                            x = i
                            y = j
            visited[y] = True
            cost+=min
            edge+=1
    print(f"MINIMUM COST IS : {cost}")
    return
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prims(graph)
