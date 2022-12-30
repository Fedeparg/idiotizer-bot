import logging
from uuid import uuid4

from telegram import Update, InlineQueryResultArticle, InputTextMessageContent, User
from telegram.ext import ContextTypes

from functions import idiotizer_i_char, idiotizer_casing_random, idiotizer_casing


class Handler:

    def __init__(self) -> None:
        # self.logger = logging.getLogger(__name__)
        self.logger = logging.getLogger(__name__)
        logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s: %(message)s')

    def __user_info_log(self, user: User) -> str:
        return f"User {user.first_name} (@{user.username}-{user.id})"

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a message when the command /start is issued."""
        user = update.effective_user
        self.logger.info(
            f"{self.__user_info_log(user)} has started the bot")
        await update.message.reply_html(
            rf"Hi {user.mention_html()}!",
        )

    async def inline_idiotizer(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        query = update.inline_query.query
        user = update.effective_user
        results = []

        if query == "":

            results.append(InlineQueryResultArticle(
                id=str(uuid4()),
                title='Type something!',
                description="Type some text so I can do my job.",
                input_message_content=InputTextMessageContent(
                    "This human doesn't know how this bot works..."),
            ),)
        else:
            self.logger.info(
                f'{self.__user_info_log(user)} is idiotizing the query: "{query}"')

            idiotizer_i = idiotizer_i_char(query)
            idiotizer_case_random = idiotizer_casing_random(query)
            idiotizer_case_1, idiotizer_case_2 = idiotizer_casing(query)

            results = [
                InlineQueryResultArticle(
                    id=str(uuid4()),
                    title='Viry intilligint',
                    description=idiotizer_i,
                    input_message_content=InputTextMessageContent(idiotizer_i),
                ),
                InlineQueryResultArticle(
                    id=str(uuid4()),
                    title='Random',
                    description=idiotizer_case_random,
                    input_message_content=InputTextMessageContent(
                        idiotizer_case_random),
                ),
                InlineQueryResultArticle(
                    id=str(uuid4()),
                    title='Type 1',
                    description=idiotizer_case_1,
                    input_message_content=InputTextMessageContent(
                        idiotizer_case_1),
                ),
                InlineQueryResultArticle(
                    id=str(uuid4()),
                    title='Type 2',
                    description=idiotizer_case_2,
                    input_message_content=InputTextMessageContent(
                        idiotizer_case_2),
                ),
            ]

        await update.inline_query.answer(results, cache_time=1)
