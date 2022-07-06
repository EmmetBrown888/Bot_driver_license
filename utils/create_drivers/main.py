from PIL import Image, ImageDraw, ImageFont


class DriverLicense:

    def __init__(self, photo_user, telegram_id):
        self.main_img = None
        self.big_photo = None
        self.small_photo = None
        self.photo_user = photo_user
        self.telegram_id = telegram_id

    def change_size_img(self, param_big, param_small):
        """Изменение размера изображения пользователя"""
        try:
            img = Image.open(self.photo_user)
            img = img.resize(param_big, Image.ANTIALIAS)
            self.big_photo = img
            img = img.resize(param_small, Image.ANTIALIAS)
            self.small_photo = img
        except Exception as exc:
            print('Exception change size img: ', exc)

    def add_photo(self, coordinate_big, coordinate_small):
        """Добавление фото на водительские права"""
        try:
            # Big photo
            background = self.main_img
            foreground = self.big_photo
            background.paste(foreground, coordinate_big, foreground.convert('RGBA'))

            # Small photo
            foreground = self.small_photo
            background.paste(foreground, coordinate_small, foreground.convert('RGBA'))
            self.main_img = background
        except Exception as exc:
            print('Exception add photo: ', exc)

    def save_result(self, path_back):
        """Сохранение результата"""
        try:
            background = Image.open(path_back)
            rgb_im = background.convert('RGB')
            foreground = self.main_img
            rgb_im.paste(foreground, (0, 0), foreground.convert('RGBA'))
            rgb_im.save(f'photos/from_user/{self.telegram_id}.jpg')
        except Exception as exc:
            print('Exception save result: ', exc)


class Alaska(DriverLicense):

    def __init__(self, photo_user, telegram_id, num_licence, date_of_birth, sex, height, weight, eyes, issue_date,
                 expires_date, class_drive, restrictions, duplicate_num, address):
        super().__init__(photo_user, telegram_id)
        self.num_licence = num_licence
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.height = height
        self.weight = weight
        self.eyes = eyes
        self.issue_date = issue_date
        self.expires_date = expires_date
        self.class_drive = class_drive
        self.restrictions = restrictions
        self.duplicate_num = duplicate_num
        self.address = address

    def add_text(self):
        """Добавление текста на изображения"""
        try:
            img = Image.open('utils/create_drivers/documents/alaska/blank.png')
            draw = ImageDraw.Draw(img)
            font_42 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 42)
            font_45 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 45)
            font_46 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 46)
            font_47 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 47)
            font_53 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 53)
            font_56 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 56)
            font_57 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 57)
            font_58 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 58)
            font_59 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 59)
            font_88 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 88)
            draw.text((1270, 185), self.num_licence, (0, 0, 0), font=font_88)
            draw.text((550, 534), self.date_of_birth, (0, 0, 0), font=font_57)
            draw.text((910, 534), self.sex, (0, 0, 0), font=font_59)
            draw.text((1044, 534), self.height, (0, 0, 0), font=font_57)
            draw.text((1257, 534), self.weight, (0, 0, 0), font=font_58)
            draw.text((1474, 534), self.eyes, (0, 0, 0), font=font_53)
            draw.text((550, 651), self.issue_date, (0, 0, 0), font=font_56)
            draw.text((550, 764), self.expires_date, (0, 0, 0), font=font_56)
            draw.text((1284, 608), self.class_drive, (0, 0, 0), font=font_42)
            draw.text((1284, 661), "NONE", (0, 0, 0), font=font_46)
            draw.text((1284, 720), self.restrictions, (0, 0, 0), font=font_42)
            draw.text((1284, 773), self.duplicate_num, (0, 0, 0), font=font_45)
            draw.text((53, 822), self.address, (0, 0, 0), font=font_47)
            rgb_im = img.convert('RGB')
            self.main_img = rgb_im
        except Exception as exc:
            print('Exception add text: ', exc)

    def run(self):
        """Запуск программы"""
        try:
            self.add_text()
            self.change_size_img(param_big=(490, 605), param_small=(138, 173))
            self.add_photo(coordinate_big=(25, 11), coordinate_small=(1467, 594))
            self.save_result(path_back='utils/create_drivers/documents/alaska/background.png')
        except Exception as ex:
            print('Exception create alaska drivers: ', ex)
        finally:
            if self.big_photo:
                self.big_photo.close()
            if self.small_photo:
                self.small_photo.close()
            if self.main_img:
                self.main_img.close()


class Arkansas(DriverLicense):

    def __init__(self, photo_user, telegram_id, num_licence, date_of_birth, sex, height, eyes, issue_date, expires_date,
                 class_drive, first_name, last_name, address):
        super().__init__(photo_user, telegram_id)
        self.num_licence = num_licence
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.height = height
        self.eyes = eyes
        self.issue_date = issue_date
        self.expires_date = expires_date
        self.class_drive = class_drive
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def add_text(self):
        """Добавление текста на изображения"""
        img = Image.open('utils/create_drivers/documents/arkansas/blank.png')
        draw = ImageDraw.Draw(img)
        font_24 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 24)
        font_25 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 25)
        font_26 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 26)
        font_28 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 28)
        font_34 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 34)
        font_38 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 38)
        font_37 = ImageFont.truetype('utils/create_drivers/font/ArialMT_Bolddmt.ttf', 37)

        draw.text((116, 119), self.num_licence, (0, 0, 0), font=font_38)
        draw.text((478, 120), self.date_of_birth, (0, 0, 0), font=font_37)
        draw.text((378, 186), self.first_name.upper(), (0, 0, 0), font=font_37)
        draw.text((378, 222), self.last_name.upper(), (0, 0, 0), font=font_37)
        draw.text((373, 293), self.address.upper(), (0, 0, 0), font=font_34)
        # draw.text((375, 322), "HMHT, AR 77203".upper(), (0, 0, 0), font=font_34)
        draw.text((389, 438), self.issue_date, (0, 0, 0), font=font_25)
        draw.text((603, 438), self.expires_date, (0, 0, 0), font=font_28)
        draw.text((390, 506), self.sex, (0, 0, 0), font=font_24)
        draw.text((677, 505), self.eyes, (0, 0, 0), font=font_26)
        rgb_im = img.convert('RGB')
        self.main_img = rgb_im

    def run(self):
        """Запуск программы"""
        try:
            self.add_text()
            self.change_size_img(param_big=(344, 394), param_small=(186, 213))
            self.add_photo(coordinate_big=(16, 211), coordinate_small=(779, 359))
            self.save_result(path_back='utils/create_drivers/documents/arkansas/background.png')
        except Exception as ex:
            print('Exception create arkansas drivers: ', ex)
        finally:
            if self.big_photo:
                self.big_photo.close()
            if self.small_photo:
                self.small_photo.close()
            if self.main_img:
                self.main_img.close()
