from aiogram import Bot, types
import random
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

a = ['лазанья','жульен','карбонара','сырный суп','пирог']

btn1 = KeyboardButton("рыба")
btn2 = KeyboardButton("мясо")
btn3 = KeyboardButton("фрукты")
btn4 = KeyboardButton("овощи")
kbd = ReplyKeyboardMarkup(resize_keyboard=True)
kbd.add(btn1, btn2, btn3, btn4)

bot = Bot(token="7548509146:AAHS7ZZWslpNfN44YrZ13U5oN95HPbQuCO4")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(mes: types.Message):
    await mes.answer("Хай, это бот кулинар. \n"
                     "Чтобы выдать любой рецепт введите /random_dish \n"
                     "Чтобы посмотреть возможные блюда с вашими продуктами введите /products и выберите из панели нужный продукт")

@dp.message_handler(commands=['random_dish'])
async def random_dish(mes: types.Message):
    await mes.answer(random.choice(a))

@dp.message_handler(commands=['products'])
async def products(mes: types.Message):
    await mes.answer('выбери продукт')

'''
@dp.message_handler(contains=['мясо'])
async def
'''