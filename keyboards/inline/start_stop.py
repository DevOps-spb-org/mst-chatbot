from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


buttons =[
	InlineKeyboardButton(text="старт"),
	InlineKeyboardButton(text="отмена")
	]

kb_start_stop = InlineKeyboardMarkup(row_width=2)
kb_start_stop.add(*buttons)
