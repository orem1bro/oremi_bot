import logging
import os
from aiogram import Bot, types, executor
from aiogram.dispatcher import Dispatcher


API_TOKEN = os.getenv('BOT_TOKEN')
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp= Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Start bot')

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply('Help')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
