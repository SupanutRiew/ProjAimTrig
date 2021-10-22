import win32gui
import numpy as np
import pyautogui
import cv2
import matplotlib.pyplot as plt
import time
import win32api
import win32con
#load model

#ans settings
config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'
model = cv2.dnn_DetectionModel(frozen_model, config_file)

model.setInputSize(320,320)
model.setInputScale(1.0/127.5)
model.setInputMean((127.5,127.5,127.5))
model.setInputSwapRB(True)

#input  1920,1080   1366 768
oldsetting = input("1.full, 2.windowed, 3.custom")
if oldsetting == "1":
    reswidth = 1920
    resheight = 1080
elif oldsetting == "2":
    reswidth = 1366
    resheight = 768
elif oldsetting == "3":
    reswidth = int(input("Width resolution: "))
    resheight = int(input("Height resolution: "))

#all guns
#gun type code from another file
#choose guns
chooseoption = input("AimBot, TriggerBot")
if chooseoption == "TriggerBot":
    #code from another file
    print("To be Done")
elif chooseoption == "AimBot":
    time.sleep(5)
    size_scale = 1

    while True:
        #Take Screenshott
        jimmy = np.array(pyautogui.screenshot(region=(0,0,reswidth,resheight)))
        jimmy = cv2.cvtColor(jimmy, cv2.COLOR_BGR2RGB)
        #Resize only for better understanding
        jimmy = cv2.resize(jimmy, (jimmy.shape[1]// size_scale, jimmy.shape[0]//size_scale))
        image = np.expand_dims(jimmy, 0)
        img_w, img_h = image.shape[2], image.shape[1]

        #detect object
        ClassIndex, confidece, bbox = model.detect(jimmy)


        #get box position
        for i, box in enumerate(bbox):
            #see class from labels file
            if ClassIndex[i] == 1 and confidece[i] >= 0.4:
                ymin, xmin, ymax, xmax = tuple(box)
                for ClassInd, conf, boxes in zip(ClassIndex, confidece, bbox):
                                #current issue: box position done
                    #left, right, top, bottom = int(xmin), int(xmin + xmax), int(ymin), int(ymin + ymax)
                    
                    #cv2.rectangle(jimmy, (int(top), int(left)), (int(bottom), int(right)), (125, 255, 51), thickness=2)
                    top, bottom, left, right = int(xmin), int(xmin + xmax), int(ymin), int(ymin + ymax)
                    
                    cv2.rectangle(jimmy, (int(left), int(top)), (int(right), int(bottom)), (125, 255, 51), thickness=2)
                    print("Detected", len(ClassIndex))
                    print(left, right, top, bottom)
                                    #192 260 326 353  middle is 341.5 192
                    midofleftright = (left+right)/2
                    midoftopbottom = (top+bottom)/2
                    print(midofleftright, midoftopbottom)
                    print(reswidth/2, resheight/2)
                    # now we have pixel position of detected object
                    
                    #next is to find the pixel differences between the crosshair and move mouse

                    pixeldiffx = int(round(midofleftright-(reswidth/2),0))
                    pixeldiffy = int(round(midoftopbottom-(resheight/2),0))
                    print(pixeldiffx, pixeldiffy)
                    #win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, pixeldiffx, pixeldiffy, 0, 0)
                    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                    #time.sleep(0.01)
                    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
        cv2.imshow("jimmy", jimmy)                       
        cv2.waitKey(1)