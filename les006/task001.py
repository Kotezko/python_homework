# Найти сумму чисел списка стоящих на нечетной позиции

a = [2, 3, 5, 9, 3]
lst = [a[i] for i in range(1, len(a), 2)]
print(lst)
print(f'{sum(lst)}')