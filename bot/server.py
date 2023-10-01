import asyncio
import logging
import sys

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


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    reply_builder = ReplyKeyboardBuilder()
    reply_builder.add(types.KeyboardButton(text="Купить", web_app=WebAppInfo(url="https://tprvx.github.io/", input_placeholder="Нажмите кнопку Купить...")))
    reply_builder.adjust(1)
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=reply_builder.as_markup(resize_keyboard=True))


@dp.message()
async def echo_handler(message: types.Message) -> None:
    message.chat.id
    inline_builder = InlineKeyboardBuilder()
    inline_builder.row(types.InlineKeyboardButton(
        text="Купить", web_app=WebAppInfo(url="https://tprvx.github.io/")
    ))
    try:
        await bot.send_message(
            chat_id=message.chat.id,
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
