'''
用于将图片转化为一定尺寸的字符画，
从「images/」文件夹中提取图片并转化为 txt 文本存放于「txt/」文件夹。
默认要求的终端尺寸为 100x50 ，若屏幕不能支持该大小，可以将参数 charWidth 修改为自定义的每行显示字符数，
调整后若运行 play.py 要求终端大小为 (charWidth)x(charWidth/2) 。
参数值具体多少，没有一个固定的值，可以自己多尝试下
'''
from PIL import Image
import numpy
def image2txt(inputFile, outputFile):
    im = Image.open(inputFile).convert('L')
    charWidth = 100
    im = im.resize((charWidth,charWidth//2))
    target_width,target_height = im.size
    data = numpy.array(im)[:target_height, :target_width]
    f = open(outputFile,'w',encoding='utf-8')
    for row in data:
        for pixel in row:
            if pixel > 127:
                f.write('1')
            else:
                f.write(' ')
        f.write('\n')
    f.close()