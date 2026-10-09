#s2water_jug_bfs.py
from collections import deque

q = deque([(0, 0)])
visited = {(0, 0)}

while q:
    a, b = q.popleft()
    print(a, b)

    if a == 2:
        print("Goal Reached")
        break

    for s in [
        (4, b), (a, 3), (0, b), (a, 0),
        (a - min(a, 3-b), b + min(a, 3-b)),
        (a + min(b, 4-a), b - min(b, 4-a))
    ]:
        if s not in visited:
            visited.add(s)
            q.append(s)




# game_tree.py

class Node:
    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

def show(node, level=0):
    print("  " * level + node.name)
    for child in node.children:
        show(child, level + 1)

# Build tree in a clean, nested structure
root = Node("A", [
    Node("B", [Node("D"), Node("E")]),
    Node("C", [Node("F"), Node("G")])
])

print("Game Tree:")
show(root)






#s6 knowledge_graph.py


graph = {
    "Rina": ["Student", "Python"],
    "Python": ["Programming Language"],
    "Student": ["College"]
}

def show_graph():
    for entity, relations in graph.items():
        for relation in relations:
            print(entity, "->", relation)

show_graph()