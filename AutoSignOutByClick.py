# -*- coding: UTF-8 -*-
import os
import random
import threading
import time

import pyautogui
import pyperclip

import CaptureScreen

# 可以正常运行

# 第1个点为签退页面标签点，        Point(x=15, y=93)
# 第2个点为页面刷新点             Point(x=999, y=53)
# 第3个点为签退按钮点             Point(x=113, y=230)
# 第4个点为弹框确认点             Point(x=886, y=495)
# 第5个点为关闭弹框点             Point(x=995, y=409)
# 第6个点为切换其他页面标签点      Point(x=122, y=90)

# 是否要自行录入点击位置
is_input_point = False
# 需要执行的点坐标
points = []

# 签退时间小时数 [18-23]
SIGN_OUT_HOUR = 19
# 签退时间分钟基数取值 [11-49]
SIGN_OUT_MIN = 48
# 签退时间分钟随机数
SING_OUT_RAN_MIN = 0 # random.randint(0, 10)

# 刷新小时时间
currentHour = 0

is_run = False
is_start = True


# 执行点集操作
def auto_start_run():
    global is_run
    is_run = True
    pyautogui.PAUSE = 1

    # 执行收集的点点击操作
    if len(points) > 0:
        # 开始执行前屏幕截图
        CaptureScreen.captare_one_screen()
        for point in points:
            pyautogui.moveTo(point, duration=1)
            pyautogui.click(point)
            time.sleep(2)
            # 操作结果屏幕截图
            CaptureScreen.captare_one_screen()
        print("操作执行成功")
    else:
        print("没有坐标点\n")
    print("方法调用完成\n")


# 执行点集操作 points 点集合
def start_run_by_points(points):
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


# 进行页面刷新
def refresh_page():
    pyautogui.PAUSE = 1
    # 执行收集的点点击操作
    if len(points) > 2:
        point = points[0]
        pyautogui.moveTo(point, duration=1)
        pyautogui.click(point)
        time.sleep(2)

        point = points[1]
        pyautogui.moveTo(point, duration=1)
        pyautogui.click(point)
        time.sleep(3)

        # 操作结果屏幕截图
        CaptureScreen.captare_one_screen()
        print("刷新成功")


# 执行完签退操作，进行关机
def auto_shut_down():
    close_app("WeChat")
    close_app("Safari")
    close_app("QQ")
    # password.secret 为电脑密码
    os.system('sudo -S shutdown -h now < password.secret')


# 开始采集点击位置坐标
def start_add_point():
    while True:
        cmd = input("请移动鼠标到采集点位置，然后回车进行采集:(按q完成采集)\n")
        if cmd == 'q':
            break
        else:
            points.append(pyautogui.position())
            print("采集了坐标点：", pyautogui.position())
    print("完成坐标采集，", points)


# 线程执行循环查询签退时间
def start_run():
    global is_run
    global currentHour
    global SING_OUT_RAN_MIN
    while is_start:
        localtime = time.localtime()
        weekDay = localtime.tm_wday
        hour = localtime.tm_hour
        current_min = localtime.tm_min
        print("当前时间", localtime)
        if 0 <= weekDay <= 6:
            if hour == SIGN_OUT_HOUR:
                print("is run", is_run)
                if current_min == (SIGN_OUT_MIN + SING_OUT_RAN_MIN) and is_run == 0:
                    open_app('Safari')
                    print("打开 Safari 成功")
                    time.sleep(1)
                    refresh_page()
                    scroll_top()
                    # 执行签退点集
                    auto_start_run()
                    time.sleep(2)
                    # 微信通知
                    notify_to_wechat("ok")
                    time.sleep(2)
                    open_app('Safari')
                    time.sleep(10)
                    SING_OUT_RAN_MIN = random.randint(0, 10)
                    print("产生的随机数", SING_OUT_RAN_MIN)
                    auto_shut_down()
                    # 表示周五晚上签退完成，关机
                    # if weekDay >= 4:
                    #     auto_shut_down()
                else:
                    print("非需要分钟\n")
                    time.sleep(20)
                    # if currentHour != hour:
                    #     open_app('Safari')
                    #     refresh_page()
                    #     currentHour = hour
            else:
                is_run = False
                print("非需要小时\n")
                time.sleep(60 * 10)
                # 日常工作点不需要刷新
                if hour > 19 or hour < 10:
                    if currentHour != hour:
                        refresh_page()
                        currentHour = hour
                    elif hour == 4:
                        refresh_page()
                        time.sleep(60 * 10)
        else:
            print("非工作日，不进行执行\n")
            time.sleep(60 * 60 * 4)


# 可以正常运行
# 第1个点为签退页面标签点，        Point(x=15, y=93)
# 第2个点为页面刷新点             Point(x=999, y=53)
# 第3个点为签退按钮点             Point(x=113, y=230)
# 第4个点为弹框确认点             Point(x=886, y=495)
# 第5个点为关闭弹框点             Point(x=995, y=409)
# 第6个点为切换其他页面标签点      Point(x=122, y=90)


# 初始化操作点集
def init_sign_out_points():
    points.append(pyautogui.Point(x=15, y=93))
    points.append(pyautogui.Point(x=999, y=53))
    points.append(pyautogui.Point(x=113, y=230))
    points.append(pyautogui.Point(x=886, y=495))
    points.append(pyautogui.Point(x=995, y=409))
    points.append(pyautogui.Point(x=122, y=90))


# 打开应用
def open_app(name):
    os.system('open /Applications/' + name + '.app')


def close_app(name):
    #os.system('sudo -S osascript -e \'tell application "' + name + '" to shut down\' < password.secret')
    os.system('killall -9 ' + name)
    print("killall -9 " + name)


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


def notify_to_wechat(content):
    open_app('WeChat')
    time.sleep(1)
    scroll_top()
    start_run_by_points(init_wechat_points())
    paste_content(content)
    CaptureScreen.captare_one_screen()


def scroll_top():
    pyautogui.moveTo(pyautogui.Point(x=316, y=500), duration=1)
    pyautogui.scroll(1000)


# 主函数
if __name__ == '__main__':
    sumMin = SIGN_OUT_MIN + SING_OUT_RAN_MIN
    print("签退时间：", str(SIGN_OUT_HOUR) + ":" + str(sumMin))
    # 不用录入点签退，自动执行
    if is_input_point == 0:
        init_sign_out_points()
        threading.Thread(target=start_run).start()
        cmd = input("输入任意字符退出\n")
    else:
        # 自主录入签退点
        start_add_point()
        cmd = input('a开始启动，q退出\n')
        while cmd != 'q':
            if cmd == 'a':
                print('启动遍历\n')
                threading.Thread(target=start_run).start()
                cmd = input("输入q退出\n")
            else:
                cmd = input('a开始启动，q退出\n')
