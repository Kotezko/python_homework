
# Ввод данных

# Создать новый контакт
def add_new():
    name = input('Name: ')
    phone = input('Phone number: ')
    return (name, phone)


# Поиск телефона в списке контактов
def find_phone():
    return input('Name: ')


# Основное меню
def show_menu():
    return input('1 - создать новый контакт\n' \
                   '2 - найти контакт\n' \
                   '3 - экспортировать контакт в txt\n' \
                   '4 - экспортировать контакт в xml\n' \
                   '0 - выход\n')




# Вывод данных на экран

def view_res(res):
    print(f"{res}\n")