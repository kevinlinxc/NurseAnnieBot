import cv2
import numpy as np
import time
import win32com.client as comclt

cam = cv2.VideoCapture(0)
time.sleep(5)
colorArray = np.zeros((COLOR_ROWS,COLOR_COLS,3),dtype=np.uint8)
happy=[255,184,195]
bandage=[255,255,255]
fun=[93,179,115]
medicine=[107,116,131]

wsh= comclt.Dispatch("WScript.Shell")
wsh.AppActivate("Made in GameMaker Studio 2")

while True:
    time.sleep(.1)
    ret,frame = cam.read()
    #cv2.imshow('webcam', frame)
    #cv2.imshow('Color', colorArray)
    colorArray[:] = frame[305, 280, :]
    rgb = frame[305, 280, [2,1,0]]
    if np.all(rgb == happy):
	    wsh.SendKeys("q")
    if np.all(rgb == fun):
        wsh.SendKeys("e")
    if np.all(rgb == bandage):
        wsh.SendKeys("w")
    if np.all(rgb == medicine):
        wsh.SendKeys("r")
    k = cv2.waitKey(20) & 0xFF
    #cv2.imshow('Color', colorArray)
    #if k == 27:
    #    break

    #if cv2.waitKey(1)&0xFF == ord('q'):
     #   break

cam.release()
cv2.destroyAllWindows()

