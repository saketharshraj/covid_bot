from telegram.ext import *
import covid_bot_responses as resp
import api_key as ak
import telepot
import covid_data as cd
# import pandas as pd
# import requests
# import io

api_key = ak.covid_key  # This is api Key, hidden because of security purpose


def start_command(update, context):
    update.message.reply_text('Type something to start')


def help_command(update, context):
    update.message.reply_text('For help DM me !')


def handle_message(update, context):
    text = str(update.message.text).lower()
    give_update(update)
    response = resp.replies(text, update)
    update.message.reply_text(response)
    print(update)


def give_update(update):
    return update


def error(update, context):
    print(f"Update {update} caused error {context.error}")


updater = Updater(api_key, use_context=True)
dp = updater.dispatcher
bot = telepot.Bot(ak.covid_key)
dp.add_handler(CommandHandler("start", start_command))
dp.add_handler(CommandHandler('help', help_command))
dp.add_handler(MessageHandler(Filters.text, handle_message))
dp.add_error_handler(error)
updater.start_polling()
updater.idle()

