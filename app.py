from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from loader import db
from utils.db_api import db_gino


async def on_startup(dispatcher):
    print("Connecting to db...")
    await db_gino.on_startup(dp)
    print("Connected to db!")

    print("Clear db")
    #await db.gino.drop_all()
    print("Db cleared")

    print("Create tables")
    await db.gino.create_all()
    print("Tables created")


    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

