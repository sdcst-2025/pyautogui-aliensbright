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
        time.sleep(1)
    except:
        print('Play Now button not detected,\nplease ensure that the game has loaded.')
        time.sleep(1)

    try:
        x,y=pyautogui.locateCenterOnScreen('assets/fullscreen.png', confidence=.8)
        pyautogui.moveTo(x,y)
        pyautogui.leftClick()
        print('Game in FullScreen')
    except:
        print('Ad Playing\nPlease wait 15 seconds')
        time.sleep(16)
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
        for i in range(20):
            pyautogui.leftClick()
        newtime=time.time()

def task1(timelimit):
    try:
        startTime=time.time()
        newtime=0
        while newtime-startTime<timelimit:
            x,y = pyautogui.locateCenterOnScreen('assets/task1.png',confidence=0.9)
            pyautogui.moveTo(x,y)
            for i in range(20):
                pyautogui.leftClick()
            newtime=time.time()
    except:
        pass

def task2(timelimit):
    try:
        startTime=time.time()
        newtime=0
        while newtime-startTime<timelimit:
            x,y = pyautogui.locateCenterOnScreen('assets/task2.png',confidence=0.9)
            pyautogui.moveTo(x,y)
            for i in range(20):
                pyautogui.leftClick()
            newtime=time.time()
    except:
        pass

def task3(timelimit):
    try:
        startTime=time.time()
        newtime=0
        while newtime-startTime<timelimit:
            x,y = pyautogui.locateCenterOnScreen('assets/task3.png',confidence=0.8)
            pyautogui.moveTo(x,y)
            for i in range(20):
                pyautogui.leftClick()
            newtime=time.time()
    except:
        print('hi Test 112')

def task4(timelimit):
    try:
        startTime=time.time()
        newtime=0
        while newtime-startTime<timelimit:
            x,y = pyautogui.locateCenterOnScreen('assets/task4.png',confidence=0.9)
            pyautogui.moveTo(x,y)
            for i in range(20):
                pyautogui.leftClick()
            newtime=time.time()
    except:
        pass

def scrollDown():
    try:
        a,b = pyautogui.locateCenterOnScreen('assets/scrolldown.png',confidence=0.9)
        pyautogui.moveTo(a,b)
        pyautogui.dragTo(a,y=b+100,duration=1,button='left')
        return a,b
    except:
        return False,False

def scrollUp(a,b):
    try:
        pyautogui.moveTo(a,y=b+100)
        pyautogui.dragTo(a,b,duration=1,button='left')
    except:
        pass

def changeOutfit():
    pass

def main():
    try:
        startGame()
        x,y = getmidCoords()
        while True:
            tLimit=10
            for i in range(4):
                maintask(x,y,15)
                task1(tLimit)
                maintask(x,y,15)
                task2(tLimit)
                tLimit+=1
            scrollX,scrollY = scrollDown()
            for i in range(2):
                maintask(x,y,15)
                task3(tLimit)
                maintask(x,y,15)
                task4(5)
            scrollUp(scrollX,scrollY)

        
    except:
        print('Game not run\nor game exited.\nPlease rerun code with game open.')

main()