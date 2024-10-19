tree = [[[5, 1, 2], [8, -8, -9]], [[9, 4, 5], [-3, 4, 3]]] 
root = 0 
pruned = 0 
def children(branch, depth, alpha, beta): 
    global tree, pruned 
    for i, child in enumerate(branch): 
        if isinstance(child, list): 
            nalpha, nbeta = children(child, depth + 1, alpha, beta) 
            if depth % 2 == 0: 
                alpha = max(alpha, nbeta) 
                branch[i] = alpha 
            else: 
                beta = min(beta, nalpha) 
        else: 
            if depth % 2 == 0: 
                alpha = max(alpha, child) 
            else: 
                beta = min(beta, child) 
            if alpha >= beta: 
                pruned += 1 
                break 
    if depth == root: 
        tree = alpha if root == 0 else beta 
    return alpha, beta 
def alphabeta(in_tree=tree, start=root, upper=-15, lower=15): 
    global pruned 
    alpha, beta = children(in_tree, start, upper, lower) 
    print(f"(alpha, beta): {alpha, beta}") 
    print(f"Result: {tree}") 
    print(f"Times pruned: {pruned}") 
    return alpha, beta, tree, pruned 
if __name__ == "__main__": 
    alphabeta()
