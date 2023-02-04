from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TG_TOKEN_API, OPEN_WEATHER_TOKEN_API
from random import randint
import datetime
import requests

storage = MemoryStorage()
bot = Bot(token=TG_TOKEN_API)
dp = Dispatcher(bot=bot, storage=storage)

class ClientStatesGroup(StatesGroup):
    weather = State()

help_descript = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>начало работы с ботом (показать клавиатуру)</em>
<b>/weather</b> - <em>показать погоду</em>
<b>/quit</b> - <em>закончить работу с ботом (скрыть клавиатуру)</em>"""

@dp.message_handler(commands="help")
async def help_command(message: types.Message):
    await message.reply(text=help_descript, parse_mode="HTML")

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    buttons = ["/help", "/weather", "/quit"]
    keyboard.add(*buttons)
    await message.reply("Добро пожаловать",reply_markup=keyboard)
    
@dp.message_handler(commands="quit")
async def knop1(message: types.Message):
    await message.reply("goodbye",reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands="weather", state=None)
async def start_command(message: types.Message):
    await ClientStatesGroup.weather.set()
    await message.reply("Привет! Напиши мне название города и я пришлю сводку погоды!")
    
@dp.message_handler(state=ClientStatesGroup.weather)
async def get_weather(message: types.Message, state: FSMContext):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={OPEN_WEATHER_TOKEN_API}&units=metric"
        )
        data = r.json()
        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно, не пойму что там за погода!"
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])
        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
            f"Погода в городе: {city}\nТемпература: {cur_weather}C° {wd}\n"
            f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
            f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
            f"***Хорошего дня!***"
            )
        await state.finish()
    except:
        await message.reply("\U00002716 Проверьте название города \U00002716")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)