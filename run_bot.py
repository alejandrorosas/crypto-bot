#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot send back the Crypto stats

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from app.settings import TELEGRAM_BOT_TOKEN
from app.handlers.base import start_handler, error_handler, echo_handler, help_handler
from app.handlers.cryptocurrencies import intense_handler, bitcoin_handler
from app.handlers.pool import pool_handler


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start_handler))
    dispatcher.add_handler(CommandHandler("help", help_handler))

    # Currencies handler
    dispatcher.add_handler(CommandHandler("intense", intense_handler))
    dispatcher.add_handler(CommandHandler("bitcoin", bitcoin_handler))

    # Pool handler
    dispatcher.add_handler(CommandHandler("pool", pool_handler))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text, echo_handler))

    # log all errors
    dispatcher.add_error_handler(error_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
