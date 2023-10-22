from aiogram import types
from bot_base.core.telegram_bot import TelegramBot

from bot_template.core.app_config import TemplateTelegramBotConfig
from bot_template.data_model.dm_pydantic import SaveTelegramMessageRequest
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from bot_template.core import TemplateApp


class TemplateTelegramBot(TelegramBot):
    _config_class = TemplateTelegramBotConfig
    recognized_hashtags = {"#ignore": {"ignore": True}}  #
    app: "TemplateApp"

    def __init__(self, config: _config_class, app: "TemplateApp" = None):
        super().__init__(config, app=app)

    async def chat_message_handler(self, message: types.Message):
        message_text = await super().chat_message_handler(message)

        # save message to the database
        if self.app:
            request = SaveTelegramMessageRequest(
                content=message_text,
                timestamp=message.date,
            )
            self.app.save_telegram_message(request)

    # from bot_base.core import mark_command
    # @mark_command(commands=["start"], description="Start command")
    # async def start(self, message: types.Message):
    #     response = dedent(
    #         f"""
    #         Hi! I'm the {self.__class__.__name__}.
    #         I'm based on the [bot-base](https://github.com/calmmage/bot-base) library.
    #         I support the following features:
    #         - voice messages parsing
    #         - hashtag and attribute recognition (#ignore, ignore=True)
    #         - multi-message mode
    #         Use /help for more details
    #         """
    #     )
    #     await message.answer(response)

    async def bootstrap(self):
        # self.register_command(self.start, commands="start")
        await super().bootstrap()
