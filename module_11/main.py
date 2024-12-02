from PIL import Image
from PIL import ImageDraw, ImageFont


class PostMaker:
    def __init__(self, name_photo):
        self.image = Image.open(name_photo)
        self.w, self.h = self.image.size
        self.image = self.image.resize((self.w // 2, self.h // 2))

    def paste(self, name_photo):
        paste_image = Image.open(name_photo)
        paste_image = paste_image.resize((paste_image.size[0] // 3, paste_image.size[1] // 3))
        self.image.paste(paste_image, (50, 50))

    def upgrade(self, text):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype('arialmt.ttf', 50)
        draw.text((1000, 80), text, font=font, fill='#1b877e')
        self.image.show()


def new_photo(name, w_del=2, h_del=2):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w//w_del, h//h_del))


image = PostMaker('photo.jpg')
image.paste('moon.png')
image.upgrade('Hi, BMW!')