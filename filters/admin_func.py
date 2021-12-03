from aiogram.dispatcher.filters.state import State, StatesGroup


class AddQuiz(StatesGroup):
	name = State()
	ask = State()
	choise = State()