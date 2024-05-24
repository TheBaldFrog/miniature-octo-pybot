from aiogram import executor, Dispatcher

from data.config import WEBHOOK_URL, WEBHOOK_PATH, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_HOST, IP
from loader import dp, bot, SSL_CERTIFICATE, ssl_context
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from loader import db
from utils.db_api import db_gino


async def on_startup(dispatcher):
    # set webhook
    await bot.set_webhook(
        url=WEBHOOK_URL,
        certificate=SSL_CERTIFICATE
    )

    print("Connecting to db...")
    await db_gino.on_startup(dp)
    print("Connected to db!")

    print("Clear db")
    # await db.gino.drop_all()
    print("Db cleared")

    print("Create tables")
    await db.gino.create_all()
    print("Tables created")

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
        ssl_context=ssl_context
    )
