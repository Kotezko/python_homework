def showMenu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности(не готово)")
    print("3. Сделать выборку сотрудников по зарплате(не готово)")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника(не готово)")
    print("6. Обновить данные сотрудника(не готово)")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате txt")
    print("9. Закончить работу")
    return int(input("Введите номер необходимого действия: "))


def addPers():
    print("\nЗаполните необходимые данные\n")

def info(message):
    print(message)
    
def viewDB(DB):
    print("\nСписок сотрудников:\n")
    print("id name surname position salary")
    print("-"*31)
    for key in DB:
        print(key, end='. ')
        for j in DB[key]:
            print(j, end=' ')
        print()
    print()