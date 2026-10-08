def f(x):
    return -x*x + 4*x

x = 0

while True:
    current = f(x)
    right = f(x + 1)
    left = f(x - 1)

    if right > current:
        x += 1
    elif left > current:
        x -= 1
    else:
        break

print("x =", x)
print("Maximum =", f(x))















# map_coloring.py

colors = ["Red", "Green", "Blue"]

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "E"],
    "D": ["B", "E"],
    "E": ["C", "D"]
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

for n in color:
    print(n, ":", color[n])