from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.types.callback_query import CallbackQuery
from keyboards import start_kb, test_kb
from loader import bot, dp
from misc import a, answers, quiz_analizer
from states import Quiz


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


@dp.callback_query_handler(lambda query: query.data in ["back"], state="*")
async def back(call: CallbackQuery, state: FSMContext):
    call.answer()
    await bot.edit_message_text(text="Сейчас тут будут вопросы", message_id=call.message.message_id, chat_id=call.from_user.id)
    await bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=start_kb)
    await state.reset_state()
