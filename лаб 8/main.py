from PIL import Image, ImageFont, ImageDraw

def proc1():

    image = Image.open('newcard.jpg')
    imcrop = image.crop((100, 100, 400, 400))
    imcrop.save('imcropped.jpg')
    imcrop.show()

def proc2():
    s = {'Новый год': 'ny.jpg', '8 марта': 'marta.jpg', '1 мая': 'may1.jpg', 'Рождество': 'roch.jpg'}
    p = input('Какой праздник? ')
    img = Image.open(s[p])
    img.show()

def proc3():
    image = Image.open('newcard.jpg')
    name = input('Введите имя: ')
    fon = ImageFont.truetype('arial_bold.ttf', 40)
    img = ImageDraw.Draw(image)
    img.text((40, 400), name + ', поздравляю!', font = fon, fill = 'white')
    image.show()

proc1(), proc2(), proc3()