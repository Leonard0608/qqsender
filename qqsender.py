import random
import time
import win32gui
import win32con
import win32clipboard as w
import datetime
class qqsender:
    def sleep_send(message,name,max_time_sleep,min_time_sleep):
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, message)
        handle = win32gui.FindWindow(None, name)
        win32gui.SendMessage(handle, 770, 0, 0)
        win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        time.sleep(random.randint(min_time_sleep,max_time_sleep))

    def clock_send(sendhour,message,name):
        if str(datetime.datetime.now().hour) == str(sendhour):
            w.OpenClipboard()
            w.EmptyClipboard()
            w.SetClipboardData(win32con.CF_UNICODETEXT, message)
            handle = win32gui.FindWindow(None, name)
            win32gui.SendMessage(handle, 770, 0, 0)
            win32gui.SendMessage(handle, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
if __name__ == '__main__':
    qqsender