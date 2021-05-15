from aiogram.types.callback_query import CallbackQuery
from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from loader import bot, dp
from misc import a, answers
from keyboards import test_kb
from states import Quiz
from misc import quiz_analizer

@dp.callback_query_handler(lambda query: query.data in ['start'], state=Quiz.started_test)
async def test_entry(call: CallbackQuery, state: FSMContext):
    call.answer()
    chat_id = call.from_user.id
    answers[chat_id] = ""
    await bot.edit_message_text(text=a[0], chat_id=call.message.chat.id, message_id=call.message.message_id)
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=test_kb)
    await Quiz.in_test.set()

@dp.callback_query_handler(lambda query: query.data in ["+", "-"], state=Quiz.in_test)
async def quiz(call: CallbackQuery, state: FSMContext):
    call.answer()
    chat_id = call.message.chat.id
    answers[chat_id] += call.data
    print(answers)
    if len(answers[chat_id]) < len(a):
        await bot.edit_message_text(text=a[len(answers[chat_id])], chat_id=chat_id, message_id=call.message.message_id)
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=call.message.message_id, reply_markup=test_kb)

    else:
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=call.message.message_id, reply_markup=None)
        await bot.edit_message_text(quiz_analizer(answers[chat_id]), chat_id=chat_id, message_id=call.message.message_id)
        answers[chat_id] = ""