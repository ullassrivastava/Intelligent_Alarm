import datetime
import winsound
import webbrowser
import random


def Ringer():
    winsound.Beep(800, 2000)


def PlayVideo():
    with open("YT.txt") as f:
        content = f.readlines()
        random_video = random.choice(content)
        webbrowser.open(random_video)


def NewsOpen():
    webbrowser.open("http://www.cnn.com/")


def TemperatureCheck():
    webbrowser.open("https://www.google.com/search?q=temperature&oq=temper&aqs=chrome.1.69i57j0l5.1978j0j7&sourceid=chrome&ie=UTF-8")


def TakeTime():
    print ("Current time:", (datetime.datetime.now().strftime("%H:%M")))
    print ("Set Alarm time")
    print("Use this form.\nExample: 06:30")
    Alarm_Time = input("Type here: ")
    print (Alarm_Time)

    Ghanti = False

    while Ghanti == False:
        Current_Time = datetime.datetime.now().strftime("%H:%M")
        print(Current_Time)
        print(Alarm_Time)
        if (Alarm_Time == Current_Time):
            Ghanti = True
            Ringer()
            PlayVideo()
            TemperatureCheck()
            NewsOpen()

TakeTime()
