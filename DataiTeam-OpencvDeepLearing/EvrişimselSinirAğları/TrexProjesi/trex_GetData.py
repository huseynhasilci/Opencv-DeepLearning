# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 10:41:05 2021

@author: husey
"""

#import key
import keyboard
import uuid
import time
from PIL import Image
from mss import mss
"""
http://www.trex-game.skipser.com/
"""
mon = {'top':485,'left':840,'width':350,'height':200}
sct = mss()
i = 0
def recordScreen(record_id,key):
    global i
    
    i+=1
    print("{}: {}".format(key,i))
    
    img = sct.grab(mon)
    im = Image.frombytes('RGB', img.size, img.rgb)
    im.save("./img/{}_{}_{}.png".format(key,record_id,i))


is_exit = False

def exit():
    global is_exit
    is_exit = True

keyboard.add_hotkey("esc", exit)

recrod_id = uuid.uuid4()

while True:
    if is_exit:
        break
    
    try:
        if keyboard.is_pressed(keyboard.KEY_UP):
            recordScreen(recrod_id,"up")
            time.sleep(0.1)
        elif keyboard.is_pressed(keyboard.KEY_DOWN):
            recordScreen(recrod_id,"down")
            time.sleep(0.1)
        elif keyboard.is_pressed("right"):
            recordScreen(recrod_id,"right")
            time.sleep(0.1)
    except RuntimeError:
        continue
















