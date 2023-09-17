from aiogram import types
from bot_base.core.telegram_bot import TelegramBot

from bot_template.core.app_config import TemplateAppConfig
from bot_template.data_model.data_model_pydantic import \
    SaveTelegramMessageRequest
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app import TemplateApp


class TemplateTelegramBot(TelegramBot):
    _config_class = TemplateAppConfig
    # _app_class = "TemplateApp"
    recognized_hashtags = {"#ignore": {"ignore": True}}  #

    def __init__(self, config: TemplateAppConfig, app: "TemplateApp" = None):
        super().__init__(config, app=app)

    async def chat_message_handler(self, message: types.Message):
        message_text = await super().chat_message_handler(message)

        # save message to the database
        if self.app:
            request = SaveTelegramMessageRequest(
                content=message_text,
                timestamp=message.date,
            )
            self.app.save_message(request)
