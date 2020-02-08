import os
import time
from win10toast import ToastNotifier

dir_path = "C:/Users/{}/Break-Time-Notification".format(os.getlogin())

with open(dir_path + "/minute.txt") as file: 
    minute = file.read()
            
    
minute = float(minute)
i = 1

while True:
    time.sleep(minute * 60)    

    toaster = ToastNotifier()
    toaster.show_toast(title = "BREAK TIME", 
                       msg = "You've been working for {} minutes!!".format(minute * i), 
                       icon_path = dir_path + '/break.ico', duration = 5)

    i += 1
