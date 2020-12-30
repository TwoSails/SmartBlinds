import os
from gpiozero import Button

def shutdown():
    try:
        os.system("sudo shutdown -h now")
    except:
        pass
