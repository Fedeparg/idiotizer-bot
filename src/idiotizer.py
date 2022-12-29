"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from random import random

import argparse

from telegram import __version__ as TG_VER

import re

import os

from uuid import uuid4

from telegram import ForceReply, Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, InlineQueryHandler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
    )

async def inline_idiotizer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.inline_query.query

    if query == "":
        return

    idiotizer_i = idiotizer_i_char(query)
    idiotizer_case = idiotizer_casing(query)
    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title=idiotizer_i,
            input_message_content=InputTextMessageContent(idiotizer_i),
        ),
        InlineQueryResultArticle(
            id=str(uuid4()),
            title=idiotizer_case,
            input_message_content=InputTextMessageContent(idiotizer_case),
        ),
    ]

    await update.inline_query.answer(results, cache_time=0)


def idiotizer_i_char(text) -> None:
    idiot_text = re.sub('[aeouáéóúàèòù]', 'i', text)
    idiot_text = re.sub('[AEOUÁÉÓÚÀÈÒÙ]', 'I', idiot_text)
    return idiot_text

def idiotizer_casing(text) -> None:
    idiot_text = ''.join(c.upper() if random() > 0.5 else c for c in text)
    idiot_text = ''.join(c.lower() if random() > 0.5 else c for c in idiot_text)
    return idiot_text


# Not used for now because reasons

# async def idiotizer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Echo the user message idiotized."""
#     idiot_text = re.sub('[aeouáéóúàèòù]', 'i', update.message.text)
#     idiot_text = re.sub('[AEOUÁÉÓÚÀÈÒÙ]', 'I', idiot_text)
#     await update.message.reply_text(idiot_text)


def main(args) -> None:
    #Start the bot
    # Create the Application and pass it your bot's token.
    application = ApplicationBuilder().token(os.environ['bot_token']).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    #application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, idiotizer))

    application.add_handler(InlineQueryHandler(inline_idiotizer))

    # Run the bot until the user presses Ctrl-C

    # add handlers
    if args.dev.lower()[0] == 'f':
        TOKEN = os.environ['bot_token']
        PORT = int(os.environ.get('PORT', '8080'))
        application.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=TOKEN,
            webhook_url="https://idiotizer.fly.dev/" + TOKEN
        )
    else:
        application.run_polling()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-dev", default = 'false', help="Development or nah")
    args = parser.parse_args()
    main(args)