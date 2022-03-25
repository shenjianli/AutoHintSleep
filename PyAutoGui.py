import pyautogui
import time
import cv2

# 调用执行动作后暂停的秒数，只能在执行一些pyautogui动作后，才能使用
pyautogui.PAUSE = 1
# 启用自动防故障功能
pyautogui.FAILSAFE = True

x, y = 122, 244
# 点是否在屏幕上
result = pyautogui.onScreen(x, y)
print(result)

# 屏幕宽度和高度
width, height = pyautogui.size()
print(width, height)

# 鼠标当前位置
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)


def move_scroll():
    print("开始进行绝对移动")
    for i in range(2):
        pyautogui.moveTo(100, 100, duration=0.25)
        pyautogui.moveTo(200, 100, duration=0.25)
        pyautogui.moveTo(200, 200, duration=0.25)
        pyautogui.moveTo(100, 200, duration=0.25)

    print("开始进行相对移动")
    for i in range(2):
        pyautogui.moveRel(50, 0, duration=0.25)
        pyautogui.moveRel(0, 50, duration=0.25)
        pyautogui.moveRel(-50, 0, duration=0.25)
        pyautogui.moveRel(0, -50, duration=0.25)

    pyautogui.dragTo(100, 200, button='left')
    pyautogui.dragTo(300, 400, 2, button='left')
    pyautogui.dragRel(0, -60, duration=0.2, button='left')

    # pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
    # 其中，button属性可以设置成left，middle和right。
    pyautogui.click(10, 20, 2, 0.25, button='left')
    # 先移动到(100, 200)再单击
    pyautogui.click(x=100, y=200, duration=2)

    pyautogui.click()
    pyautogui.doubleClick()

    # 鼠标在（100，150）位置左击两下
    pyautogui.doubleClick(x=100, y=100, button='left')

    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.mouseDown(button='right')
    pyautogui.mouseUp(button='right', x=100, y=200)

    # scroll函数控制鼠标滚轮的滚动，amount_to_scroll参数表示滚动的格数。正数则页面向上滚动，负数则向下滚动
    # pyautogui.scroll(clicks=amount_to_scroll, x=moveToX, y=moveToY)
    pyautogui.scroll(150, 200, 2)
    pyautogui.scroll(10)
    pyautogui.scroll(-10)
    pyautogui.scroll(10, x=200, y=200)

    # 缓动/渐变函数可以改变光标移动过程的速度和方向。通常鼠标是匀速直线运动，这就是线性缓动/渐变函数。
    # PyAutoGUI有30种缓动/渐变函数，可以通过pyautogui.ease*?查看。

    # 开始很慢，不断加速
    pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)

    # 开始很快，不断减速
    pyautogui.moveTo(200, 200, 2, pyautogui.easeOutQuad)

    # 开始和结束都快，中间比较慢
    pyautogui.moveTo(300, 300, 2, pyautogui.easeInOutQuad)

    # 一步一徘徊前进
    pyautogui.moveTo(400, 400, 2, pyautogui.easeInBounce)

    # 徘徊幅度更大，甚至超过起点和终点
    pyautogui.moveTo(500, 500, 2, pyautogui.easeInElastic)


def get_mouse_position():
    time.sleep(5)
    print('开始获取鼠标位置')
    try:
        for i in range(10):
            x, y = pyautogui.position()
            position_str = '鼠标坐标点（x，y）为{},{}'.format(str(x).rjust(4), str(y).rjust(4))
            # 获取鼠标所在屏幕点的RGB颜色
            pix = pyautogui.screenshot().getpixel((x, y))
            position_str += ' RGB:(' + str(pix[0]).rjust(3) + ',' + str(pix[1]).rjust(3) + ',' + str(pix[2]).rjust(
                3) + ')'
            print(position_str)
            time.sleep(1)
    except:
        print('获取鼠标位置失败')


def get_wechat_position():
    wechat_info = pyautogui.locateOnScreen('wechat.png', confidence=0.5)
    print(wechat_info)
    _location = pyautogui.center(wechat_info)
    print('该图标在屏幕中的位置是：X={},Y={}, 宽{}，高{}像素'.format(wechat_info.left, wechat_info.top, wechat_info.width, wechat_info.height))
    pyautogui.click(_location)


if __name__ == "__main__":
    get_wechat_position()


