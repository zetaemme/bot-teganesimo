import os, logging
from telegram.ext import Updater, CommandHandler

# Get token from TOKEN.txt file (create it if not existent)
with open(os.path.dirname(os.path.realpath(__file__)) + '/TOKEN.txt') as file:
    TOKEN = file.readline().strip()

# Updater and Dispatcher definition
updater = Updater(token = TOKEN, use_context = True)
dispatcher = updater.dispatcher

# Set logging for error handling format
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

# Pray command
def pray(update, context):
    context.bot.send_message(chat_id = update.message.chat_id, text = 'In nome del Padre, del Figlio e della scarpetta con il ragù')


# Poll command
def poll(update, context):
    options = ['11.45', '12.00', '12.15', '12.30', '12.45', '13.00', '13.15', 'Ho il mio cibo', 'Oggi non vengo']
    context.bot.send_poll(chat_id=update.message.chat_id, question = 'Orario Pranzo:', options = options)


# Handler
pray_handler = CommandHandler('pray', pray)
poll_handler = CommandHandler('poll', poll)

dispatcher.add_handler(pray_handler)
dispatcher.add_handler(poll_handler)

updater.start_polling()
print('Polling...')