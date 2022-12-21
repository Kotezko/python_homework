# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = [2, 3, 4, 5, 6]


posMin = 0
posMax = len(n) - 1
mid = int(len(n) / 2)
print(mid)
while (posMin <= mid and posMax >= mid):
    result = n[posMin] * n[posMax]
    print(f"произведение пар чисел на позициях {posMin} и {posMax} = {result}")
    posMin+=1
    posMax-=1
