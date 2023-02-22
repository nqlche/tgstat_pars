from telegram_channels import get_data
from aiogram import Bot, Dispatcher
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup)
from aiogram.filters import Command, Text
from config import TOKEN_API
from aiogram import F
from aiogram.types import FSInputFile
import asyncio

# start bot
bot = Bot(token=TOKEN_API)
dp = Dispatcher()

button_1: KeyboardButton = KeyboardButton(text='/help')
keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    keyboard=[[button_1]],
    resize_keyboard=True,
    one_time_keyboard=True)


@dp.message(Command(commands=['start']))
async def cmd_start(message: Message):
    await message.answer(text='Этот бот умеет парсить топ 100 чатов с tgstat.ru\n'
                              'Введите ссылку на категорию c чатами', reply_markup=keyboard)


@dp.message(F.text.startswith('https'))
async def parser(message: Message):
    await message.answer(text='Работаю...')
    get_data(message.text)
    file = FSInputFile('../bot/chats.csv')
    await bot.send_document(document=file, chat_id=message.chat.id)


@dp.message(Command(commands=['help']))
async def love(message: Message):
    await message.answer(
        text='<i>Бот умеет парсить любые категории чатов с сайте tgstat, также поддерживается любая сортировка</i>',
        parse_mode='html')


@dp.message()
async def foo(message: Message):
    await message.reply(text='Я понимаю только ссылки на tgstat и то не все 😭')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
