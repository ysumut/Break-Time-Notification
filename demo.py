import time
from win10toast import ToastNotifier


minute = 50
i = 1

while True:
    time.sleep(minute * 60)    

    toaster = ToastNotifier()
    toaster.show_toast(title = "MOLA VAKTİ", msg = "{} dk'dır çalışıyorsun!!".format(minute * i), 
                       icon_path="C:\\Users\\umut_\\Desktop\\mola\\break.ico", duration=60)

    i += 1
