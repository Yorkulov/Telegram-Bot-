from aiogram.dispatcher.filters.state import StatesGroup, State

class Generation(StatesGroup):
    text_to_image = State()