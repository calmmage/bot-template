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

    def _schedule_jobs(self):
        from apscheduler.triggers.interval import IntervalTrigger
        import datetime

        assert self.config.enable_scheduler

        # every Sunday at 23:59
        next_sunday = datetime.datetime.now()
        notify_trigger = IntervalTrigger(weeks=1, start_date=next_sunday)
        self._scheduler.add_job(
            self._sample_job,
            trigger=notify_trigger,
            id="notify_users",
            name="Notify users",
        )

    async def _sample_job(self):
        """
        Refresh tokens and notify users
        :return:
        """
        self.logger.info("This is a sample job")
        message = "This is a sample job"
        await self.bot.send_safe(message, 123)
