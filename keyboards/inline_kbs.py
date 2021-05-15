from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Пройти тест", callback_data="start")]
])

test_kb = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [InlineKeyboardButton(text="+", callback_data="+"),
    InlineKeyboardButton(text="-", callback_data="-")
    ],
    [InlineKeyboardButton(text="Отменить тест", callback_data='cancel')]
])