from aiogram import Dispatcher, Bot

from bot.handlers import register_user_handlers

dp = Dispatcher()


def register_handlers() -> None:
    register_user_handlers(dp)


async def start_bot(token: str) -> None:
    bot = Bot(token)
    register_handlers()
    await dp.start_polling(bot)
