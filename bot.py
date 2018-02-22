# -*- coding: utf-8 -*-
import os
from telegram.ext import Updater, MessageHandler, Filters

# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']

#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...

updater = Updater(token=token)
dispatcher = updater.dispatcher


def replay_in_caps(bot, update):
    message = update.message

    if message.text == '?' and message.reply_to_message is not None:
        bot.send_message(chat_id=message.chat_id,
                         text=message.reply_to_message.text.upper(),
                         reply_to_message_id=message.message_id)


replay_in_caps_handler = MessageHandler(Filters.text, replay_in_caps)
dispatcher.add_handler(replay_in_caps_handler)

updater.start_polling()
