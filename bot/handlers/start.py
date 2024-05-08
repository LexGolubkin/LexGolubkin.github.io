from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo


shop = Router(name=__name__)


@shop.message(CommandStart())
async def start_command_processing(message: Message):
    to_shop = 'В магазин'
    info = 'О боте'

    to_shop_btn = KeyboardButton(text=to_shop, web_app=WebAppInfo(url='https://github.com/LexGolubkin'))
    info_btn = KeyboardButton(text=info)
    markup = ReplyKeyboardMarkup(keyboard=[[to_shop_btn],
                                           [info_btn]], resize_keyboard=True)
    await message.answer(text='Выберите действие', reply_markup=markup)
