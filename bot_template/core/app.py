from bot_base.core import App
from bot_template.core.app_config import (
    TemplateAppConfig,
    TemplateDatabaseConfig,
    TemplateTelegramBotConfig,
)
from bot_template.core.telegram_bot import TemplateTelegramBot
from bot_template.data_model.dm_mongo import TelegramMessageMongo
from bot_template.data_model.dm_pydantic import SaveTelegramMessageRequest


class TemplateApp(App):
    _app_config_class = TemplateAppConfig
    _telegram_bot_class = TemplateTelegramBot
    _database_config_class = TemplateDatabaseConfig
    _telegram_bot_config_class = TemplateTelegramBotConfig

    def save_telegram_message(self, message: SaveTelegramMessageRequest):
        self._connect_db()
        item = TelegramMessageMongo(content=message.content, date=message.date)
        item.save()
