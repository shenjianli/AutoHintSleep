import pyautogui
from datetime import datetime,tzinfo,timedelta
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import CaptureScreen


# 需要执行的点坐标
points = []


def auto_start_run():
    pyautogui.PAUSE = 1
    # 执行收集的点点击操作
    if len(points) > 0:
        CaptureScreen.captare_one_screen()
        for point in points:
            pyautogui.moveTo(point, duration=1)
            pyautogui.click(point)
            # 操作结果屏幕截图
            CaptureScreen.captare_one_screen()
        print("操作执行成功")
    else:
        print("没有坐标点")
    print("方法调用完成")


class UTC(tzinfo):
    """UTC"""
    def __init__(self, offset=0):
        self._offset = offset

    def utcoffset(self, dt):
        return timedelta(hours=self._offset)

    def tzname(self, dt):
        return "UTC +%s" % self._offset

    def dst(self, dt):
        return timedelta(hours=self._offset)


def start_add_point():
    while True:
        cmd = input("请移动鼠标到采集点位置，然后回车进行采集:(按q完成采集)\n")
        if cmd == 'q':
            break
        else:
            points.append(pyautogui.position())
            print("采集了坐标点：", pyautogui.position())
    print("完成坐标采集，", points)


def hint_launch():
    print("吃午饭喽")


def test():
    print("test")


if __name__ == '__main__':
    # start_add_point()
    # time.sleep(8)
    # print("开始自动执行采集点，点击事件")
    # auto_start_run()

    print("启动定时器执行")
    # scheduler = BlockingScheduler()
    # scheduler.add_job(auto_start_run, 'date', run_date=datetime(2021, 11, 1, 20, 15, tzinfo=UTC(8)))
    # scheduler.start()
    #

    bgScheduler = BackgroundScheduler(timezone='Asia/Shanghai')
    bgScheduler.add_job(test, 'interval', minutes=1)
    bgScheduler.start()
    print('启动后台定时器')

    scheduler = BlockingScheduler(timezone='Asia/Shanghai')
    # 表示星期1到星期6每天  晚上19:30执行签退操作
    scheduler.add_job(hint_launch, 'cron', hour='18', minute='15', day_of_week='0-5')
    scheduler.start()
    print('启动阻塞定时器')


