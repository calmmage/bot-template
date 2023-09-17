from bot_base.core import App
from bot_template.core.app_config import TemplateAppConfig
from bot_template.core.telegram_bot import TemplateTelegramBot


class TemplateApp(App):
    _app_config_class = TemplateAppConfig
    _telegram_bot_class = TemplateTelegramBot
