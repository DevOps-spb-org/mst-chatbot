import logging
from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from keyboards.common import btn_create_quiz
from loader import dp, bot
from setting.config import admin_id, admin_id_2
from filters import AddQuiz


@dp.message_handler(Text(equals="Отмена"), state=AddQuiz)
async def cancel(message: types.Message, state: FSMContext):
	await message.answer("Вы отменили добавление вопроса", reply_markup=types.ReplyKeyboardRemove())
	await state.reset_state()
	

@dp.message_handler(user_id=admin_id_2, commands='addquiz')
async def add_quiz(message: types.Message):
	await message.answer("Введите вопрос или нажмите /Отмена", reply_markup=btn_create_quiz.create_quiz)
	await AddQuiz.name.set()


@dp.message_handler(user_id=admin_id, state=AddQuiz.name)
async def enter_name(message: types.Message, state: FSMContext):
	name = message.text
	# item = Items()
	
	await message.answer("Теперь введите правильный вариант ответа")
	await AddQuiz.next()


@dp.message_handler(user_id=admin_id, state=AddQuiz.ask)
async def enter_choise(message: types.Message, state: FSMContext):
	ask = message.text
	await message.answer("Теперь введите не правильный вариант ответа")
	await state.finish()
	
	
	


