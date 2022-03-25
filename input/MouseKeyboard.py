from pynput import keyboard, mouse
from loguru import logger
from threading import Thread

logger.add('moyu.log')


def on_press(key):
    logger.debug(f'{key} :pushed')


def on_release(key):
    if key == keyboard.Key.esc:
        return False


def press_thread():
    with keyboard.Listener(on_press, on_release) as lsn:
        lsn.join()


def on_click(x, y, button, pressed):
    print('on_click')
    if button == mouse.Button.left:
        logger.debug('left was pressed! ')
    elif button == mouse.Button.right:
        logger.debug('right was pressed! ')
    else:
        return False


def on_move(x, y):
    print('Pointer moved to {}'.format((x, y)))


def on_scroll(x, y, dx, dy):
    print('scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))


def click_thread():
    with mouse.Listener(on_move, on_click, on_scroll) as listener:
        listener.join()


if __name__ == '__main__':
    t1 = Thread(target=press_thread())
    print('start 1')
    t2 = Thread(target=click_thread())
    print('start 2')
