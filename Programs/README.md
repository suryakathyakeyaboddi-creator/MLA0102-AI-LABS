## 1. Breadth First Search (BFS)

**Breadth First Search** explores a graph level by level. It starts from the root node and visits all neighboring nodes before moving to the next level.

### Pseudocode
BFS(Graph, Start)
create an empty queue
mark Start as visited
insert Start into queue

while queue is not empty
    node ← remove from queue
    visit node
    for each adjacent node
        if not visited
            mark visited
            insert into queue

---

## 2. Depth First Search (DFS)

**Depth First Search** explores a graph by going as deep as possible along a branch before backtracking.

### Pseudocode
DFS(Graph, Node)
mark Node as visited
visit Node

for each adjacent node
    if not visited
        DFS(Graph, adjacent node)

---

## 3. Uniform Cost Search (UCS)

**Uniform Cost Search** expands the node with the lowest path cost. It always guarantees the optimal solution when all costs are positive.

### Pseudocode
UCS(Graph, Start, Goal)
priority queue ← (0, Start)

while queue is not empty
    cost, node ← remove lowest cost node
    if node is Goal
        return solution path

    for each neighbor
        new_cost ← cost + edge cost
        insert neighbor with new_cost

---

## 4. Water Jug Problem

The **Water Jug problem** is a classic state space search problem. Each state represents the amount of water in two jugs.

### State Representation
(x, y)
x → amount of water in Jug A
y → amount of water in Jug B


### Pseudocode
WaterJug(jugA, jugB, target)
start from (0, 0)
use BFS to explore all states
avoid repeated states

if any state matches target
    return solution path

---

## 5. Greedy Best First Search (GBFS)

**GBFS** selects the next node based only on the heuristic value. It is fast but does not always guarantee the optimal path.

### Pseudocode
GBFS(Graph, Heuristic, Start, Goal)
priority queue ← (heuristic(Start), Start)

while queue not empty
    node ← lowest heuristic value
    if node is Goal
        return path

    expand node using heuristic values

---

## 6. Min-Max Algorithm

The **Min-Max algorithm** is used in two-player games. One player tries to maximize the score, while the other tries to minimize it.

### Pseudocode
MINIMAX(node, depth, maximizingPlayer)
if node is leaf or depth is zero
return node value

if maximizingPlayer
    return maximum of child values
else
    return minimum of child values

---

## 7. Alpha-Beta Pruning

**Alpha-Beta pruning** improves the Min-Max algorithm by removing branches that do not affect the final decision.

### Pseudocode
ALPHABETA(node, depth, alpha, beta, maximizingPlayer)
if depth is zero
return value

update alpha and beta
prune branches when beta ≤ alpha

---

## 8. Decision Tree (Rule-Based)

A **Decision Tree** uses simple IF–ELSE rules to make decisions based on input conditions.

### Pseudocode
DecisionTree(inputs)
if condition is true
return decision
else
return alternate decision


---

## 9. A* Search Algorithm

**A\*** is an informed search algorithm that combines path cost and heuristic value to find the optimal path.

### Formula
f(n) = g(n) + h(n)


### Pseudocode
AStar(Graph, Start, Goal)
initialize open list with Start
calculate f(n) for each node

select node with lowest f(n)
expand until Goal is reached
