from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from loader import dp


class FSMAmin(StatesGroup):
	name = State()
	description = State()


@dp.message_hendler(commands='Загрузить', state=None)
async def cm_start(message: types.Message):
	await FSMAmin.name.set()
	await message.reply('Введи название')


# @dp.message_handler(content_types=['photo'], state=FSMAmin.photo)
# async def load_photo(message: types.Message, state: FSMContext):
# 	async with state.proxy() as data:
# 		data['photo'] =message.photo[0].file_id
# 	await FSMAmin.next()
# 	await message.reply("Tеперь введи назварние")
	
	
@dp.message_handler(state=FSMAmin.description)
async def load_name(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['name'] = message.text
	await FSMAmin.next()
	await message.reply("Введи описание")


@dp.message_handler(state=FSMAmin.description)
async def load_description(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['discription'] = message.text
	await state.finish()
	
	