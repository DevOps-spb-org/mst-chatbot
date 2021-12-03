from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp


class FSMUser(StatesGroup):
	name = State()
	position = State()
	
	
@dp.message_handler(commands='sign', state=None)
async def create_user(message: types.Message):
	await FSMUser.name.set()
	await message.reply("Введите имя")


@dp.message_handler(state=FSMUser.name)
async def load_name(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['name'] = message.text
	await FSMUser.next()
	await message.reply("Введи вашу должность")


@dp.message_handler(state=FSMUser.position)
async def load_position(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['position'] = message.text
	async with state.proxy() as data:
		await message.reply(str(data)) # TODO убрать и не возвращать данные пользователю
	await message.reply("Вы успешно зарегистрированы.")



	

def register_handlers_use(dp: Dispatcher):
	dp.register_message_handler(create_user, commands='sign', state=None)
	dp.register_message_handler(load_name, state=FSMUser.name)
	dp.register_message_handler(load_position, state=FSMUser.position)