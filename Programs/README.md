# 🧠 Artificial Intelligence Search & Decision Algorithms

This repository contains **standard implementations and pseudocode** of core **Artificial Intelligence algorithms** commonly taught in **AI courses, labs, exams, and interviews**.

The focus is on **clarity, correctness, and standard problem-solving structure**.

---

## 📌 Algorithms Covered

1. Breadth First Search (BFS)
2. Depth First Search (DFS)
3. Uniform Cost Search (UCS)
4. Water Jug Problem
5. Greedy Best First Search (GBFS)
6. Min-Max Algorithm
7. Alpha-Beta Pruning
8. Decision Tree (Rule-Based)
9. A* Search Algorithm

---

## 1️⃣ Breadth First Search (BFS)

### 🔹 Idea
Explores nodes **level by level** using a queue.

### 🔸 Pseudocode
BFS(Graph, Start)
create empty queue
mark Start as visited
enqueue Start

while queue not empty
    node ← dequeue
    process node
    for each neighbor of node
        if not visited
            mark visited
            enqueue neighbor


---

## 2️⃣ Depth First Search (DFS)

### 🔹 Idea
Explores as **deep as possible** before backtracking.

### 🔸 Pseudocode


DFS(Graph, Node)
mark Node as visited
process Node

for each neighbor of Node
    if not visited
        DFS(Graph, neighbor)


---

## 3️⃣ Uniform Cost Search (UCS)

### 🔹 Idea
Expands the **lowest path cost** node first.

### 🔸 Pseudocode


UCS(Graph, Start, Goal)
priority_queue ← (cost=0, Start)

while queue not empty
    cost, node ← pop lowest cost
    if node is Goal
        return path

    for each neighbor
        new_cost ← cost + edge_cost
        push (new_cost, neighbor)


---

## 4️⃣ Water Jug Problem (State Space Search)

### 🔹 Idea
Use BFS to reach a state where one jug has the target amount.

### 🔸 State Representation


(x, y)
x → water in jug A
y → water in jug B


### 🔸 Pseudocode


WaterJug(jugA, jugB, target)
start_state ← (0, 0)
queue ← start_state
visited ← empty

while queue not empty
    state ← dequeue
    if state matches target
        return solution

    generate all valid next states
    add unvisited states to queue


---

## 5️⃣ Greedy Best First Search (GBFS)

### 🔹 Idea
Chooses node with **lowest heuristic value only**.

### 🔸 Pseudocode


GBFS(Graph, Heuristic, Start, Goal)
priority_queue ← (h(Start), Start)

while queue not empty
    node ← pop lowest heuristic
    if node is Goal
        return path

    for each neighbor
        add neighbor based on heuristic


---

## 6️⃣ Min-Max Algorithm

### 🔹 Idea
Used in **two-player games** to choose optimal move.

### 🔸 Pseudocode


MINIMAX(node, depth, maximizingPlayer)
if depth == 0 or node is terminal
return node value

if maximizingPlayer
    best ← -∞
    for each child
        best ← max(best, MINIMAX(child))
    return best
else
    best ← +∞
    for each child
        best ← min(best, MINIMAX(child))
    return best


---

## 7️⃣ Alpha-Beta Pruning

### 🔹 Idea
Optimizes Min-Max by **pruning unnecessary branches**.

### 🔸 Pseudocode


ALPHABETA(node, depth, alpha, beta, maximizingPlayer)
if depth == 0
return value

if maximizingPlayer
    for each child
        alpha ← max(alpha, ALPHABETA(child))
        if beta ≤ alpha
            break
    return alpha
else
    for each child
        beta ← min(beta, ALPHABETA(child))
        if beta ≤ alpha
            break
    return beta


---

## 8️⃣ Decision Tree (Rule-Based)

### 🔹 Idea
Decision making using **IF–ELSE rules**.

### 🔸 Pseudocode


DecisionTree(inputs)
if condition1
if condition2
return decision A
else
return decision B
else
return decision C


---

## 9️⃣ A* Search Algorithm

### 🔹 Idea
Uses **cost + heuristic** to find optimal path.

### 🔸 Formula


f(n) = g(n) + h(n)


### 🔸 Pseudocode


AStar(Graph, Start, Goal)
open_list ← Start
g(Start) ← 0

while open_list not empty
    node ← lowest f(n)
    if node is Goal
        return path

    for each neighbor
        tentative_g ← g(node) + cost
        if better path found
            update costs
            add neighbor to open_list


