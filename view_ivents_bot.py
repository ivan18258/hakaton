import logging
import os
import sys
import json
import requests
from dotenv import load_dotenv
from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Updater


load_dotenv()

TELEGRAM_TOKEN = os.getenv('TOKENBOT')

handler_CP1251 = logging.FileHandler(filename='cp1251.log')
handler_UTF8 = logging.FileHandler(filename='program.log', encoding='utf-8')
logging.basicConfig(
    level=logging.DEBUG,
    handlers=(handler_UTF8, handler_CP1251),
    format=('%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - '
            '%(lineno)s - %(message)s'))

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)
logger.setLevel(logging.ERROR)
logger.setLevel(logging.CRITICAL)

handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - '
                              '%(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(formatter)

bot = Bot(token=TELEGRAM_TOKEN)

URL1 = 'http://127.0.0.1:8000/api/v1/events/'
URL2 = 'http://127.0.0.1:8000/api/v1/events_mini/'


def list_events(update, context):
    response = requests.get(URL1).json()
    for i in range(len(response)):
        events_id = response[i]['id']
        events_title = response[i]['title']
        description = response[i]['description']
        time = response[i]['time']
        image = response[i]['image']
        chat = update.effective_chat
        context.bot.send_message(chat.id, f'{events_id}\n{description}\n{image}\n{time}')

    


def track_events(update, context):
    pass


def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([
                ['/list_events'] ,['/Отслеживаемые события']
            ], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text='Спасибо, что вы включили меня, {}!'.format(name),
        reply_markup=buttons
        )


def check_token():
    """
    Check the token required for running the entire code in the .env.
    If the token is available function returns True, otherwise - False.
    """
    if TELEGRAM_TOKEN:
        return True
    else:
        return False


def main():
    """
    The main logic of the bot.
    """
    updater = Updater(token=TELEGRAM_TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', wake_up))
    updater.dispatcher.add_handler(CommandHandler('list_events', list_events))
    updater.dispatcher.add_handler(CommandHandler('track_events', track_events))
    updater.start_polling()#poll_interval=20.0)
    updater.idle()
# poll_interval=20.0

if __name__ == '__main__':
    main()