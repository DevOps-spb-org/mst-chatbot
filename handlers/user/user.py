# by Hemenguelbindi
from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from filters.users import NewUser, FirstQuiz
from keyboards.common import btn_start_cancel
from keyboards.inline import cancel_button, kb_start_stop
from loader import dp


# Начало регистрации пользователя
@dp.message_handler(commands='sign', state=None)
async def create_user(message: types.Message):
	await NewUser.name.set()
	await message.answer("Введите имя в формате ФИО на русском", reply_markup=cancel_button)
	
	
@dp.callback_query_handler(text_contains='Отмена', state=NewUser)
async def cancel(call: types.CallbackQuery, state: FSMContext):
	"""Отмена регистрации"""
	await call.answer("Вы отказались от регистрации, жаль нам есть чему вас научить", show_alert=True)
	await call.message.edit_reply_markup()
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
	Что бы начать тест нажми на кнопу старт, елси нет тогда нажми отмена", reply_markup=kb_start_stop)
# Конец регитрации


# Выбор подолжит или нет
@dp.callback_query_handler(text_contains="Не хочу")
async def down(call: types.CallbackQuery):
	await call.answer("Вы решели не проходить тестировани, ваш начальный рейтинг: 0", show_alert=True)
	await call.message.edit_reply_markup()


@dp.callback_query_handler(text_contains="Поехали!!!")
async def down(call: types.CallbackQuery):
	await call.answer("Тогда чего мы ждем, начнем каждый правильный ответ дает 10 очков")
	await call.message.edit_reply_markup()
# Конец выбора

# Quiz