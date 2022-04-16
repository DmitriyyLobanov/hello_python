
import bot_commands   as bc
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext



updater = Updater('5347093915:AAEmHsH02avaszv-yfTs1Q4ZC9f9SeOtGxc')

updater.dispatcher.add_handler(CommandHandler('hi', bc.hi_command))
updater.dispatcher.add_handler(CommandHandler('Time', bc.time_command))
updater.dispatcher.add_handler(CommandHandler('help', bc.help_command))
updater.dispatcher.add_handler(CommandHandler('sum', bc.sum_command))

print('Server start.')
updater.start_polling()
updater.idle()