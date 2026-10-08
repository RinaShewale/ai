import heapq

graph = {
    "V1": [("V2", 2), ("V3", 4)],
    "V2": [("V1", 2), ("V4", 3)],
    "V3": [("V1", 4), ("V4", 1), ("V5", 5)],
    "V4": [("V2", 3), ("V3", 1), ("V6", 2)],
    "V5": [("V3", 5), ("V6", 1)],
    "V6": [("V4", 2), ("V5", 1)]
}

h = {
    "V1": 7,
    "V2": 5,
    "V3": 3,
    "V4": 2,
    "V5": 1,
    "V6": 0
}

def astar(start, goal):
    q = [(h[start], 0, start, [start])]

    while q:
        f, cost, node, path = heapq.heappop(q)

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Cost:", cost)
            return

        for next_node, c in graph[node]:
            new_cost = cost + c
            heapq.heappush(q, (new_cost + h[next_node],
                               new_cost, next_node, path + [next_node]))

astar("V1", "V6")










map_coloring.py


colors = ["Red", "Green"]

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

color = {}

def valid(node, c):
    for n in graph[node]:
        if n in color and color[n] == c:
            return False
    return True

def solve(nodes):
    if not nodes:
        return True

    node = nodes[0]

    for c in colors:
        if valid(node, c):
            color[node] = c

            if solve(nodes[1:]):
                return True

            del color[node]

    return False

solve(list(graph))

for node in color:
    print(node, ":", color[node])