# python bot.py
import json
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

from konf import TOKEN


r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
data = json.loads(r.text)



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
    await message.answer (cg.get_price(ids=' bitcoin, ethereum, ravencoin, ripple, Binance coin', vs_currencies='usd'))

@dp.message_handler(Text(equals="Фиат"))
async def fiat(message: types.Message):
    if (r.status_code == 200):
        r.encoding = 'utf-8'
    await message.reply (data['Valute']['USD']['Name'], "=", data['Valute']['USD']['Value'])

if __name__ == '__main__':
    executor.start_polling(dp)
