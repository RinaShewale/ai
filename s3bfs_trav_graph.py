from collections import deque

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8, 9],
    5: [10, 11],
    6: [12, 13],
    7: [14, 15]
}

def bfs(start):
    queue = deque([start])
    visited = set()

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            for n in graph.get(node, []):
                queue.append(n)

bfs(1)







# alpha_beta.py

def alphabeta(node, depth, alpha, beta, maximizing):
    if depth == 0:
        return node

    if maximizing:
        value = -999
        for child in node:
            value = max(value, alphabeta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    else:
        value = 999
        for child in node:
            value = min(value, alphabeta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value

tree = [
    [[3, 5], [2, 9]],
    [[0, 7]]
]

print("Best Value:", alphabeta(tree, 2, -999, 999, True))