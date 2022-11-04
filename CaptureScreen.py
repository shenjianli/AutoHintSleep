# -*- coding: UTF-8 -*-
import os
from os.path import exists
from time import sleep
from PIL import ImageGrab
from os import remove, mkdir, listdir
import time

# 可以正常运行

pic_dir = 'pics'


def create_pic_dir():
    if not exists(pic_dir):
        mkdir(pic_dir)
        print('创建图片目录')
    else:
        print('目录存在，不需要创建')


def captare_one_screen():
    create_pic_dir()
    t = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    ImageGrab.grab().save(f'{pic_dir}/{t}.png',
                          quality=95, subsampling=0)
    print('当前屏幕截图', t)


def record_screen(maxNum):
    print('开始录制屏幕图片')
    index = 0
    while index < maxNum:
        ImageGrab.grab().save(f'{pic_dir}/{index}.png',
                              quality=95, subsampling=0)
        sleep(1)
        index = index + 1
        print('创建屏幕，第{}张图片完成'.format(index))


def delete_pics(pic_path):
    if exists(pic_path):
        files = os.listdir(pic_path)
        for file in files:
            file_data = pic_path + "/" + file
            if os.path.isfile(file_data):
                os.remove(file_data)
            else:
                delete_pics(file_data)


def delete_cache():
    delete_pics(pic_dir)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    delete_cache()
    create_pic_dir()
    record_screen(5)
    captare_one_screen()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
