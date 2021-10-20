from Captcha.CaptchaGenerator import Captcha
from PIL import Image
import os
from Json.Reader import Reader
from Json.Writer import Writer

generator = Captcha('Json\\settings.json')
image_index = 0
reader, writer = Reader('Json\\settings.json'), Writer()
work = True
print('You can use class "Captcha" in your project')

while work:
    qty = int(input('How many captchas to generate: '))
    name = input('Name json file with captcha answers(with end .json): ')
    dir_name = input('Name folder with generated captcha: ')
    try:
        with open('{0}\\{1}'.format(dir_name, name), 'w', encoding='utf-8') as f:
            f.write('{}')
    except FileNotFoundError:
        os.mkdir(dir_name)
        with open('{0}\\{1}'.format(dir_name, name), 'w', encoding='utf-8') as f:
            f.write('{}')

    while image_index < qty:
        image, answer = generator.generate()
        image.save('{0}\\captcha_{1}.jpg'.format(dir_name, image_index))
        tmp = reader.read_filename('{0}\\{1}'.format(dir_name, name))
        tmp['captcha_' + str(image_index)] = answer
        writer.write_filename('{0}\\{1}'.format(dir_name, name), tmp)
        print('{0} captcha was created...'.format(image_index))
        image_index += 1
    if input('Continue?(y/n)').lower() == 'n':
        work = False

