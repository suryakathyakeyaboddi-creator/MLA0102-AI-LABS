import heapq
def ucs(graph, start, goal):
    pq = [(0, start)]
    visited = set()
    while pq:
        cost, node = heapq.heappop(pq)
        if node in visited:
            continue
        print(f"Visiting {node} with cost {cost}")
        visited.add(node)
        if node == goal:
            print("Goal reached with total cost:", cost)
            return
        for neighbour, weight in graph[node]:
            if neighbour not in visited:
                heapq.heappush(pq, (cost + weight, neighbour))
    print("Goal not reachable")
# User Input
graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ")
    edges = int(input(f"Enter number of edges from {node}: "))
    graph[node] = []
    for _ in range(edges):
        neighbour, weight = input("Enter neighbour and cost: ").split()
        graph[node].append((neighbour, int(weight)))
start = input("Enter start node: ")
goal = input("Enter goal node: ")
ucs(graph, start, goal)
