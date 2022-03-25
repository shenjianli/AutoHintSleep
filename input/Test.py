# -*- coding: UTF-8 -*-
import pynput.mouse
from pynput.mouse import Button, Controller
import time

# mouse = Controller()
# print(mouse.position)
# time.sleep(3)
# print('The current pointer position is {0}'.format(mouse.position))
#
# # set pointer position
# mouse.position = (277, 645)
# print('now we hove moved it to {0}'.format(mouse.position))
#
# # 鼠标移动（x,y）个距离
# mouse.move(5, -5)
# print("move after {}".format(mouse.position))
#
# mouse.press(Button.left)
# mouse.release(Button.left)
#
# # Double click
# mouse.click(Button.left, 1)
#
# # scroll two steps down
# mouse.scroll(0, 500)


def on_move(x, y):
    print('Pointer moved to {}'.format((x, y)))


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        return False


def on_scroll(x, y, dx, dy):
    print('scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))


keyboard = pynput.keyboard.Controller()


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))


def on_release(key):
    print('{0} released'.format(key))
    if key == pynput.keyboard.Key.esc:
        return False


def keyboard_listener():
    while True:
        with pynput.keyboard.Listener(on_press, on_release) as listener:
            listener.join()


def test_keyboard():
    time.sleep(3)
    # 按下空格和释放空格
    keyboard.press(pynput.keyboard.Key.space)
    keyboard.release(pynput.keyboard.Key.space)

    time.sleep(3)
    # 按下a键和释放a键
    keyboard.press('a')
    keyboard.release('a')

    time.sleep(3)
    # 按下a键和释放a键
    keyboard.press('A')
    keyboard.release('A')

    time.sleep(3)
    with keyboard.pressed(pynput.keyboard.Key.shift):
        keyboard.press('b')
        keyboard.release('b')
    time.sleep(13)
    keyboard.type('hello world')


if __name__ == '__main__':
    print('start')
    # keyboard_listener()
    # test_keyboard()
    while True:
        with  pynput.mouse.Listener(on_move, on_click, on_scroll) as listener:
            listener.join()
