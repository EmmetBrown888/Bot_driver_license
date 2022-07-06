import os
import logging

from aiogram.dispatcher.filters import Text
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputFile

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# States
choose_state = None


class FormAlaska(StatesGroup):
    num_licence = State()
    date_of_birth = State()
    sex = State()
    height = State()
    weight = State()
    eyes = State()
    issue_date = State()
    expires_date = State()
    class_drive = State()
    restrictions = State()
    duplicate_num = State()
    address = State()


class FormArkansas(StatesGroup):
    num_licence = State()
    date_of_birth = State()
    sex = State()
    height = State()
    eyes = State()
    issue_date = State()
    expires_date = State()
    class_drive = State()
    first_name = State()
    last_name = State()
    address = State()


async def waiting(message):
    await bot.send_message(message.from_user.id, 'Пожалуйста подождите...', parse_mode='Markdown')


@dp.message_handler(commands=['start', 'help'])
@dp.message_handler(Text(equals='⬅️ Назад в меню', ignore_case=True), state=None)
@dp.callback_query_handler(text='Меню')
async def send_welcome(message: types.Message):
    """Обработчик команд: `/start` or `/help` """
    first_text = "Приветствую 👋 Вас в боте сервиса по созданию водительских прав США!🇺🇸"
    second_text = """
Вам требуется качественный водительские права?
-Вы попали именно туда.

🔶 Интуитивно понятный интерфейс;
🔶 Быстрое создания;
🔶 Круглосуточная площадка;

Мы постоянно улучшаем наши инструменты и варианты водительских прав.

Выберите нужный вам штат и оцените качество и простоту в работе.
    """

    buttons = InlineKeyboardMarkup()
    button_alaska = InlineKeyboardButton('🗽 Аляска', callback_data='Аляска')
    button_arkansas = InlineKeyboardButton('🗽 Арканзас', callback_data='Арканзас')
    buttons \
        .add(button_alaska) \
        .add(button_arkansas)

    await bot.send_message(message.from_user.id, first_text, reply_markup=types.ReplyKeyboardRemove())
    await message.answer(second_text, reply_markup=buttons, parse_mode='Markdown')


@dp.callback_query_handler(text='Аляска')
async def alaska(message: types.Message):
    global choose_state
    choose_state = 'Alaska'
    photo = InputFile('photos/states/alaska.jpg')
    await waiting(message)
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)

    # Добавьте ваше фото
    message_text = 'Добавьте фото в бота'
    await bot.send_message(message.from_user.id, message_text, parse_mode='Markdown')


@dp.callback_query_handler(text='Арканзас')
async def arkansas(message: types.Message):
    global choose_state
    choose_state = 'Arkansas'
    photo = InputFile('photos/states/arkansas.jpg')
    await waiting(message)
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)

    # Добавьте ваше фото
    message_text = "Добавьте фото в бота"
    await bot.send_message(message.from_user.id, message_text, parse_mode='Markdown')


@dp.message_handler(content_types=['photo'])
async def get_photo(message):
    await waiting(message)
    file_info = await bot.get_file(message.photo[-1].file_id)
    filename = file_info.file_path.split('photos/')[1].split('.')
    await message.photo[-1].download(f'photos/from_user/{message.from_user.id}.{filename[1]}')

    if choose_state == 'Alaska':
        await FormAlaska.num_licence.set()
    else:
        await FormArkansas.num_licence.set()

    await bot.send_message(message.from_user.id, 'Введите номер водительской лицензии', parse_mode='Markdown')


if __name__ == '__main__':
    from handlers.alaska import *
    from handlers.arkansas import *

    executor.start_polling(dp, skip_updates=True)
