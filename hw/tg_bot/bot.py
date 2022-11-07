from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    user = msg.from_user.first_name
    await bot.send_message(msg.chat.id, f'Привет, {user}!')


@dp.message_handler(commands=['menu'])
async def help(msg: types.Message):
    await bot.send_message(msg.chat.id, f'/start — приветствие\n/talk — поболтать с ботом')


@dp.message_handler(commands=['talk'])
async def talk(msg: types.Message):
    await bot.send_message(msg.chat.id, 'Какое твое настоящее имя?')
    await bot.send_message(msg.chat.id, f'{msg.text}! Прекрасное имя!')


def ask_age(reply):
    bot.send_message(reply.chat.id, f'{reply.text}! Прекрасное имя!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
