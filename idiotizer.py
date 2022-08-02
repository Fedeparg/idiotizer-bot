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
        reply_markup=ForceReply(selective=True),
    )

async def inline_idiotizer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.inline_query.query

    if query == "":
        return

    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            title=idiotizer_fun(query),
            input_message_content=InputTextMessageContent(idiotizer_fun(query)),
        ),
    ]

    await update.inline_query.answer(results)


def idiotizer_fun(text) -> None:
    idiot_text = re.sub('[aeouáéóúàèòù]', 'i', text)
    idiot_text = re.sub('[AEOUÁÉÓÚÀÈÒÙ]', 'I', idiot_text)
    return idiot_text

async def idiotizer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message idiotized."""
    idiot_text = re.sub('[aeouáéóúàèòù]', 'i', update.message.text)
    idiot_text = re.sub('[AEOUÁÉÓÚÀÈÒÙ]', 'I', idiot_text)
    await update.message.reply_text(idiot_text)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = ApplicationBuilder().token(os.environ.get('bot_token')).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    #application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, idiotizer))

    application.add_handler(InlineQueryHandler(inline_idiotizer))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()