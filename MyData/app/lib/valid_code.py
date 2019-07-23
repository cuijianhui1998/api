import random
from io import BytesIO

from PIL import Image,ImageDraw,ImageFont,ImageEnhance


class ValidateCode:
    WIDTH = 400
    HIGH = 200
    def __init__(self,width=400,high=200):
        self.width = width
        self.high = high

    def image_init(self):
        return self._get_image()

    def _get_image(self):
        code = ''.join(self._rand_text())
        im1 = Image.new(mode='RGB', size=(self.WIDTH, self.HIGH), color=(255, 255, 255))
        draw = ImageDraw.Draw(im1, mode='RGB')
        self._back_color(draw)

        for xy, text in zip(self._rand_text_xy(self.WIDTH, self.HIGH), code):
            draw.text(xy=xy, text=text, fill=self._rand_font_color(), font=self._rand_font(self.HIGH))
        for i in range(self._rand_line_count()):
            draw.line(self._rand_line_xy(self.WIDTH, self.HIGH), fill=self._rand_line_color(), width=1)
        im = ImageEnhance.Sharpness(im1).enhance(0.0)
        im.thumbnail((self.width, self.high))
        return (im,code)


    def _rand_font(self,high):
        font_type = ['font/BRADHITC.TTF','font/ebrimabd.ttf','font/segoesc.ttf','font/segoescb.ttf',
                     'font/STFANGSO.TTF','font/times.ttf','font/timesbi.ttf','font/timesi.ttf']
        font_file = random.choice(font_type)
        font_size = random.randint(high//2,high//1.5)
        ft = ImageFont.truetype(font_file,size=font_size)
        return ft

    def _rand_text(self):
        STRTYPE = 'abcdefghijklmnopqrstuvwxyz0123456789'
        texts = [random.choice(STRTYPE) for _ in range(4)]
        return texts
    def _back_color(self,draw):
        for x in range(self.WIDTH):
            for y in range(self.HIGH):
                draw.point((x, y), fill=self._rand_line_color())

    def _rand_line_color(self):
        red = random.randint(32,127)
        green = random.randint(32,127)
        blue = random.randint(32,127)
        return (red,green,blue)
    def _rand_font_color(self):
        red = random.randint(128, 255)
        green = random.randint(128, 255)
        blue = random.randint(128, 255)
        return (red, green, blue)

    def _rand_line_xy(self,width,high):
        start_x = random.randint(0,width)
        start_y = random.randint(0,high)
        end_x = random.randint(0,width)
        end_y = random.randint(0,high)
        return (start_x,start_y,end_x,end_y)

    def _rand_line_count(self):
        return random.randint(70,100)

    def _rand_text_xy(self,width,high):
        code1 = (random.randint(0,width//6),random.randint(high//10,high//2))
        code2 = (random.randint(width//4,width//2),random.randint(high//10,high//2))
        code3 = (random.randint(width//2,width-width//3),random.randint(high//10,high//2))
        code4 = (random.randint(width-width//4,width-width//6),random.randint(high//10,high//2))
        return [code1,code2,code3,code4]

if __name__ == '__main__':
    import base64
    code = ValidateCode(30,15)
    res = code.image_init()
    im = res[0]
    valid = res[1]
    output = BytesIO()
    im.save(output, 'PNG')
    content = output.getvalue()
    ccc = base64.b64encode(content)
    ccc = str(ccc,'utf-8')
    with open('i.png','wb') as f:
        f.write(ccc)
    print(valid)
