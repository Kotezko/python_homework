import view as v
import module as m

def start():
    Run = True
    options = [findMember, position, salary, addMember, delMember, update, exportJson, expTxt, exit]
    while Run == True:
        # Выбор пользователя в меню:
        userIn = v.showMenu()-1 # v.showMenu заменить на модуль основного меню из windowsView
        if userIn < 0 or userIn > 8:
            v.info('\nОшибка ввода!\n')
        else:
            # Проверка на exit:
            if userIn == 8:
                # Меняем флаг для выхода из программы
                Run = False
            options[userIn]()
# 1
def findMember():
    request = input("что ищем? ")
    dataBase = m.importCSV() # словарь из БД
    res = m.findPers(dataBase, request)
    v.viewDB(res)

# 2
def position():
    
    return 0

# 3
def salary():

    return 0

# 4
def addMember():
    v.addPers()
    m.push_data()
    return v.info(f"\nСотрудник добавлен\n")

# 5
def delMember():

    return 0

# 6
def update():

    return 0

# 7
def exportJson():
    m.expJSON()
    v.info(f"\nФайл JSON создан\n")

# 8
def expTxt():
    m.expTXT()
    v.info(f"\nТекстовый файл создан")

# 9
def exit():

    v.info("Выход")
