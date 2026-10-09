from collections import deque

queue = deque(["Monkey at Door"])
visited = []
while queue:
    state = queue.popleft()
    if state not in visited:
        visited.append(state)
        print(state)
        if state == "Monkey at Door":
            queue.append("Monkey at Box")
        elif state == "Monkey at Box":
            queue.append("Box Under Banana")
        elif state == "Box Under Banana":
            queue.append("Monkey Climbs Box")
        elif state == "Monkey Climbs Box":
            queue.append("Monkey Gets Banana")
print("Goal Reached")








colors = ["Red", "Green", "Blue"]

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}

color = {}

def solve(nodes):
    if not nodes:
        return True
    
    node = nodes[0]
    for c in colors:
        # Check if any neighbor already has this color
        if all(color.get(n) != c for n in graph[node]):
            color[node] = c
            if solve(nodes[1:]):
                return True
            del color[node]  # Backtrack
            
    return False

solve(list(graph.keys()))

print("Map Coloring:")
for node, col in color.items():
    print(f"{node} : {col}")