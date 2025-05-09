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

bot = Bot(token="7602865776:AAFgZj1xO8VH4tCrR5O5AdJa7E1RcEx7g9A")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(mes: types.Message):
    await mes.answer("Хай, это бот кулинар. \n"
                     "Чтобы выдать любой рецепт введите /random_dish \n"
                     "Чтобы посмотреть возможные блюда с вашими продуктами введите /products и выберите из панели нужный продукт",
                     reply_markup=kbd)

@dp.message_handler(commands=['random_dish'])
async def random_dish(mes: types.Message):
    await mes.answer(random.choice(a))

@dp.message_handler(commands=['products'])
async def products(mes: types.Message):
    await mes.answer('выбери продукт')

@dp.message_handler(content_types="web_app_data")
async def get_data(web_app_message):
    global price
    begin = web_app_message.web_app_data.data.rfind(" ")
    end = web_app_message.web_app_data.data.rfind("$")
    price = web_app_message.web_app_data.data[begin + 1:end]
    await bot.send_message(web_app_message.chat.id,
                           web_app_message.web_app_data.data, reply_markup=buy_kb)

@dp.message_handler(filters.Text(contains="Оплатить"))
async def buy(message: types.Message):
    await message.answer(f"Спасибо за покупку на {price}$")

'''
@dp.message_handler(contains=['мясо'])
async def
'''

executor.start_polling(dp, skip_updates=True)