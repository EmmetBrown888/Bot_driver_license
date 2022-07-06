import re
from main import bot


async def validate_form(form_field, state, message):
    pattern_date = r'(\d{1,2}-\d{1,2}-\d{4})'
    pattern_name = r'([A-Z]|[a-z]+)([^[A-Z]|[a-z]]|$)'
    if form_field == 'num_licence':
        amount_num = (10 if state == 'Arkansas' else 7)
        if not message.text.isdigit() or not len(message.text) == amount_num:
            await bot.send_message(
                message.from_user.id,
                f'Водительская лицензия должна состоять из {amount_num} цифр!', parse_mode='Markdown')

            await bot.send_message(
                message.from_user.id, 'Введите номер водительской лицензии', parse_mode='Markdown')
        else:
            return True
    elif form_field == 'date_of_birth':
        if not re.search(pattern_date, message.text):
            await bot.send_message(
                message.from_user.id,
                f'Дата рождения должна быть в формате: месяц-день-год!', parse_mode='Markdown')

            await bot.send_message(
                message.from_user.id, 'Введите дату рождения в формате: месяц-день-год', parse_mode='Markdown')
        else:
            return True
    elif form_field == 'sex':
        if message.text not in ['F', 'M']:
            await bot.send_message(
                message.from_user.id,
                f'Пол должен состоять из одной буква, пример F или M!', parse_mode='Markdown')

            await bot.send_message(
                message.from_user.id, 'Введите пол, например F или M', parse_mode='Markdown')
        else:
            return True
    elif form_field == 'height':
        pattern_height = r'(\d{1}-\d{2})'
        if not re.search(pattern_height, message.text):
            await bot.send_message(
                message.from_user.id,
                f'Рост должен быть по примеру: 5-09!', parse_mode='Markdown')

            await bot.send_message(
                message.from_user.id, 'Введите рост, например 5-09', parse_mode='Markdown')
        else:
            return True
    elif form_field == 'eyes':
        pattern_eyes = r'(^|[^A-Z])[A-Z]{3}([^A-Z]|$)'
        if not re.search(pattern_eyes, message.text):
            await bot.send_message(
                message.from_user.id,
                f'Цвет глаз должен быть по примеру: BLU', parse_mode='Markdown')

            await bot.send_message(
                message.from_user.id, 'Введите цвет глаз, например BLU', parse_mode='Markdown')
        else:
            return True
    elif form_field == 'issue_date':
        if not re.search(pattern_date, message.text):
            await bot.send_message(
                message.from_user.id,
                f'Дата выпуска водительских прав должна быть в формате: месяц-день-год!',
                parse_mode='Markdown'
            )

            await bot.send_message(
                message.from_user.id,
                'Введите дату выпуска водительских прав в формате: месяц-день-год',
                parse_mode='Markdown'
            )
        else:
            return True
    elif form_field == 'expires_date':
        if not re.search(pattern_date, message.text):
            await bot.send_message(
                message.from_user.id,
                f'Дата окончания годности водительских прав должна быть в формате: месяц-день-год!',
                parse_mode='Markdown'
            )

            await bot.send_message(
                message.from_user.id,
                'Введите дату окончания годности водительских прав в формате: месяц-день-год',
                parse_mode='Markdown'
            )
        else:
            return True
    elif form_field == 'class_drive':
        if not message.text in ['B', 'D', 'C', 'E']:
            await bot.send_message(
                message.from_user.id,
                f'Класс водительских прав должен быть например: B',
                parse_mode='Markdown'
            )

            await bot.send_message(
                message.from_user.id,
                'Введите класс водительских прав, например B',
                parse_mode='Markdown'
            )
        else:
            return True
    elif form_field == 'first_name':
        if not re.search(pattern_name, message.text):
            await bot.send_message(
                message.from_user.id,
                f'Имя должно быть наример: Peter', parse_mode='Markdown')

            await bot.send_message(
                message.from_user.id, 'Введите Имя, например Peter', parse_mode='Markdown')
        else:
            return True
    elif form_field == 'last_name':
        if not re.search(pattern_name, message.text):
            await bot.send_message(
                message.from_user.id,
                f'Фамилия должна быть наример: Jackson', parse_mode='Markdown')

            await bot.send_message(
                message.from_user.id, 'Введите Фамилию, например Jackson', parse_mode='Markdown')
        else:
            return True
    elif form_field == 'weight':
        pattern_weight = r'(\d{3})'
        if not re.search(pattern_weight, message.text):
            await bot.send_message(
                message.from_user.id,
                f'Вес должен быть наример: 172', parse_mode='Markdown')

            await bot.send_message(
                message.from_user.id, 'Введите вес, например 165', parse_mode='Markdown')
        else:
            return True
    elif form_field == 'restrictions':
        if not message.text.isdigit() or not len(message.text) == 1:
            await bot.send_message(
                message.from_user.id,
                f'Номер ограничения должен состоять из одной цифры!', parse_mode='Markdown')

            await bot.send_message(
                message.from_user.id, 'Введите номер ограничения, например 1', parse_mode='Markdown')
        else:
            return True
    elif form_field == 'duplicate_num':
        if not message.text.isdigit() or not len(message.text) == 1:
            await bot.send_message(
                message.from_user.id,
                f'Номер дубликата должен состоять из одной цифры!', parse_mode='Markdown')

            await bot.send_message(
                message.from_user.id, 'Введите номер дубликата, например 2', parse_mode='Markdown')
        else:
            return True
