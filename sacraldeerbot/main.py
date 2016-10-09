# -*- coding: utf-8 -*-
import logging
import uuid
from random import randrange

from telegram import InlineQueryResultPhoto
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext import Filters
from telegram.ext import InlineQueryHandler
from telegram.ext import Updater

TOKEN = '256066731:AAHrxsh6s-ww3ia9z0vWaUOHkAHNT-B69ks'

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="I'm a sacral deer. Ask your aswers")


def answer(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultPhoto(
            id=uuid.uuid4(),
            caption=u"{} - {}".format(query, randrange(0, 10)),
            photo_url='',
            thumb_url=''
        )
    )
    bot.answerInlineQuery(update.inline_query.id, results, cache_time=0)


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Sorry, I didn't understand that command.")


def main():
    logging.info("Bot started")

    answer_handler = InlineQueryHandler(answer)
    dispatcher.add_handler(answer_handler)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    unknown_handler = MessageHandler([Filters.command], unknown)
    dispatcher.add_handler(unknown_handler)

    logging.info("Bot up !")

    updater.start_polling()

if __name__ == '__main__':
    main()
