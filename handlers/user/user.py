# by Hemenguelbindi
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from filters.users import NewUser, FirstQuiz
from keyboards.common import btn_start_cancel
from loader import dp


# Начало регистрации пользователя
@dp.message_handler(commands='sign', state=None)
async def create_user(message: types.Message):
	await NewUser.name.set()
	await message.answer("Введите имя в формате ФИО на русском", reply_markup=btn_start_cancel)
	
	
@dp.message_handler(Text(equals="Отмена"), state=NewUser)
async def cancel(message: types.Message, state: FSMContext):
	"""Отмена регистрации"""
	await message.answer("Вы отказались от регистрации, а жаль\
	на есть чему вас научить", reply_markup=types.ReplyKeyboardRemove())
	await state.reset_state()


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
	await message.answer("Теперь пройдем не большой тест, чтобы узнать проблемные зоны!\
	Что бы начать тест нажми на кнопу старт, елси нет тогда нажми отмена", reply_markup=btn_start_cancel)
# Конец регитрации


# Начало опроса
@dp.message_handler(Text(equals='Отмена'))
async def start_quiz(message: types.Message):
	await message.answer("Вот не задача а вам нужно все таки пройти это!", reply_markup=types.ReplyKeyboardRemove())
	
	
@dp.message_handler(text='Старт')
async def start_quiz(message: types.Message):
	await message.answer("Чего ждать приступим!", reply_markup=types.ReplyKeyboardRemove())
	



# def register_handlers_use(dp: Dispatcher):
# 	"""
# 		регистрация handlers
# 	"""
# 	dp.register_message_handler(create_user, commands='sign', state=None)
# 	dp.register_message_handler(load_name, state=NewUser.name)
# 	dp.register_message_handler(load_position, state=NewUser.position)