import asyncio
import logging
import sys
import ast

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.markdown import hbold

import config

TOKEN = config.MAIN["telegram_bot_token"]
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

web_app_url = "https://tprvx.github.io/#"


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    reply_builder = ReplyKeyboardBuilder()
    reply_builder.add(types.KeyboardButton(text="Регистрация", web_app=WebAppInfo(url=f"https://tprvx.github.io/#/form", input_placeholder="Нажмите кнопку Купить...")))
    reply_builder.adjust(1)
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=reply_builder.as_markup(resize_keyboard=True))


@dp.message()
async def echo_handler(message: types.Message) -> None:
    chat_id = message.chat.id
    if message.web_app_data is not None:
        reg_data = ast.literal_eval(message.web_app_data.data)
        await bot.send_message(chat_id, f"Отлично! Мы узнали что ваша страна <b>{reg_data['country']}</b>, город <b>{reg_data['street']}</b>, и вы <b>{reg_data['subject']}</b>!")
    inline_builder = InlineKeyboardBuilder()
    inline_builder.row(types.InlineKeyboardButton(
        text="Купить", web_app=WebAppInfo(url=f"https://tprvx.github.io/#/products")
    ))
    try:
        await bot.send_message(
            chat_id=chat_id,
            text=f"{hbold(message.from_user.full_name)}, воспользуйся нашими услугами, нажав кнопку ниже👇",
            reply_markup=inline_builder.as_markup()
        )
    except Exception as e:
        print(e)
        await message.answer("Nice try!")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
