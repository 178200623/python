'''
用于获取 txt 文本集与依次显示 txt 文本集，
以达到在终端播放字符动画的效果。
运行之前请修改视频目录「videoPath」、txt 文件夹目录「txt_dir_path」、images 文件夹目录「img_dir_path」。
然后运行 play.py
'''
import sys, os
import time
import image2txt

def getTxt(imagePath, txtPath):
	img_count = 1
	while img_count <= len(os.listdir(imagePath)):
		imageFile = imagePath + str(img_count) + '.png'
		txtFile = txtPath + str(img_count) + '.txt'
		image2txt.image2txt(imageFile, txtFile)
		print('骚能程序员加载中： ' + str(img_count) + '%')
		img_count += 1

def play(txtPath):
	txt_count = 1
	while txt_count <= len(os.listdir(txtPath)):
		os.system('type ' + txtPath + str(txt_count) + '.txt')
		time.sleep(1.0/40)
		txt_count += 1
		os.system('cls')

if __name__ == '__main__':
	txt_dir_path = r'D:\github\python\ImageTest\text' + '\\'
	img_dir_path = r'D:\github\python\ImageTest\images' + '\\'
	getTxt(img_dir_path, txt_dir_path)
	play(txt_dir_path)
