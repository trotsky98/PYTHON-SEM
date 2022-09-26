# 2. Напишите программу, которая на вход принимает 
# 5 чисел и находит максимальное из них.

max = 0
for i in range(5):
    n = int(input())
    if n > max:
        max = n
print(max)