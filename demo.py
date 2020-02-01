import time
from win10toast import ToastNotifier


minute = 50
i = 1

while True:
    time.sleep(minute * 60)    

    toaster = ToastNotifier()
    toaster.show_toast(title = "BREAK TIME", msg = "You've been working for {} minutes!!".format(minute * i), 
                       icon_path="break.ico", duration=60)

    i += 1
