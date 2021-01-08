from infi.systray import SysTrayIcon
import os


def Entrar(systray):
    os.startfile("Entrar.url")


def shut(systray):
    os.startfile("C:/Users/cuber/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Automation/Shutdowncompauto.lnk")


def say_hello(systray):
    os.startfile("C:/Users/cuber/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Automation/Automation.lnk")


menu_options = (("Open Entrar", None, Entrar), ("Shutdown Computer", None, shut), ("Run Automation", None, say_hello))
systray = SysTrayIcon("C:/Windows/WinSxS/amd64_microsoft-windows-sechealthui.appxmain_31bf3856ad364e35_10.0.19041.662_none_90d044da3ce12473/Device.theme-dark.ico", "Automation", menu_options)
systray.start()
