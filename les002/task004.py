# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в отдельном списке( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].

n= int(input("введите число: "))
nums = []
result=1
positions = [3,1,4]
for i in range(-n, n+1):
    if i !=0:  # только если нужно убрать ноль, как в примере
        nums.append(i)
print(f"список элементов: {nums}")
for i in positions:
    result *= nums[i]
print(f"результат умножения элементов списка находящихся на позициях{positions} = {result}")