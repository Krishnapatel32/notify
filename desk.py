import csv
import random as r
import win10toast as wt

toast = wt.ToastNotifier()

ICON_PATH = "image\\social.ico"

data = open(r"dataa\dictionary.csv")
data = csv.reader(data)
#print(data)

data1 = list(data)

randomword=r.choice(data1)

listToStr = ' '.join(map(str, randomword))

toast.show_toast("Word for the Day",listToStr,ICON_PATH,duration=30)