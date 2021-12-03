from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


buttons =[
	InlineKeyboardButton(text="Поехали!!!", callback_data='Поехали!!!'),
	InlineKeyboardButton(text="Не хочу", callback_data='Не хочу')
	]

kb_start_stop = InlineKeyboardMarkup(row_width=2)
kb_start_stop.add(*buttons)
