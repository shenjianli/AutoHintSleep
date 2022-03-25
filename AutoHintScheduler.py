import time

import pyautogui
from datetime import datetime,tzinfo,timedelta

import pyperclip
from apscheduler.schedulers.background import BackgroundScheduler


def auto_start_hint():
    pyautogui.PAUSE = 1
    # 微信icon位置
    # icon_position = pyautogui.Point(x=451, y=847)
    entry_position = pyautogui.Point(x=346, y=543)

    # pyautogui.moveTo(icon_position, duration=2)
    # pyautogui.click(icon_position)

    pyautogui.moveTo(entry_position, duration=1)
    pyautogui.click(entry_position)

    pyperclip.copy('开始工作了')
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command')
    pyautogui.press('enter')

    pyperclip.copy('小伙')
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command')
    pyautogui.press('enter')
    print("提示完成")


def print_time():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('print --- {}'.format(t))


if __name__ == '__main__':
    print(pyautogui.position())
    scheduler = BackgroundScheduler(timezone='Asia/Shanghai')
    # corn 是周期  interval是间隔  date 是具体日期
    # 每间隔1分3秒执行一次
    # scheduler.add_job(print_time, 'interval', seconds=3, minutes=1)
    # 表示星期一到星期六，每天12：21执行一次
    scheduler.add_job(print_time, 'cron', hour='12', minute='21', day_of_week='0-5')
    scheduler.start()
    input("输入结束\n")

