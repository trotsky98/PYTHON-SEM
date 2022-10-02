# 1. Напишите программу, которая принимает на вход вещественное число
#    и показывает сумму его цифр. 

num = float(input())
sum_digits = 0

power = len(str(num)) - 2
num *= 10 ** power

while num:
    sum_digits += num % 10
    num //= 10

print(int(sum_digits))