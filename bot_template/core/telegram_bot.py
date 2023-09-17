from bot_base.core.telegram_bot import TelegramBot


class TemplateTelegramBot(TelegramBot):
    recognized_hashtags = {"#ignore": {"ignore": True}} #
    pass
