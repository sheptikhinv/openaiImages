from aiogram import Router, F, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from bot import funcs

router = Router(name='user')


@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Для анализа youtube-превью, отправьте мне изображение.\n"
                         "Также вы можете добавить описание к изображению, тогда оно тоже будет учтено нейросетью.")


@router.message(F.photo)
async def get_photo(message: Message):
    description = message.caption or None
    image = await message.bot.get_file(message.photo[-1].file_id)
    file_path = f"./images/{funcs.id_generator()}.jpg"
    await message.bot.download_file(image.file_path, file_path)
    response = funcs.get_gpt_response(prompt=funcs.read_file("prompt.txt"),
                                      base64_image=funcs.encode_image(file_path),
                                      description=description)
    await message.answer(response)


def register_user_handlers(dp: Dispatcher):
    dp.include_router(router)
