from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

btn_start_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
btn = ['Старт', 'Отмена']
btn_start_cancel.add(*btn)
