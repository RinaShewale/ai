from collections import deque

def bfs():
    start = ("A", "B", False, False)
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        monkey, box, on_box, banana = state

        if banana:
            print("Solution:")
            for x in path:
                print(x)
            return

        if monkey != box:
            new = (box, box, on_box, banana)
            if new not in visited:
                visited.add(new)
                queue.append((new, path + ["Move to box"]))

        if monkey == box and monkey != "C":
            new = ("C", "C", False, banana)
            if new not in visited:
                visited.add(new)
                queue.append((new, path + ["Push box to C"]))

        if monkey == box and not on_box:
            new = (monkey, box, True, banana)
            if new not in visited:
                visited.add(new)
                queue.append((new, path + ["Climb on box"]))

        if on_box and box == "C":
            new = (monkey, box, True, True)
            if new not in visited:
                visited.add(new)
                queue.append((new, path + ["Grab banana"]))

bfs()










# map_coloring_csp.py

colors = ["Red", "Green", "Blue"]

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

solve(list(graph.keys()))

print("Map Coloring:")
for node in color:
    print(node, ":", color[node])