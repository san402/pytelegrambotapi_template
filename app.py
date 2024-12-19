import random
import string
from email.contentmanager import maintype
from typing import Iterable

import telebot
from dotenv import load_dotenv
from os import environ

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

from models import TelegramButton, User

load_dotenv()
bot = telebot.TeleBot(token=environ.get('TELEGRAM_BOT_TOKEN'))

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def gen_inline_markup(buttons:Iterable[TelegramButton], width=2, max_row_keys=2):
    markup = InlineKeyboardMarkup()
    markup.row_width = width
    markup.max_row_keys = max_row_keys
    rows = (InlineKeyboardButton(text=x.name,
                                    callback_data=x.callback_data,
                                    url=x.url) for x in buttons)
    markup.add(*rows)
    return markup

def gen_reply_markup(buttons:Iterable[TelegramButton], width=2, max_row_keys=2):
    markup = ReplyKeyboardMarkup()
    markup.row_width = width
    markup.max_row_keys = max_row_keys
    rows = (KeyboardButton(text=x.name) for x in buttons)
    markup.add(*rows)
    markup.resize_keyboard = True
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user = User(from_user=call.from_user)
    # handle user callback here

@bot.message_handler(content_types=['text'])
def message_handler(message):
    user = User(from_user=message.from_user)
    # handle user message here

@bot.message_handler(commands=['start'])
def start(message):
    user = User(from_user=message.from_user)
    # handle start command here

if __name__ == '__main__':
    bot.polling()