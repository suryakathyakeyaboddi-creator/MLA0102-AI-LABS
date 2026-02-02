def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -1000
        for i in range(2):
            val = alpha_beta(depth+1, nodeIndex*2+i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 1000
        for i in range(2):
            val = alpha_beta(depth+1, nodeIndex*2+i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


# -------- USER INPUT --------
values = list(map(int, input("Enter 8 leaf node values (space separated): ").split()))

result = alpha_beta(0, 0, True, values, -1000, 1000)
print("Optimal value using Alpha-Beta Pruning:", result)
