from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InputFile

from utils.create_drivers.main import Arkansas
from utils.validate_fields.validate import validate_form
from main import dp, bot, FormArkansas, waiting


@dp.message_handler(state=FormArkansas.num_licence)
async def process_license(message: types.Message, state: FSMContext):
    """Заполнение номера водительской лицензии"""
    async with state.proxy() as data:
        data['num_licence'] = message.text
        res_valid = await validate_form('num_licence', 'Arkansas', message)
        if res_valid:
            await FormArkansas.next()
            await bot.send_message(message.from_user.id, 'Введите дату рождения в формате месяц-день-год',
                                   parse_mode='Markdown')


@dp.message_handler(state=FormArkansas.date_of_birth)
async def process_date_of_birth(message: types.Message, state: FSMContext):
    """Заполнение даты рождения"""
    async with state.proxy() as data:
        data['date_of_birth'] = message.text
        res_valid = await validate_form('date_of_birth', 'Arkansas', message)
        if res_valid:
            await FormArkansas.next()
            await bot.send_message(message.from_user.id, 'Введите пол, например F или M', parse_mode='Markdown')


@dp.message_handler(state=FormArkansas.sex)
async def process_sex(message: types.Message, state: FSMContext):
    """Заполнение пола"""
    async with state.proxy() as data:
        data['sex'] = message.text
        res_valid = await validate_form('sex', 'Arkansas', message)
        if res_valid:
            await FormArkansas.next()
            await bot.send_message(message.from_user.id, 'Введите рост, например 5-09', parse_mode='Markdown')


@dp.message_handler(state=FormArkansas.height)
async def process_height(message: types.Message, state: FSMContext):
    """Заполнение роста"""
    async with state.proxy() as data:
        data['height'] = message.text
        res_valid = await validate_form('height', 'Arkansas', message)
        if res_valid:
            await FormArkansas.next()
            await bot.send_message(message.from_user.id, 'Введите цвет глаз, например BLU', parse_mode='Markdown')


@dp.message_handler(state=FormArkansas.eyes)
async def process_eyes(message: types.Message, state: FSMContext):
    """Заполнение цвета глаз"""
    async with state.proxy() as data:
        data['eyes'] = message.text
        res_valid = await validate_form('eyes', 'Arkansas', message)
        if res_valid:
            await FormArkansas.next()
            await bot.send_message(message.from_user.id,
                                   'Введите дату выпуска водительских прав в формате: месяц-день-год',
                                   parse_mode='Markdown')


@dp.message_handler(state=FormArkansas.issue_date)
async def process_issue_date(message: types.Message, state: FSMContext):
    """Заполнение даты выпуска водительских прав"""
    async with state.proxy() as data:
        data['issue_date'] = message.text
        res_valid = await validate_form('issue_date', 'Arkansas', message)
        if res_valid:
            await FormArkansas.next()
            await bot.send_message(message.from_user.id,
                                   'Введите дату окончания годности водительских прав в формате: месяц-день-год',
                                   parse_mode='Markdown')


@dp.message_handler(state=FormArkansas.expires_date)
async def process_expires_date(message: types.Message, state: FSMContext):
    """Заполнение даты окончания годности водительских прав"""
    async with state.proxy() as data:
        data['expires_date'] = message.text
        res_valid = await validate_form('expires_date', 'Arkansas', message)
        if res_valid:
            await FormArkansas.next()
            await bot.send_message(message.from_user.id, 'Введите класс водительских прав, например B',
                                   parse_mode='Markdown')


@dp.message_handler(state=FormArkansas.class_drive)
async def process_class_drive(message: types.Message, state: FSMContext):
    """Заполнение класса водительских прав"""
    async with state.proxy() as data:
        data['class_drive'] = message.text
        res_valid = await validate_form('class_drive', 'Arkansas', message)
        if res_valid:
            await FormArkansas.next()
            await bot.send_message(message.from_user.id, 'Введите Имя, например Peter', parse_mode='Markdown')


@dp.message_handler(state=FormArkansas.first_name)
async def process_first_name(message: types.Message, state: FSMContext):
    """Заполнение Имя"""
    async with state.proxy() as data:
        data['first_name'] = message.text
        res_valid = await validate_form('first_name', 'Arkansas', message)
        if res_valid:
            await FormArkansas.next()
            await bot.send_message(message.from_user.id, 'Введите Фамилию, например Jackson', parse_mode='Markdown')


@dp.message_handler(state=FormArkansas.last_name)
async def process_last_name(message: types.Message, state: FSMContext):
    """Заполнение Фамилию"""
    async with state.proxy() as data:
        data['last_name'] = message.text
        res_valid = await validate_form('last_name', 'Arkansas', message)
        if res_valid:
            await FormArkansas.next()
            await bot.send_message(message.from_user.id, 'Введите адрес', parse_mode='Markdown')


@dp.message_handler(state=FormArkansas.address)
async def process_address(message: types.Message, state: FSMContext):
    """Заполнение адреса"""
    async with state.proxy() as data:
        data['address'] = message.text

    await state.finish()
    await waiting(message)

    # Создания водительских прав
    driver_license = Arkansas(
        f'./photos/from_user/{message.from_user.id}.jpg',
        message.from_user.id,
        data['num_licence'],
        data['date_of_birth'],
        data['sex'],
        data['height'],
        data['eyes'],
        data['issue_date'],
        data['expires_date'],
        data['class_drive'],
        data['first_name'],
        data['last_name'],
        data['address']
    )
    driver_license.run()

    # Отправка готовых прав пользователю
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    button_menu = KeyboardButton('⬅️ Назад в меню')
    buttons.row(button_menu)

    message_text = 'Ваши готовые водительские права! Спасибо что вы с нами!'

    photo = InputFile(f'photos/from_user/{message.from_user.id}.jpg')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)

    await message.answer(message_text, reply_markup=buttons, parse_mode='Markdown')
