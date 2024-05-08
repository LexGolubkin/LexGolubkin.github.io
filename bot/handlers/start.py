from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

from configs.base import INDEX_HTML_PATH


shop = Router(name=__name__)


@shop.message(CommandStart())
async def start_command_processing(message: Message):
    to_shop = 'В магазин'
    info = 'О боте'

    to_shop_btn = KeyboardButton(text=to_shop, web_app=WebAppInfo(url=INDEX_HTML_PATH))
    info_btn = KeyboardButton(text=info)
    markup = ReplyKeyboardMarkup(keyboard=[[to_shop_btn],
                                           [info_btn]], resize_keyboard=True)
    # markup = InlineKeyboardMarkup(inline_keyboard=[])
    # markup.add(InlineKeyboardButton(text=to_shop, web_app=WebAppInfo(url=INDEX_HTML_PATH)))
    await message.answer(text='Выберите действие', reply_markup=markup)


@shop.message(content_types=['web_app_data'])
async def web_app_data_processing(message: Message):
    await message.answer(message.web_app_data.data)
