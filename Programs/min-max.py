def minimax(depth, nodeIndex, maximizingPlayer, values):
    # Leaf node condition
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -1000
        for i in range(2):
            value = minimax(depth + 1, nodeIndex * 2 + i, False, values)
            best = max(best, value)
        return best
    else:
        best = 1000
        for i in range(2):
            value = minimax(depth + 1, nodeIndex * 2 + i, True, values)
            best = min(best, value)
        return best


# ---------- USER INPUT ----------
values = list(map(int, input("Enter 8 leaf node values (space separated): ").split()))

result = minimax(0, 0, True, values)
print("Optimal value using Min-Max:", result)
