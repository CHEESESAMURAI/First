from aiogram.dispatcher.filters.state import State, StatesGroup

class Quiz(StatesGroup):
    started_test = State()
    in_test = State()