from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                              resize_keyboard=True)
button_1: KeyboardButton = KeyboardButton('❤️')
kb.add(button_1)
