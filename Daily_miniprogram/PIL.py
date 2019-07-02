"""第 0000 题：**将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果"""
from PIL import Image,ImageFont,ImageDraw,ImageColor

def add_num(image,text):
    #打开图片然后设置字体
    font = ImageFont.truetype("arial.ttf",50)
    #设置字体颜色
    fontcolor = ImageColor.colormap.get('red')
    #将字体加到图片上
    draw = ImageDraw.Draw(image)
    width, height = image.size
    draw.text((width - 50, 30), text, font=font, fill=fontcolor)
    #保存图片
    image.save("D:\\image2.jpg")

if __name__ == '__main__':
    image = Image.open('D:\\thumbnail.jpg')
    text = "4"
    add_num(image,text)
