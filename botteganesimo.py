import os, logging
from aiogram import Bot, Dispatcher, executor, types

# Get token from TOKEN.txt file (create it if not existent)
with open(os.path.dirname(os.path.realpath(__file__)) + '/TOKEN.txt') as file:
    TOKEN = file.readline().strip()

# Bot and Dispatcher definition
bot = Bot(token = TOKEN)
dispatcher = Dispatcher(bot)

# Set logging for error handling format
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

# Pray command
@dispatcher.message_handler(commands = ['pray'])
async def send_pray(message: types.Message):
    await message.answer(text='In nome del Padre, del Figlio e della scarpetta con il ragù')


# Poll command
@dispatcher.message_handler(commands = ['poll'])
async def send_poll(message: types.Message):
    options = ['11.45', '12.00', '12.15', '12.30', '12.45', '13.00', '13.15', 'Ho il mio cibo', 'Oggi non vengo']
    await bot.send_poll(message.chat.id, question='Orario Pranzo:', options=options, is_anonymous=False)


# Executor
executor.start_polling(dispatcher)