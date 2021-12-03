from aiogram.types import Message
from loader import dp


@dp.message_handler(commands='start')
async def start_bot(message: Message):
    await message.reply(f"Привет {message.from_user.full_name}!",
                        reply=False)
