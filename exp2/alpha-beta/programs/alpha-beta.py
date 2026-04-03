def alphabeta(depth, node_index, is_max, values, max_depth, alpha, beta):
    
    if depth == max_depth:
        return values[node_index]

    if is_max:
        best = float('-inf')
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i,
                            False, values, max_depth, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            
            if beta <= alpha:
                break
        return best

    else:
        best = float('inf')
        for i in range(2):
            val = alphabeta(depth + 1, node_index * 2 + i,
                            True, values, max_depth, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

           
            if beta <= alpha:
                break
        return best



values = [3, 5, 6, 9, 1, 2, 0, -1]
tree_depth = 3

result = alphabeta(0, 0, True, values, tree_depth,
                   float('-inf'), float('inf'))

print("Optimal value using Alpha-Beta:", result)
                                                                                                                                                                                                                                                                                                                                                                                                            
