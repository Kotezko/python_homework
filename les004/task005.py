# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
import re
import os
os.chdir("les004")

with open('task005_1.txt','r') as data:
    mn_1 = data.readline()
    list_of_mn_1 = re.split('[x,^,+, ]+', mn_1)
with open('task005_2.txt','r') as data:
    mn_2 = data.readline()
    list_of_mn_2 = re.split('[x,^,+, ]+', mn_2)
sum_mn = []
mn=''
j=0
for i in range(0,len(list_of_mn_1), 2):
    sum_mn.append(int(list_of_mn_1[i]) + int(list_of_mn_2[i]))
for i in range(len(sum_mn), 1, -1):
    mn += f'{sum_mn[j]}x^{i} + '
    j+=1
with open('task005_sum.txt', 'w') as data:
    data.write(mn + f'{sum_mn[len(sum_mn)-1]}x + {int(list_of_mn_1[len(list_of_mn_1)-1]) + int(list_of_mn_2[len(list_of_mn_2)-1])}')


# print(f'({mn_1})+({mn_2})')
# with open('sum_mn.txt', 'w') as data:
#     data.write(f'({mn_1})+({mn_2})')