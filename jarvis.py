# python jarvis.py

import json
import requests
from aiogram import Bot, types, Dispatcher
from aiogram.dispatcher.filters import Text
from pycoingecko import CoinGeckoAPI
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from konf import TOKEN

cg = CoinGeckoAPI()


# цикл для отправки запросов на сайт
def cripta():
    if (cg.status_code == 200):
        cg.encoding = 'utf-8'


btc = (cg.get_price(ids=' bitcoin', vs_currencies='usd'))  # достаем валюту в словарь
btc1 = btc.get('bitcoin')  # достаем значение из словаря - биток
btc2 = btc1.get('usd')

eth = (cg.get_price(ids=' ethereum', vs_currencies='usd'))  # достаем валюту в словарь
eth1 = eth.get('ethereum')  # достаем значение из словаря - эфир
eth2 = eth1.get('usd')

zec = (cg.get_price(ids=' zcash', vs_currencies='usd'))  # достаем валюту в словарь
zec1 = zec.get('zcash')  # достаем значение из словаря - зедкеш
zec2 = zec1.get('usd')

# импорт курсов фиата
r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')


# обрабатываем Джсон по фиату
def fiat():  # цикл для отправки запросов на сайт
    if (r.status_code == 200):
        r.encoding = 'utf-8'


data = json.loads(r.text)

u = (data['Valute']['USD']['Value'])
e = (data['Valute']['EUR']['Value'])

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# кнопки
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Крипта", "Фиат"]
    keyboard.add(*buttons)
    await message.reply("Какие курсы интересуют?", reply_markup=keyboard)


# from aiogram.dispatcher.filters import Text
@dp.message_handler(Text(equals="Крипта"))
async def crypto(message: types.Message):
    await message.reply('Btc: ' + str(btc2) + ",  " + "Eth: " + str(eth2) + ', ' \
                        + 'Zec: ' + str(zec2))  # вывод цены крипты


@dp.message_handler(Text(equals="Фиат"))
async def fiat(message: types.Message):
    if (r.status_code == 200):
        r.encoding = 'utf-8'
    await message.reply('Usd: ' + str(u) + ",  " + 'Eur: ' + str(e))  # вывод цены фиата


if __name__ == '__main__':
    executor.start_polling(dp)

