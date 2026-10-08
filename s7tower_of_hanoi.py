def hanoi(n, source, dest, temp):
    if n == 1:
        print(source, "->", dest)
        return

    hanoi(n-1, source, temp, dest)
    print(source, "->", dest)
    hanoi(n-1, temp, dest, source)

hanoi(3, "A", "C", "B")




# expert_system.py

temperature = int(input("Enter temperature: "))

if temperature > 30:
    print("It is Hot")
elif temperature < 15:
    print("It is Cold")
else:
    print("It is Normal")