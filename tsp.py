from itertools import permutations

def tsp(graph,start):
    n = len(graph)
    cities = [i for i in range(n) if i != start]
    bc = float('inf')
    bp =  []
    for perm in permutations(cities):
        path = [start] + list(perm) + [start]
        cost = 0
        for i in range(len(path)-1):
            cost += graph[path[i]][path[i+1]]
        if cost<bc:
            bc = cost
            bp = path
    return bc,bp
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
path, cost = tsp(graph, 0)
print("Best path:", path)
print("Min cost:", cost)