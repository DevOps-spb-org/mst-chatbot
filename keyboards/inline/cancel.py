from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


cancel_button = InlineKeyboardMarkup(row_width=1)
btn_cancel = InlineKeyboardButton(text="Отмена", callback_data='Отмена')
cancel_button.add(btn_cancel)
