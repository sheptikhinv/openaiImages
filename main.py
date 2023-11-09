import asyncio

from bot import start_bot
from bot.funcs import check_images_dir
from config import get_token, get_openai_token


if __name__ == '__main__':
    check_images_dir()
    token = get_token()
    openai_token = get_openai_token()
    asyncio.run(start_bot(token))
