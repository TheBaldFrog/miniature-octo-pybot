from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode

from loader import dp
from utils.db_api import quick_commands


@dp.message_handler(Command("email"))
async def wait_email(message: types.Message, state: FSMContext):
    await message.answer("Send me your email...")
    await state.set_state("email")


@dp.message_handler(state="email")
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    await quick_commands.update_user_email(email=email, id=message.from_user.id)
    user = await quick_commands.select_user(id=message.from_user.id)
    await message.answer("Data updated successfully.\n" +
                         hcode(f'id={user.id}\n'
                               f'name={user.name}\n'
                               f'email={user.email}\n'))
    await state.finish()
