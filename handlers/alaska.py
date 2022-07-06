from aiogram.dispatcher import FSMContext
from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InputFile

from utils.validate_fields.validate import validate_form
from utils.create_drivers.main import Alaska
from main import dp, bot, FormAlaska, waiting


@dp.message_handler(state=FormAlaska.num_licence)
async def process_license(message: types.Message, state: FSMContext):
    """Заполнение номера водительской лицензии"""
    async with state.proxy() as data:
        data['num_licence'] = message.text
        res_valid = await validate_form('num_licence', 'Alaska', message)
        if res_valid:
            await FormAlaska.next()
            await bot.send_message(message.from_user.id, 'Введите дату рождения в формате месяц-день-год', parse_mode='Markdown')


@dp.message_handler(state=FormAlaska.date_of_birth)
async def process_date_of_birth(message: types.Message, state: FSMContext):
    """Заполнение даты рождения"""
    async with state.proxy() as data:
        data['date_of_birth'] = message.text
        res_valid = await validate_form('date_of_birth', 'Alaska', message)
        if res_valid:
            await FormAlaska.next()
            await bot.send_message(message.from_user.id, 'Введите пол, например F', parse_mode='Markdown')


@dp.message_handler(state=FormAlaska.sex)
async def process_sex(message: types.Message, state: FSMContext):
    """Заполнение пола"""
    async with state.proxy() as data:
        data['sex'] = message.text
        res_valid = await validate_form('sex', 'Alaska', message)
        if res_valid:
            await FormAlaska.next()
            await bot.send_message(message.from_user.id, 'Введите рост, например 5-09', parse_mode='Markdown')


@dp.message_handler(state=FormAlaska.height)
async def process_height(message: types.Message, state: FSMContext):
    """Заполнение роста"""
    async with state.proxy() as data:
        data['height'] = message.text
        res_valid = await validate_form('height', 'Alaska', message)
        if res_valid:
            await FormAlaska.next()
            await bot.send_message(message.from_user.id, 'Введите вес', parse_mode='Markdown')


@dp.message_handler(state=FormAlaska.weight)
async def process_weight(message: types.Message, state: FSMContext):
    """Заполнение веса"""
    async with state.proxy() as data:
        data['weight'] = message.text
        res_valid = await validate_form('weight', 'Alaska', message)
        if res_valid:
            await FormAlaska.next()
            await bot.send_message(message.from_user.id, 'Введите цвет глаз, например BLU', parse_mode='Markdown')


@dp.message_handler(state=FormAlaska.eyes)
async def process_eyes(message: types.Message, state: FSMContext):
    """Заполнение цвета глаз"""
    async with state.proxy() as data:
        data['eyes'] = message.text
        res_valid = await validate_form('eyes', 'Alaska', message)
        if res_valid:
            await FormAlaska.next()
            await bot.send_message(message.from_user.id,
                                   'Введите дату выпуска водительских прав в формате: месяц-день-год', parse_mode='Markdown')


@dp.message_handler(state=FormAlaska.issue_date)
async def process_issue_date(message: types.Message, state: FSMContext):
    """Заполнение даты выпуска водительских прав"""
    async with state.proxy() as data:
        data['issue_date'] = message.text
        res_valid = await validate_form('issue_date', 'Alaska', message)
        if res_valid:
            await FormAlaska.next()
            await bot.send_message(message.from_user.id,
                                   'Введите дату окончания годности водительских прав в формате: месяц-день-год',
                                   parse_mode='Markdown')


@dp.message_handler(state=FormAlaska.expires_date)
async def process_expires_date(message: types.Message, state: FSMContext):
    """Заполнение даты окончания годности водительских прав"""
    async with state.proxy() as data:
        data['expires_date'] = message.text
        res_valid = await validate_form('expires_date', 'Alaska', message)
        if res_valid:
            await FormAlaska.next()
            await bot.send_message(message.from_user.id,
                                   'Введите класс водительских прав, например B',
                                   parse_mode='Markdown')


@dp.message_handler(state=FormAlaska.class_drive)
async def process_class_drive(message: types.Message, state: FSMContext):
    """Заполнение класса водительских прав"""
    async with state.proxy() as data:
        data['class_drive'] = message.text
        res_valid = await validate_form('class_drive', 'Alaska', message)
        if res_valid:
            await FormAlaska.next()
            await bot.send_message(message.from_user.id, 'Введите номер ограничения, например 1', parse_mode='Markdown')


@dp.message_handler(state=FormAlaska.restrictions)
async def process_restrictions(message: types.Message, state: FSMContext):
    """Заполнение номера количества ограничений"""
    async with state.proxy() as data:
        data['restrictions'] = message.text
        res_valid = await validate_form('restrictions', 'Alaska', message)
        if res_valid:
            await FormAlaska.next()
            await bot.send_message(message.from_user.id, 'Введите номер дубликата, например 2', parse_mode='Markdown')


@dp.message_handler(state=FormAlaska.duplicate_num)
async def process_duplicate_num(message: types.Message, state: FSMContext):
    """Заполнение номера дубликата прав"""
    async with state.proxy() as data:
        data['duplicate_num'] = message.text
        res_valid = await validate_form('duplicate_num', 'Alaska', message)
        if res_valid:
            await FormAlaska.next()
            await bot.send_message(message.from_user.id, 'Введите адрес', parse_mode='Markdown')


@dp.message_handler(state=FormAlaska.address)
async def process_address(message: types.Message, state: FSMContext):
    """Заполнение адреса"""
    async with state.proxy() as data:
        data['address'] = message.text

    await state.finish()
    await waiting(message)

    # Создания водительских прав
    driver_license = Alaska(
        f'./photos/from_user/{message.from_user.id}.jpg',
        message.from_user.id,
        data['num_licence'],
        data['date_of_birth'],
        data['sex'],
        data['height'],
        data['weight'],
        data['eyes'],
        data['issue_date'],
        data['expires_date'],
        data['class_drive'],
        data['restrictions'],
        data['duplicate_num'],
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
