# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

n= int(input("введите число "))
# result= 0
# for i in range(1,n+1):
#     result += (1+1/i)**i
# print(round(result, 2))

lst = [(1+1/i)**i for i in range(1,n+1)]
print(round(sum(lst),2))