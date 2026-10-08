def f(x):
    return -(x - 5) ** 2 + 25

x = 0

while True:
    current = f(x)
    left = f(x - 1)
    right = f(x + 1)

    if right > current:
        x = x + 1
    elif left > current:
        x = x - 1
    else:
        break

print("Maximum value:", f(x))
print("At x =", x)









# forward_chaining.py

facts = {"A", "B"}

rules = [
    ({"A", "B"}, "C"),
    ({"C"}, "D"),
    ({"D"}, "E")
]

while True:
    new_fact = False

    for condition, result in rules:
        if condition.issubset(facts) and result not in facts:
            facts.add(result)
            print(result)
            new_fact = True

    if not new_fact:
        break

print("Facts:", facts)








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