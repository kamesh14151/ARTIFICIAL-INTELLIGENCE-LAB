import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    parent = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor, cost in graph[current]:
            new_cost = g_cost[current] + cost

            if new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = current

    return None


# Graph
graph = {
    'A': [('C', 1), ('B', 5)],
    'C': [('B', 1)],
    'B': []
}

# Heuristic
heuristic = {
    'A': 2,
    'C': 1,
    'B': 0
}

# Run A*
result = a_star(graph, 'A', 'B', heuristic)

print("Shortest path:", result)
