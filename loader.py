import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=config.API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
