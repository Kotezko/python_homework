import csv
import json
import os
os.chdir("les008")


def importCSV():
    count = 0
    dct = {}
    with open('database.csv', 'r', encoding = 'utf-8') as DB:     # считываем базу
        for line in DB:
            if line.strip()[0] != 'i':    # пропускаем "оглавление"
                count += 1
                list = line.strip().split(';') # строку в список
                list.pop(0) #отрезаем лишние id
                dct[count] = list # список в словарь
                print(dct)
    return dct # возвращаем словарь

def findPers(dct, request):
    res = {}
    requestWords = request.split()
    satisfyIndex = [0 for i in range(max(dct.keys()) + 1)] # Список для подсчёта совпадений
    for i in dct: # Проход по словарю
        for j in dct[i]: # Проход по элементам
            if request.lower().count(j.lower()):  # Ищем совпадения по объекту поиска
                satisfyIndex[i] += 1  # Считаем количество совпадений в каждом элементе словаря
    if max(satisfyIndex): # Проверка наличия совпадений
        if satisfyIndex.count(max(satisfyIndex)) > 1: # Проверка на несколько совпадений
            satisfyList = [i for i in range(len(satisfyIndex)) if satisfyIndex[i] == max(satisfyIndex)]
            for i in satisfyList:
                res[i] = dct[i]
        else: # Единственное совпадение
            maxIndex = satisfyIndex.index(max(satisfyIndex))
            res[maxIndex] = dct[maxIndex]
    else: # Неудачный поиск
        res[0] = ['Сотрудник не найден']
    return res

def writeData(data, fileName): #запись в бд
    with open(fileName, 'a', encoding = 'utf-8') as file:
        file.write(";".join(map(str, data)))
        file.write(f"\n")

def countData(name): # счетчик индекса
    with open(name, 'r', encoding = 'utf-8') as file:
        data = file.read()
    return data.count('\n')

def newPers():
    dct = dict()
    Id = countData("database.csv") 
    dct["id"] = Id
    dct["name"] = input('Имя: ')
    dct["surname"] = input('Фамилия: ')
    dct["position"] = input('Должность: ')
    dct["salary"] = input('Зарплата: ')
    return dct

def push_data():
    dct = newPers()
    writeData([dct.get("id"), dct.get("name"), dct.get("surname"), dct.get("position"), dct.get("salary")], "database.csv")

def expJSON():
    # путь к файлам БД
    # словарь, в который складываются записи из БД
    myList = []
    # открываем файл CSV на чтение
    with open('database.csv', 'r', encoding = 'utf-8') as dataBase:
        for line in dataBase:
            # запишем в список строки, кроме первой
            if line[0] != 'i':
                myList.append(line)
    # открываем или создаем файл JSON на запись
    with open('ExpDB.json', 'w+', encoding = 'utf-8') as jsonFile:
        # построчно записываем в формате JSON
        jsonFile.write('[')
        # переменная для подсчета количества записей
        Count = 0
        for item in myList:
            jsonFile.write('\n')
            jsonFile.write('    {' + '\n')
            jsonFile.write(f'        "id": {item.split(";")[0]},\n')
            jsonFile.write(f'        "name": {item.split(";")[1]},\n')
            jsonFile.write(f'        "surname": {item.split(";")[2]},\n')
            jsonFile.write(f'        "position": {item.split(";")[3]},\n')
            jsonFile.write(f'        "salary": {item.split(";")[4]}\n')
            Count += 1
            # определяем надо ли ставить запятую в конце
            if Count != len(myList):
                jsonFile.write('    },')
            else:
                jsonFile.write('    }')
        jsonFile.write('\n]')

def expTXT():
    # словарь, в который складываются записи из БД
    myList = []
    # открываем файл CSV на чтение
    with open("database.csv", 'r', encoding = 'utf-8') as dataBase:
        for line in dataBase:
            # запишем в список строки
            myList.append(line)
    # открываем или создаем файл TXT на запись
    with open("ExpDB.txt", 'w+', encoding = 'utf-8') as txtFile:
        # построчно записываем список
        for item in myList:
            txtFile.write(item)


