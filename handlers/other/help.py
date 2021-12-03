from aiogram.types import Message
from loader import dp


@dp.message_handler(commands='help')
async def help(message: Message):
	await message.answer(f"""
	Список команд:
	/sing - зарегистрировать нового пользователя
	/profile -  покажет информацию о пользователе
	""", reply=False)
	
	