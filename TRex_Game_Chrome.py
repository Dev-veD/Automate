import pyautogui as pg
import time as tm
from PIL import ImageGrab,ImageOps
from numpy import *
ax=(190,256 ,325,289 )
while(1):
    x=ImageGrab.grab(ax)
    x=ImageOps.grayscale(x)
    a=array(x)
    print(a.sum())
    if(a.sum()!=1136025):
        pg.keyDown('space')
        tm.sleep(0.01)
        pg.keyUp('space')



