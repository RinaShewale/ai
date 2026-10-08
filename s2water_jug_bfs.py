#s2water_jug_bfs.py
from collections import deque

def bfs():
    q = deque([(0, 0)])
    visited = set()

    while q:
        a, b = q.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        print(a, b)

        if a == 2:
            print("Goal Reached")
            return

        states = [
            (4, b),
            (a, 3),
            (0, b),
            (a, 0),
            (a - min(a, 3-b), b + min(a, 3-b)),
            (a + min(b, 4-a), b - min(b, 4-a))
        ]

        for state in states:
            if state not in visited:
                q.append(state)

bfs()







# game_tree.py

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, node):
        self.children.append(node)

def show(node, level=0):
    print("  " * level + node.name)

    for child in node.children:
        show(child, level + 1)

root = Node("A")

b = Node("B")
c = Node("C")

d = Node("D")
e = Node("E")
f = Node("F")
g = Node("G")

root.add(b)
root.add(c)

b.add(d)
b.add(e)

c.add(f)
c.add(g)

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