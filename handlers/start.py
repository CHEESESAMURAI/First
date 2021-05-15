from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from loader import dp, bot
from keyboards import start_kb
from states import Quiz



@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, 'Сейчас тут будут вопросы',
                           reply_markup=start_kb)
    await Quiz.started_test.set()
