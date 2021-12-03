from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


create_quiz = ReplyKeyboardMarkup(resize_keyboard=True)
btn_create = ["Создать опрос", "Отмена"]
create_quiz.add(*btn_create)


