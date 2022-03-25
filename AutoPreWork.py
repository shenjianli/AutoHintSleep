# -*- coding: UTF-8 -*-
import os
import time
import pyperclip
import pyautogui


# 可正常运行  桌面 auto_pre_word.sh chmod 777 auto_pre_word.sh  双击执行


def paste_content(name):
    pyperclip.copy(name)
    time.sleep(1)
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command')
    pyautogui.press('enter')


def init_wechat_points():
    points = [pyautogui.Point(x=316, y=117),
              pyautogui.Point(x=601, y=658)]
    return points


# 执行点集操作 points 点集合
def auto_start_run(points):
    pyautogui.PAUSE = 1
    # 执行收集的点点击操作
    if len(points) > 0:
        for point in points:
            pyautogui.moveTo(point, duration=1)
            pyautogui.click(point)
            time.sleep(1)
        print("操作执行成功")
    else:
        print("没有坐标点\n")
    print("方法调用完成\n")


# 采集点
def start_add_point():
    while True:
        cmd = input("请移动鼠标到采集点位置，然后回车进行采集:(按q完成采集)\n")
        if cmd == 'q':
            break
        else:
            print("采集了坐标点：", pyautogui.position())


def notify_to_wechat(content):
    open_app('WeChat')
    auto_start_run(init_wechat_points())
    paste_content(content)


# 打开应用
def open_app(name):
    os.system('open /Applications/' + name + '.app')


# 打开桌面的Android Studio
def open_as():
    os.system('open /Users/jerry/Desktop/Android_Studio.app')


def click_min():
    min_point = [pyautogui.Point(x=44, y=51)]
    auto_start_run(min_point)


def start_safari():
    open_app('Safari')
    print("打开 Safari 成功")
    safari_points = [pyautogui.Point(x=15, y=93)]
    auto_start_run(safari_points)
    print("请使用opt扫描二维码登录")
    input("输入任意字符继续")
    refresh_page()
    click_min()


def refresh_page():
    refresh_points = [pyautogui.Point(x=15, y=93),
                      pyautogui.Point(x=999, y=53)]
    auto_start_run(refresh_points)


def start_wechat():
    open_app('WeChat')
    print("打开微信成功")
    wechat_points = [pyautogui.Point(x=714, y=513)]
    auto_start_run(wechat_points)
    print("请在手机上点击登录微信")
    input("输入任意字符继续")
    wechat_points = [pyautogui.Point(x=157, y=39)]
    auto_start_run(wechat_points)


def start_qq():
    open_app('QQ')
    print("打开QQ成功")
    qq_points = [pyautogui.Point(x=688, y=547)]
    auto_start_run(qq_points)
    paste_content('233619298662shen')
    time.sleep(5)
    qq_points = [pyautogui.Point(x=231, y=49)]
    auto_start_run(qq_points)


def start_as():
    open_as()
    time.sleep(25)
    as_points = [pyautogui.Point(x=722, y=206)]
    auto_start_run(as_points)


dev_path = "/Users/jerry/Desktop/Android/Module-OxfordAndroid-1.0"
dev_path1 = "/Users/jerry/Desktop/oxford/code/dev/Module-OxfordAndroid"


# 更新开发的工程项目
def update_dev_project():
    origin_path = os.getcwd()
    print("当前目录：", os.getcwd())
    print("改变操作目录到cocos下")
    os.chdir(dev_path)
    print("当前目录：", os.getcwd())
    os.system('git pull')
    os.chdir(dev_path1)
    os.system('git pull')
    os.chdir(origin_path)
    print("当前目录：", os.getcwd())


def start_outlook():
    open_app('Microsoft_Outlook')
    time.sleep(20)
    as_points = [pyautogui.Point(x=955, y=341),
                 pyautogui.Point(x=38, y=38)]
    auto_start_run(as_points)


def start_power_on():
    # enter_computer()
    link_to_wifi()
    # start_outlook()
    start_qq()
    update_dev_project()
    # start_as()
    start_wechat()
    start_safari()


def link_to_wifi():
    wifi_points = [pyautogui.Point(x=1188, y=12),pyautogui.Point(x=1054, y=165)]
    auto_start_run(wifi_points)
    time.sleep(2)


def enter_computer():
    paste_content('asdfghjkl;\'')
    time.sleep(10)


# 采集点
def start_add_point():
    while True:
        cmd = input("请移动鼠标到采集点位置，然后回车进行采集:(按q完成采集)\n")
        if cmd == 'q':
            break
        else:
            print("采集了坐标点：", pyautogui.position())


def close_app(name):
    #os.system('sudo -S osascript -e \'tell application "' + name + '" to shut down\' < password.secret')
    os.system('killall -9 ' + name)
    print("killall -9 " + name)


if __name__ == '__main__':
    start_power_on()
    close_app("Terminal")

