# by Hemenguelbindi
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from filters.users import NewUser
from loader import dp


@dp.message_handler(commands='sign', state=None)
async def create_user(message: types.Message):
	await NewUser.name.set()
	await message.answer("Введите имя в формате ФИО на русском")


@dp.message_handler(state=NewUser.name)
async def load_name(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['name'] = message.text
	await NewUser.next()
	await message.answer("Введи вашу должность")


@dp.message_handler(state=NewUser.position)
async def load_position(message: types.Message, state: FSMContext):
	"""
	:return: position and all input user
	"""
	async with state.proxy() as data:
		data['position'] = message.text
	# async with state.proxy() as data:
	# await message.answer(str(data)) # TODO убрать и не возвращать данные пользователю
	await state.finish()
	await message.answer("Вы успешно зарегистрированы.")
	await message.answer("Теперь пройдем не большой тест, чтобы узнать проблемные зоны!")



	


# def register_handlers_use(dp: Dispatcher):
# 	"""
# 		регистрация handlers
# 	"""
# 	dp.register_message_handler(create_user, commands='sign', state=None)
# 	dp.register_message_handler(load_name, state=NewUser.name)
# 	dp.register_message_handler(load_position, state=NewUser.position)