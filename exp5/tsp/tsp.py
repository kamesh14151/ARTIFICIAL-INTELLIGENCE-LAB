from itertools import permutations

# Distance matrix between cities
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def calculate_cost(path, dist):
    cost = 0
    for i in range(len(path) - 1):
        cost += dist[path[i]][path[i + 1]]
    cost += dist[path[-1]][path[0]]  # return to start
    return cost

def tsp_brute_force(dist):
    n = len(dist)
    cities = list(range(1, n))  # fix city 0 as start
    
    min_cost = float('inf')
    best_path = None

    for perm in permutations(cities):
        path = [0] + list(perm)
        cost = calculate_cost(path, dist)
        if cost < min_cost:
            min_cost = cost
            best_path = path

    best_path.append(0)  # return to start
    return tuple(best_path), min_cost

# Run TSP
path, cost = tsp_brute_force(dist)

print(f"Path: {path}")
print(f"Minimum Cost: {cost}")
