# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# - 6 -> да
# - 7 -> да
# - 1 -> нет

n = int(input())
if  0 < n < 6:
    print("Workday")
elif 5 < n < 8:
        print("Weekend")
else:
    print("it s not a day of the week")