from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start(msg: types.Message):
    user = msg.from_user.first_name
    await msg.reply(f'Привет, {user}!')


@dp.message_handler(commands=['help'])
async def process_help(msg: types.Message):
    await msg.reply(f'/start — приветствие\n/help — список команд бота\n/talk — поболтать с ботом')


@dp.message_handler(commands=['talk'])
async def simple_talk(msg: types.Message):
    await msg.reply('Какое твое настоящее имя?')
    await msg.reply(f'{msg.text}! Прекрасное имя!')
    # await bot.send_message(msg.from_user.id, f'{msg.text}! Прекрасное имя!')


if __name__ == '__main__':
    executor.start_polling(dp)
