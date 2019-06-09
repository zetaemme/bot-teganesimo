import logging
import os

from aiogram import Bot, Dispatcher, executor, types

with open(os.path.dirname(os.path.realpath(__file__)) + '/TOKEN.txt') as file:
    TOKEN = file.readline().strip()


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['pray'])
async def sand_pray(message: types.Message):
    await bot.send_message(message.chat.id, 'In nome del Padre, del Figlio e della scarpetta con il ragù')


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await bot.send_message(message.chat.id, "/vote - Inizia votazione\n/pray - Una bella preghierina")


@dp.message_handler(commands=['poll'])
async def handle_poll(message: types.Message):
    options = ['11.45', '12.00', '12.15', '12.30', '12.45', '13.00', '13.15', 'Ho il mio cibo', 'Oggi non vengo']

    await bot.send_poll(message.chat.id, 'Orario pranzo: ', options=options, disable_notification=False, reply_to_message_id=None)


if __name__ == '__main__':
    executor.start_polling(dp)
