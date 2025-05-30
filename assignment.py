#!python3
import time
import pyautogui

print('Please get the game open and onto the main screen.\nWebsite: https://www.crazygames.com/game/duck-duck-clicker-ixu')
time.sleep(2) #allows user to get the game open

def startGame():
    try:
        x,y=pyautogui.locateCenterOnScreen('assets/playnow.png', confidence=.8)
        pyautogui.moveTo(x,y)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        print('Game Started.')
    except:
        print('Play Now button not detected,\nplease ensure that the game has loaded.')
    try:
        x,y=pyautogui.locateCenterOnScreen('assets/fullscreen.png', confidence=.8)
        pyautogui.moveTo(x,y)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        print('Game in FullScreen')
    except:
        print('Fullscreen button not detected,\nplease ensure that the game has loaded.')
    time.sleep(1)

def getmidCoords():#returns the planet coords
    time.sleep(0.5)
    x,y=pyautogui.locateCenterOnScreen('assets/clicky.png', confidence=.7)
    x +=100
    y+=100
    pyautogui.moveTo(x,y)
    return x,y

def maintask(xcoord,ycoord,timelimit): #pressing down on the middle of the planet
    startTime=time.time()
    newtime=0
    while newtime-startTime<timelimit:
        pyautogui.moveTo(xcoord,ycoord)
        mouseAutoclickThing(xcoord,ycoord)
        newtime=time.time()

def mouseAutoclickThing(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
