import heapq

def gbfs(graph, heuristic, start, goal):
    visited = set()
    priority_queue = []
    
    # (heuristic value, node)
    heapq.heappush(priority_queue, (heuristic[start], start))
    parent = {start: None}

    while priority_queue:
        _, current = heapq.heappop(priority_queue)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
                parent[neighbor] = current

    return None


# ---------- USER INPUT ----------
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

heuristic = {
    'A': 4,
    'B': 2,
    'C': 1,
    'D': 0
}

start = input("Enter start node: ").upper()
goal = input("Enter goal node: ").upper()

path = gbfs(graph, heuristic, start, goal)
print("Path using Greedy Best First Search:", path)
