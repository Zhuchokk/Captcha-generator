from PIL import Image, ImageDraw, ImageFont
from Json.Reader import Reader
import random


class Captcha:
    def __init__(self, path_to_settings):
        self.path = path_to_settings
        self.reader = Reader(self.path)
        self.settings = self.reader.read()
        self.dictionary = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.font = ImageFont.truetype('arial.ttf', size=40)
        self.image_height = 60
        self.image_width = 0

    def generate(self):
        captcha = Image.new('RGB', (self.settings['qty_letters'] * 50, 60))
        captcha_text = ''
        draw_captcha = ImageDraw.Draw(captcha)
        x = 0
        for i in range(self.settings['qty_letters']):
            captcha_text += random.choice(self.dictionary)

        for letter in captcha_text:
            letter_image = Image.new('RGB', (50, self.image_height))
            letter_draw = ImageDraw.Draw(letter_image)
            letter_draw.text((random.randint(0, 15), random.randint(0, 15)), letter, font=self.font)
            angle = random.randint(self.settings['min_rotate_letter'], self.settings['max_rotate_letter'])
            letter_image = letter_image.rotate(angle)
            captcha.paste(letter_image, (x, 0))
            x += 50
        for i in range(random.randint(1, 3)):
            draw_captcha.line((random.randint(0, 15), random.randint(20, 40),
                               self.settings['qty_letters'] * 50 - random.randint(1, 15), random.randint(5, 55)),
                              fill="white", width=random.randint(1, 3))

        pixels = list(captcha.getdata())
        for i in range(self.settings['qty_letters'] * 50 * 60):
            if random.randint(1, 100 // self.settings['point_noise_percent']) == 1:
                color = random.randint(50, 200)
                pixels[i] = (color, color, color)
            if pixels[i] == (255, 255, 255):
                pixels[i] = (0, 0, 0)
            elif pixels[i] == (0, 0, 0):
                pixels[i] = (255, 255, 255)

        captcha.putdata(pixels)
        captcha.show()
        return captcha


c = Captcha('..\\Json\\settings.json')
c.generate()