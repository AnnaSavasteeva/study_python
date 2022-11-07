from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start(msg: types.Message):
    await msg.reply('Привет!\nНапиши мне что-нибудь!')


@dp.message_handler(commands=['help'])
async def process_help(msg: types.Message):
    # .reply - ответ на сообщение, c цитированием этого сообщения
    await msg.reply('Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!')


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
