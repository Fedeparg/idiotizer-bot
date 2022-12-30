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
import argparse
import os

from telegram.ext import ApplicationBuilder, CommandHandler, InlineQueryHandler

from handlers import Handler

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.

def main(args) -> None:
    # Start the bot
    # Create the Application and pass it your bot's token.
    application = ApplicationBuilder().token(os.environ['bot_token']).build()
    handlers = Handler()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", handlers.start))

    application.add_handler(InlineQueryHandler(handlers.inline_idiotizer))

    # Run the bot until the user presses Ctrl-C
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
    parser.add_argument("-dev", default='false', help="Development or nah")
    args = parser.parse_args()
    main(args)
