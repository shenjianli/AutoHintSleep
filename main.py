# This is a sample Python script.
# -*- coding: UTF-8 -*-
import os
import time

import cv2
import pyperclip
import pyautogui

from notify.WeChatNotification import WeChatPub


def paste_content(name):
    pyperclip.copy(name)
    time.sleep(1)
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command')
    pyautogui.press('enter')


def init_wechat_points():
    points1 = [pyautogui.Point(x=316, y=117),
               pyautogui.Point(x=601, y=658)]
    return points1


# 执行点集操作 points 点集合
def auto_start_run(points):
    pyautogui.PAUSE = 1
    # 执行收集的点点击操作
    if len(points) > 0:
        for point in points:
            pyautogui.moveTo(point, duration=1)
            pyautogui.click(point)
            time.sleep(2)
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


# auto
def auto_img_click(clickImgFile, whatDo, debug = True):
    pyautogui.screenshot('big.png')
    gray = cv2.imread("big.png", 0)
    img_template = cv2.imread(clickImgFile, 0)

    w, h = img_template.shape[::-1]
    res = cv2.matchTemplate(gray, img_template, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top = min_loc[0]
    left = min_loc[1]
    x = [top, left, w, h]

    top_left = min_loc  # 左上角的位置
    bottom_right = (top_left[0] + w, top_left[1] + h)  # 右下角的位

    # 先移动再操作， 进行点击动作，可以修改为其他动作
    pyautogui.moveTo(top + h / 2, left + w / 2)
    whatDo(x)

    if debug:
        # 读取原图
        img = cv2.imread("big.png", 1)
        # 在原图上画矩形
        cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)
        # 调试显示
        img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_NEAREST)
        cv2.imshow("processed", img)
        cv2.waitKey(0)
        # 销毁所有窗口
        cv2.destroyAllWindows()
    os.remove("big.png")


# 打开应用
def open_app(name):
    os.system('open /Applications/' + name + '.app')


# 打开桌面的Android Studio
def open_as():
    os.system('open /Users/jerry/Desktop/Android_Studio.app')


def min_current_window():
    pyautogui.keyDown('command')
    pyautogui.press('m')
    pyautogui.keyUp('command')
    print('min_current_window')


def click_min():
    min_point = [pyautogui.Point(x=44, y=51)]
    auto_start_run(min_point)


def start_safari():
    open_app('Safari')
    print("打开 Safari 成功")
    time.sleep(2)
    safari_points = [pyautogui.Point(x=15, y=93),
                     pyautogui.Point(x=999, y=53)]
    auto_start_run(safari_points)
    print("请使用opt扫描二维码登录")
    input("输入任意字符继续")
    click_min()


def start_wechat():
    open_app('WeChat')
    print("打开微信成功")
    time.sleep(2)
    wechat_points = [pyautogui.Point(x=714, y=513)]
    auto_start_run(wechat_points)
    print("请在手机上点击登录微信")
    input("输入任意字符继续")
    wechat_points = [pyautogui.Point(x=258, y=114)]
    auto_start_run(wechat_points)


def start_qq():
    open_app('QQ')
    print("打开QQ成功")
    time.sleep(2)
    qq_points = [pyautogui.Point(x=688, y=547)]
    auto_start_run(qq_points)
    paste_content('233619298662shen')
    time.sleep(5)
    qq_points = [pyautogui.Point(x=231, y=49)]
    auto_start_run(qq_points)


def start_as():
    open_as()
    time.sleep(15)
    as_points = [pyautogui.Point(x=722, y=206)]
    auto_start_run(as_points)


def start_outlook():
    open_app('Microsoft_Outlook')
    time.sleep(2)
    as_points = [pyautogui.Point(x=955, y=341),
                 pyautogui.Point(x=38, y=38)]
    auto_start_run(as_points)


def start_power_on():
    start_safari()
    start_wechat()
    start_qq()
    start_as()


def close_terminal():
    os.system('killall Terminal')


def close_app(name):
    #os.system('sudo -S osascript -e \'tell application "' + name + '" to shut down\' < password.secret')
    os.system('killall -9 ' + name)
    print("killall -9 " + name)


def scroll_top():
    pyautogui.moveTo(pyautogui.Point(x=316, y=500), duration=1)
    pyautogui.scroll(1000)


def notify_to_wechat(content):
    open_app('WeChat')
    points = [pyautogui.Point(x=316, y=500)]
    auto_start_run(points)
    time.sleep(5)
    scroll_top()
    print('滚动到顶')
    auto_start_run(init_wechat_points())
    paste_content(content)


# 进行页面刷新
def refresh_page():
    pyautogui.PAUSE = 1
    # 执行收集的点点击操作
    point = pyautogui.Point(x=15, y=93)
    pyautogui.moveTo(point, duration=1)
    pyautogui.click(point)
    time.sleep(2)

    point = pyautogui.Point(x=999, y=53)
    pyautogui.moveTo(point, duration=1)
    pyautogui.click(point)
    time.sleep(3)

    # 操作结果屏幕截图
    print("刷新成功")


def notify_sign_out():
    wechat = WeChatPub()
    wechat.send_hint("今日已执行签退")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    time.sleep(3)
    # refresh_page()
    # open_app('WeChat')
    # scroll_top()
    # notify_to_wechat('ok')
    # scroll_top()
    # start_outlook()
    # close_app("WeChat")

    notify_sign_out()
    # start_power_on()
    # start_safari()
    # start_wechat()
    # start_qq()
    # start_as()
    # open_as()
    # start_add_point()
    # points = [pyautogui.Point(x=95, y=494),
    #           pyautogui.Point(x=15, y=93)]
    # auto_start_run(points)
    # start_add_point()
    # notify_to_wechat('执行成功')
    # time.sleep(5)
    # auto_img_click("wechat.png", pyautogui.click)
    # print("请8秒移动鼠标到任务栏微信图标中间")
    # time.sleep(1)
    #
    # print("第一个坐标：", pyautogui.position())
    # print_hi('PyCharm')
    #
    #
    # print("请8秒移动鼠标到微信聊天输入文字点")
    # #time.sleep(8)
    # print("第二个坐标：", pyautogui.position())

    # os.system('sudo -S shutdown -h now < password.secret')
    # os.system('cd /Users/jerry/Applications')
    # os.system('ls -al')
    # os.system('open /Applications/WeChat.app')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
