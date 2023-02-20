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

button_1: KeyboardButton = KeyboardButton(text='❤️')
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
    file = FSInputFile('../botinki/chats.csv')
    await bot.send_document(document=file, chat_id=message.chat.id)


@dp.message(Text(text='❤️'))
async def love(message: Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo='https://sun9-8.userapi.com/c845524/v845524953/742a0/WezZEhFte10.jpg')


@dp.message()
async def foo(message: Message):
    await message.reply(text='Я понимаю только ссылки на tgstat и то не все 😭')


async def main():
    get_data(url='https://tgstat.ru/ratings/chats/business?sort=members')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
