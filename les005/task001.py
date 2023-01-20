# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


text = input("введите текст: ")
s= list(text.split())
# for i in s:
#     if "абв"in i:
#         s.remove(i)
b = filter(lambda x: "абв" not in x, s)
print(" ".join(b))