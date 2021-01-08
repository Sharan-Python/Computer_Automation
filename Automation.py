from win10toast import ToastNotifier
import pyautogui
import schedule
import pygame
import time
import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = int(battery.percent)

print("automated v1.0")


def low_battery():
    if percent < 20:
        notify = ToastNotifier()
        notify.show_toast("CONNECT CHARGER", "20% Charge remaining",
                          icon_path="C:/Windows/SystemApps/Microsoft.Windows.SecHealthUI_cw5n1h2txyewy/Assets/Device.contrast-white.ico",
                          duration=10)


low_battery()


def job():
    pyautogui.click(x=25, y=1048)
    time.sleep(1)
    pyautogui.click(x=701, y=430)
    time.sleep(2)
    pyautogui.getActiveWindow().maximize()
    time.sleep(20)
    pyautogui.click(x=1475, y=141)
    time.sleep(15)
    pyautogui.click(x=190, y=532)
    time.sleep(15)
    pyautogui.click(x=127, y=518)


def time_up():
    pygame.mixer.init()
    pygame.mixer.music.load("c:/windows/media/windows user account control.wav")
    pygame.mixer.music.play()
    notify = ToastNotifier()
    notify.show_toast("ALERT", "Its Almost Time For Class",
                      icon_path="C:/Windows/SystemApps/Microsoft.Windows.SecHealthUI_cw5n1h2txyewy/Assets/Device.contrast-white.ico",
                      duration=5)


schedule.every().monday.at("13:48").do(job)
schedule.every().tuesday.at("13:48").do(job)
schedule.every().wednesday.at("13:48").do(job)
schedule.every().thursday.at("13:48").do(job)
schedule.every().friday.at("13:48").do(job)

schedule.every().monday.at("13:54").do(time_up)
schedule.every().tuesday.at("13:54").do(time_up)
schedule.every().wednesday.at("13:54").do(time_up)
schedule.every().thursday.at("13:54").do(time_up)
schedule.every().friday.at("13:54").do(time_up)

while True:
    schedule.run_pending()
    time.sleep(1)
