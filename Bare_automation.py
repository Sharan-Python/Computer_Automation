

# Please make sure you read through the comments in this file to understand the usage

from win10toast import ToastNotifier
import pyautogui
import schedule
import pygame
import time
import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = int(battery.percent)

def low_battery():
    # I made this indicate low battery, but you can put anything you like
    # win 10 toast is for showing a system notification when system battery is low
    # Add your code here
    pass

low_battery() # Make you call functions that should run all he time

def job():
    # Some other function like moving the mouse with pyautogui 
    pass


def time_up():
    notify = ToastNotifier()
    notify.show_toast("ALERT", "Its Almost Time For Class",
                      icon_path="C:/Windows/SystemApps/Microsoft.Windows.SecHealthUI_cw5n1h2txyewy/Assets/Device.contrast-white.ico",
                      duration=5)
    # I have online classes so I get a reminder for that

schedule.every().monday.at("13:48").do(job) # Line 36 - 46 can be edited as per your choice, it has simple syntax, so it should not be hard
schedule.every().tuesday.at("13:48").do(job) # Line 36 - 46 uses schedule module to run functions we defined above
schedule.every().wednesday.at("13:48").do(job) # Line 36 - 46 USE ONLY 24 HOUR TIME FORMAT, USE '0' TO FILL UP EMPTY SPACES IN THE TIME LIKE - 06:56 
schedule.every().thursday.at("13:48").do(job)
schedule.every().friday.at("13:48").do(job)

schedule.every().monday.at("13:54").do(time_up)
schedule.every().tuesday.at("13:54").do(time_up)
schedule.every().wednesday.at("13:54").do(time_up)
schedule.every().thursday.at("13:54").do(time_up)
schedule.every().friday.at("13:54").do(time_up)

while True: # Necessary code for schedule
    schedule.run_pending()
    time.sleep(1)
