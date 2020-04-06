#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Bot made using as base python-telegram-bot echobot2 code found on GitHub
https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/echobot2.py
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, pass_args

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello, I\'m the HEMA Finder bot, I\'m a bot desing with a focus on HEMA but you can also'
                              ' just use me to search for cool swords. Form more information input /help')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Here is a list of useful commands:')
    update.message.reply_text('/MasterInfo \'mastercompletename\''
                              '/MI'
                              '/SwordInfo \'swordname\''
                              '/SI'
                              '/GuardInfo \'guardname\''
                              '/GI'
                              '/FindSword \'swordname\''
                              '/FS'
                              '/FindGuard \'guardname\''
                              '/FG')


def MasterInfo(update, context):
    """Used to get a description of certain master"""
    update.message.reply_text(
        "Achille Marozzo (1484-1553) was a 16th century Italian fencing master. He was born in San Giovanni in Persiceto (a possession of Bologna) to Lodovico Marozzo in 1484.[1] After moving to the city, he studied fencing after the Dardi style in the school of the great Bolognese master Guido Antonio di Luca, and may thus have been an acquaintance of fellow student—and later, fellow master—Antonio Manciolino.")


def FindSword(update, context, MessageHandler):
    """Used to search for a sword"""
    update.message.reply_text("http://long-swords.weebly.com/uploads/1/2/8/8/12881839/1344933_orig.jpg?1")


def SwordInfo(update, context, pass_args):
    """Used to get a description of certain sword"""
    update.message.reply_text("The Longsword is a type of European sword used during the late medieval period, approximately 1350 to 1550 (with early and late use reaching into the 13th and 17th centuries, respectively). Longswords have long cruciform hilts with grips over 10 to 15in length (providing room for two hands). Straight double-edged blades are often over 1 m to 1.2 m (40\" to 48\") length, and weigh typically between 1.2 and 2.4 kg (2½ to 5 lb), with light specimens just below 1 kg (2.2 lb), and heavy specimens just above 2 kg (4½ lb).")


def FindGuard(update, context):
    """Used to search for a guard"""
    update.message.reply_text("https://wiktenauer.com/images/0/00/Marozzo_31.png")


def GuardInfo(update, context):
    """Used to get a description of certain guard"""
    update.message.reply_text("guardia di testa")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("983825642:AAGi4clr8ff9bvr9fSNLR4H7oaerpz3kMMs", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("FindSword", FindSword))
    dp.add_handler(CommandHandler("FS", FindSword))
    dp.add_handler(CommandHandler("findsword", FindSword))
    dp.add_handler(CommandHandler("FindGuard", FindGuard))
    dp.add_handler(CommandHandler("FG", FindGuard))
    dp.add_handler(CommandHandler("findguard", FindGuard))
    dp.add_handler(CommandHandler("MasterInfo", MasterInfo))
    dp.add_handler(CommandHandler("MI", MasterInfo))
    dp.add_handler(CommandHandler("masterinfo", MasterInfo))
    dp.add_handler(CommandHandler("SwordInfo", SwordInfo))
    dp.add_handler(CommandHandler("SI", SwordInfo))
    dp.add_handler(CommandHandler("swordinfo", SwordInfo))
    dp.add_handler(CommandHandler("GuardInfo", GuardInfo))
    dp.add_handler(CommandHandler("GI", GuardInfo))
    dp.add_handler(CommandHandler("guardinfo", GuardInfo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
