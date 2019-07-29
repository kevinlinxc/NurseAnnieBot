import cv2
import numpy as np
import time
import win32com.client as comclt

cam = cv2.VideoCapture(0)
time.sleep(5)
ix,iy = -1, -1
COLOR_ROWS=300
COLOR_COLS=300
colorArray = np.zeros((COLOR_ROWS,COLOR_COLS,3),dtype=np.uint8)
happy=[255,184,195]
bandage=[255,255,255]
fun=[93,179,115]
medicine=[107,116,131]

wsh= comclt.Dispatch("WScript.Shell")
wsh.AppActivate("Made in GameMaker Studio 2")

def print_coords(event,x,y,flags,param):
    global ix,iy
    if 1:
        print('mouseX: ' +str(x), 'mouseY: '+str(y))
        ix,iy = x,y
        colorArray[:] = frame[305, 280, :]
        rgb = frame[305, 280, [2,1,0]]
        
        # From stackoverflow.com/questions/1855884/determine-font-color-based-on-background-color
        luminance = 1 - (0.299*rgb[0] + 0.587*rgb[1] + 0.114*rgb[2]) / 255
        if luminance < 0.5:
            textColor = [0,0,0]
        else:
            textColor = [255,255,255]

        cv2.putText(colorArray, str(rgb), (20, COLOR_ROWS - 20),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, color=textColor)
        cv2.imshow('Color', colorArray)


while True:
    time.sleep(.1)
    ret,frame = cam.read()
    cv2.imshow('webcam', frame)
    cv2.setMouseCallback('webcam',print_coords)
    cv2.imshow('Color', colorArray)
    colorArray[:] = frame[305, 280, :]
    rgb = frame[305, 280, [2,1,0]]
    if np.all(rgb == happy):
	    print('sending happy')
	    wsh.SendKeys("q")
    if np.all(rgb == fun):
        print('sending fun')
        wsh.SendKeys("e")
    if np.all(rgb == bandage):
        print('sending bandage')
        wsh.SendKeys("w")
    if np.all(rgb == medicine):
        print('sending medicine')
        wsh.SendKeys("r")
    k = cv2.waitKey(20) & 0xFF
    cv2.imshow('Color', colorArray)
    if k == 27:
        break

    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

