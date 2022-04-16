
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def log(update: Update, context: CallbackContext):
    file = open('dp.csv', 'a')
    file.write(f'{update._effective_user.first_name}, {update._effective_user.id}, {update.message.text}\n')
    file.close()