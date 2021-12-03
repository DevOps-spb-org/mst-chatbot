from aiogram.dispatcher.filters.state import State, StatesGroup


class NewUser(StatesGroup):
	"""
	:param
	name (str) хранит имя пользолвателя
	position (str)  хранит дожность пользователя
	"""
	name = State()
	position = State()