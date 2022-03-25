import time

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler


def job(text):
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('{} --- {}'.format(text, t))


def block_scheduler():
    sched = BlockingScheduler(timezone='MST')
    sched.add_job(job, 'interval', id='3_second_job', seconds=3, args=['block_scheduler'])
    sched.start()


def background_scheduler():
    job("start")
    sched = BackgroundScheduler(timezone='MST')
    sched.add_job(job, 'interval', id='3_second_job', seconds=3, args=["background_scheduler"])
    sched.start()
    while True:
        print('main 1s')
        time.sleep(1)


def sign_out():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('sign out --- {}'.format(t))


def sign_out_every_day():
    sched = BackgroundScheduler(timezone='Asia/Shanghai')
    # 表示星期一到星期六，第天晚上19：30执行一次
    sched.add_job(sign_out, 'cron', hour='18', minute='5', day_of_week='0-5')
    sched.start()
    print("后台 启动 签退 计划")


def sign_in():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('sign in --- {}'.format(t))


def sign_in_very_day():
    sched = BackgroundScheduler(timezone='Asia/Shanghai')
    # 表示星期一到星期六，第天早上9：05执行一次
    sched.add_job(sign_in, 'cron', hour='13', minute='0', day_of_week='0-5')
    sched.start()
    print("后台 启动 签到 计划")


def refresh():
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print('refresh --- {}'.format(t))


def refresh_page():
    print("后台 start 启动 刷新 计划")
    sched = BlockingScheduler(timezone='Asia/Shanghai')
    # 表示第天晚上刷新一次
    sched.scheduled_job(refresh, 'cron', hour='14', minute='6')
    sched.start()
    print("后台 end 启动 刷新 计划")


if __name__ == '__main__':
    sign_in_very_day()
    sign_out_every_day()
    refresh_page()
