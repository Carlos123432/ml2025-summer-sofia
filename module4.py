# Carlos Mendez, module4.py

N = int(input("Positive Integer: "))
numbers = []
for i in range(N):
    num = int(input("Enter number {i + 1}: "))
    numbers.append(num)

X = int(input("Enter the number to search for (X): "))

if X in numbers:
    print(numbers.index(X) + 1)
else:
    print(-1)