# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).


number = int(input())
if number not in [1, 2, 3, 4]:
    print('error')
elif number == 1:
    print('x > 0 and y > 0')
elif number == 2:
    print('x < 0 and y > 0')
elif number == 3:
    print('x < 0 and y < 0')
elif number == 4:
    print('x > 0 and y < 0')