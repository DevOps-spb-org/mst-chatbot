from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.common import btn_create_quiz
from loader import dp, bot
from aiogram.dispatcher.filters import BoundFilter
from setting.config import admin_id


class CheackAdmin(BoundFilter):
	key = admin_id
	
	async def check(self, message: types.Message):
		member = await bot.get_chat_member(message.chat.id, message.from_user.id)
		return member.is_chat_admin()


class FSMAmdin(StatesGroup):
	name = State()
	description = State()
	

class FSMAdmincreatedQuzi(StatesGroup):
	name = State()
	description = StatesGroup
	

@dp.message_handler(commands='create')
async def create_quiz(message: types.Message):
	await message.answer("Выберете один их предложенных вариантов", reply_markup=btn_create_quiz.create_quiz)
	

@dp.message_handler(Text(equals="Создать опрос"))
async def add_name_quiz(message: types.Message):
	await FSMAdmincreatedQuzi.name.set()
	await message.reply("Введите название опроса")
	
	
@dp.message_handler(state=FSMAdmincreatedQuzi.name)
async def add_description(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['name'] = message.text
	await FSMAdmincreatedQuzi.next()
	await message.reply("Введите описание опроса")


@dp.message_handler(state=FSMAdmincreatedQuzi.description)
async def load_quiz(message: types.Message, state=None):
	async with state.proxy() as data:
		data['position'] = message.text
	await message.answer("Quiz успешно добавлен")
	
	
@dp.message_handler(lambda message: message.text == "Отмена")
async def action_cancel(message: types.Message):
	remove_btm = types.ReplyKeyboardRemove()
	await message.answer("Если хотите опять добавить quiz и вопросы напишите /create", reply_markup=remove_btm)


def register_handlers_use(dp: Dispatcher):
	"""
		регистрация handlers
	"""
	dp.register_message_handler(create_quiz, commands='sign', state=None)
	dp.register_message_handler(add_description, state=FSMAdmincreatedQuzi.name)
	dp.register_message_handler(load_quiz, state=FSMAdmincreatedQuzi.description)