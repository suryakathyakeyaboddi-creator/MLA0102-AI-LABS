def dfs(graph, node, visited):
    print(node, end=" ")
    visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)
# User Input
graph = {}
n = int(input("Enter number of nodes: "))
for _ in range(n):
    node = input("Enter node: ")
    neighbours = input(f"Enter neighbours of {node} (space separated): ").split()
    graph[node] = neighbours
start = input("Enter start node: ")
visited = set()
print("DFS Traversal:", end=" ")
dfs(graph, start, visited)