# Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)

import random 

nums = []
for i in range(-5, 5+1):
    nums.append(i)
print(f"список элементов: {nums}")
for i in nums:
    x = random.randint(0,len(nums)-1)
    y = nums[i]
    nums[i] = nums[x]
    nums[x] = y
print(f"список элементов после перемешивания: {nums}")
    