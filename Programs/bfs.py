from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    print("BFS Traversal:", end=" ")
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
# User Input
graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ")
    neighbours = input(f"Enter neighbours of {node} (space separated): ").split()
    graph[node] = neighbours
start = input("Enter start node: ")
bfs(graph, start)
