# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
x = int(input('введите номер четверти: '))
if x > 0 and x < 5:
    if (x == 1):
        print("диапазон 1 четверти x>0 и y>0")
    elif (x == 2):
        print("диапазон 2 четверти x<0 и y>0")
    elif (x == 3):
        print("диапазон 3 четверти x<0 и y<0")
    elif (x == 4):
        print("диапазон 4 четверти x>0 и y<0")
else:
    print("не верный номер четверти")