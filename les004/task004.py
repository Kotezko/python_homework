# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import os
os.chdir("les004")
import random 
k = int(input("введите число: "))
mn= ''
for i in range(k, 1, -1):
    mn += f'{random.randint(0,100)}x^{i} + '

with open('task004.txt', 'w') as data:
        data.write(mn + f'{random.randint(0,100)}x + {random.randint(0,100)} = 0')
