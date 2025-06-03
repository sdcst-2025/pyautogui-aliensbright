#!python3
import time
import pyautogui

print('Please get the game open and onto the main screen.\nWebsite: https://www.crazygames.com/game/duck-duck-clicker-ixu')
time.sleep(2) #allows user to get the game open

def startGame():
    try:
        x,y=pyautogui.locateCenterOnScreen('assets/playnow.png', confidence=.8)
        pyautogui.moveTo(x,y)
        pyautogui.leftClick()
        print('Game Started.')
    except:
        print('Play Now button not detected,\nplease ensure that the game has loaded.')
    try:
        x,y=pyautogui.locateCenterOnScreen('assets/fullscreen.png', confidence=.8)
        pyautogui.moveTo(x,y)
        pyautogui.leftClick()
        print('Game in FullScreen')
    except:
        print('Fullscreen button not detected,\nplease ensure that the game has loaded.')
    time.sleep(1)

def getmidCoords():#returns the planet coords
    try:
        time.sleep(0.5)
        x,y=pyautogui.locateCenterOnScreen('assets/clicky.png', confidence=.7)
        x+=420
        y+=450
        pyautogui.moveTo(x,y)
        return x,y
    except:
        print('Game not located,\nplease rerun program.')
        return False,False

def maintask(xcoord,ycoord,timelimit): #pressing down on the middle of the planet
    startTime=time.time()
    newtime=0
    pyautogui.moveTo(xcoord,ycoord)   
    while newtime-startTime<timelimit:
        pyautogui.leftClick()
        newtime=time.time()

def task1():
    try:
        startTime=time.time()
        newtime=0
        while newtime-startTime<10:
            x,y = pyautogui.locateCenterOnScreen('assets/task1.png',confidence=0.9)
            pyautogui.moveTo(x,y)
            for i in range(20):
                pyautogui.leftClick()
            print('hi')
            newtime=time.time()
    except:
        pass

def task2():
    try:
        while True:
            x,y = pyautogui.locateCenterOnScreen('assets/task2.png',confidence=0.8)
            pyautogui.moveTo(x,y)
            for i in range(20):
                pyautogui.leftClick()
    except:
        pass

def mouseAutoclickThing(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.mouseDown()
    pyautogui.mouseUp()

def main():
    try:
        startGame()
        x,y = getmidCoords()
        while True:
            maintask(x,y,15)
            task1()
            maintask(x,y,15)
            task2()
    except:
        pass

main()