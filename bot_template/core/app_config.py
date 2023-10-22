from bot_base.core import AppConfig, DatabaseConfig, TelegramBotConfig


class TemplateDatabaseConfig(DatabaseConfig):
    pass


class TemplateTelegramBotConfig(TelegramBotConfig):
    pass


class TemplateAppConfig(AppConfig):
    database: TemplateDatabaseConfig = TemplateDatabaseConfig()
    telegram_bot: TemplateTelegramBotConfig = TemplateTelegramBotConfig()
