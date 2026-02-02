from collections import deque
def water_jug(jug1, jug2, target):
    visited = set()
    queue = deque()
    queue.append((0, 0))
    parent = {}
    parent[(0, 0)] = None
    visited.add((0, 0))
    while queue:
        x, y = queue.popleft()
        if x == target or y == target:
            path = []
            current = (x, y)
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]
        next_states = [
            (jug1, y),  
            (x, jug2), 
            (0, y),    
            (x, 0),    
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   
        ]
        for state in next_states:
            if state not in visited:
                visited.add(state)
                parent[state] = (x, y)
                queue.append(state)

    return None
jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))
result = water_jug(jug1, jug2, target)
if result:
    print("\nSteps to reach the target:")
    for step in result:
        print(step)
else:
    print("Target amount cannot be measured.")
