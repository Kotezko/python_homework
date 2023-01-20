# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
import random 
def gamerMove(gamer, quantity):
    move = int(input(f"{gamer}, осталось {quantity}, сколько конфет возьмешь? "))
    quantity -= move
    return quantity

def botMove(quantity):
    move = quantity % 29
    if move == 0:
        move = random.randrange(1, 28) if quantity >= 28 else quantity
    print(f'Бот забрал {move} конфет')
    quantity -= move
    return quantity


mode = int(input("выберете режим игры 1 - игрок vs игрокб 2 - игрок vs бот"))
quantity = 2021 # количество конфет
if mode == 1: 
    gamer1 = input("введите имя: ")
    gamer2 = input("введите имя: ")
    move = random.randrange(1,3)
    if move == 1: print(f"ходит {gamer1}")
    else: 
        gamer1,gamer2 = gamer2,gamer1
        print(f"ходит {gamer1}")
    while quantity>0:
        if quantity>28:
            quantity = gamerMove(gamer1, quantity)
            if quantity>28:
                quantity = gamerMove(gamer2, quantity)
            else:
                print(f"осталось {quantity}, победил {gamer2}")
                break
        else:
            print(f"осталось {quantity}, победил {gamer1}")
            break
elif mode == 2:
    gamerVsBot = input("введите имя: ")
    move = random.randrange(1,3)
    if move == 1: 
        print(f"ходит {gamerVsBot}")
        while quantity>0:
            if quantity>28:
                quantity = gamerMove(gamerVsBot, quantity)
                if quantity>28:
                    move2 = random.randrange(1,29)
                    print(f"бот берет {move2} конфет")
                    quantity -= move2
                else:
                    print(f"осталось {quantity}, победил бот")
                    break
            else:
                print(f"осталось {quantity}, победил {gamerVsBot}")
                break
    else: 
        print(f"ходит бот")
        while quantity>0:
            if quantity>28:
                move2 = random.randrange(1,29)
                print(f"бот берет {move2} конфет")
                quantity -= move2
                if quantity>28:
                    quantity = gamerMove(gamerVsBot, quantity)
                else:
                    print(f"осталось {quantity}, победил {gamerVsBot}")
                    break
            else:
                print(f"осталось {quantity}, победил бот")
                break
else:
    gamerVsBot = input("введите имя: ")
    move = random.randrange(1,3)
    if move == 1: 
        print(f"ходит {gamerVsBot}")
        while quantity>0:
            if quantity>28:
                quantity = gamerMove(gamerVsBot, quantity)
                if quantity>28:
                    quantity = botMove(quantity)
                else:
                    print(f"осталось {quantity}, победил бот")
                    break
            else:
                print(f"осталось {quantity}, победил {gamerVsBot}")
                break
    else:
        print(f"ходит бот")
        while quantity>0:
            if quantity>28:
                quantity = botMove(quantity)
                if quantity>28:
                    quantity = gamerMove(gamerVsBot, quantity)
                else:
                    print(f"осталось {quantity}, победил {gamerVsBot}")
                    break
            else:
                print(f"осталось {quantity}, победил бот")
                break
