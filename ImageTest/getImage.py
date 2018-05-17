'''
是用于从视频中提取帧图片，提取的帧图片存放于「images/」文件夹，
若文件夹中已存在帧图片可不运行该程序。
若要调整每帧图片数可调整变量 crop_time 累加的数值，
清空已存在的图片集，修改视频路径「videoPath」、帧图片目录路径「imagePath」，
再运行 getImage.py。
'''
import os
import ffmpeg
def getImage(videoPath,imagePath):
    img_count = 1
    crop_time = 0.0
    while crop_time <= 15.0:
        #'ffmpeg -i D:\\github\\python\\ImageTest\\movies\\mo.mp4 -f image2 -ss 0.5 -vframes 1 D:\\github6.png'
        cmd = 'ffmpeg -i '+ videoPath +' -f image2 -ss '+str(crop_time)+' -vframes 1 '+imagePath+'\\'+str(img_count)+'.png'
        print(cmd)
        os.system(cmd)
        img_count += 1
        #print('Geting Image' + str(img_count) + '.png' +'from time ' + str(crop_time))
        crop_time += 0.1
    print('Image Collected')


if __name__ == '__main__':
    videoPath = 'D:\github\python\ImageTest\movies\mo.mp4'
    imagePath = 'D:\github\python\ImageTest\images'
    getImage(videoPath,imagePath)