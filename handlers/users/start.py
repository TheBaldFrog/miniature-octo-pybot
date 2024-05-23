from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db
from utils.db_api import quick_commands


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    await quick_commands.add_user(id=message.from_user.id, name=name)

    count = await quick_commands.count_users()
    await message.answer(
        '\n'.join(
            [
                f'Hi, {message.from_user.full_name}!',
                'Sei stato aggiunto nella database',
                f'Nella db ci sono <b>{count}</b> utenti'
            ]
        )
    )
