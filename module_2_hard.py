import random

n = random.randint(3, 20)
list_ = []

for i in range(1, n):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            list_.append(i)
            list_.append(j)
print(f"Число - {n}")
print(*list_, sep="")