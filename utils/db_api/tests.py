import asyncio

from data import config
from utils.db_api import quick_commands
from utils.db_api.db_gino import db


async def test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    print("Add users")
    await quick_commands.add_user(1, "One", "email1")
    await quick_commands.add_user(2, "Two", "email2")
    await quick_commands.add_user(3, "Three", "email3")
    await quick_commands.add_user(4, "Four", "email4")
    await quick_commands.add_user(5, "Five", "email5")
    print("finish")

    users = await quick_commands.count_users()
    print(f"count all users: {users}")

    user = await quick_commands.select_user(id=5)
    print(f"select user: {user}")

    users = await quick_commands.select_all_user()
    print(f"select all users: {users}")

    users = list(map(str, await quick_commands.select_all_user()))
    print(f"select all users: {users}")

asyncio.run(test())
