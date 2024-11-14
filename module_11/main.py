from PIL import Image
from PIL import ImageDraw, ImageFont

def new_photo(name, w_del=2, h_del=2):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w//w_del, h//h_del))


im = new_photo('photo.jpg')
moon = new_photo('moon.png', 5, 5)

im.paste(moon, (100, 50))

draw = ImageDraw.Draw(im)
font = ImageFont.truetype('arialmt.ttf', 50)
draw.text((1000, 80), 'Hi, BMW', font=font, fill='#1b877e')

im.show()