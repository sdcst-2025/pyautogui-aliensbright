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
        mouseAutoclickThing()
        newtime=time.time()

"""
#def start(): #gets to the main screen
#    try:
#        pyautogui.moveTo(pyautogui.locateCenterOnScreen('assets/rungame.png'))
#        pyautogui.click(clicks=2,interval=0.5)
#        time.sleep(4)
#    except:
#        try:
#            pyautogui.moveTo(pyautogui.locateCenterOnScreen('assets/sleep.png',confidence=0.8))
#            pyautogui.click(clicks=2,interval=0.5)
#            time.sleep(1)
#        except:
#            pass
#

def sidetask1(): #goes to the shop on the bottom of the screen.

    shoplist=['damage','speed','limit','auto']
    shoplistlength=shoplist
    n=True
    while n==True:
        for i in shoplist:
            try:
                pyautogui.moveTo(pyautogui.locateCenterOnScreen(f'assets/{i}.png',confidence=0.8))
                mousething()
                time.sleep(0.5)
            except:
                shoplistlength.remove(i)
                if len(shoplistlength)==0:
                    n=False

#def sidetask3(): #Go into rebirth tab and use feathers for effects
#    pyautogui.moveTo(pyautogui.locateCenterOnScreen('assets/rebirth.png',confidence=0.9))
#    pyautogui.click(clicks=2,duration=0.5)
#    x,y= pyautogui.locateCenterOnScreen('assets/rebirthknife.png',confidence=0.9)
#    reCoords=[(x,y),(x+75,y),(x+150,y),(x+225,y),(x,y+100),(x+75,y+100),(x+150,y+100),(x+225,y+100)]
#    for i in reCoords:
#        pyautogui.moveTo(i[0],i[1],0.1)
#        pyautogui.click()
#    pyautogui.moveTo(pyautogui.locateCenterOnScreen('assets/xmarks.png',confidence=0.9))
#    pyautogui.click(2,duration=0.5)

def sidetask2(): #collects gems from the collection tab
    n=True
    while n==True:
        try:
            x,y=(pyautogui.locateCenterOnScreen('assets/collection.png', confidence=.7))
            pyautogui.moveTo(x,y-20)
            mousething()
            time.sleep(1)
        except:
            pass
        try:
            for i in range(6):
                if i==0:
                    try:
                        pyautogui.locateCenterOnScreen('assets/gems.png',region=(x,y-100,300,500),confidence=0.9)
                    except:
                        n=False
                pyautogui.moveTo(pyautogui.locateCenterOnScreen('assets/gems.png',region=(x,y-100,300,500),confidence=0.9))
                pyautogui.click(clicks=2,duration=0.2)
        except:
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('assets/book.png',confidence=0.9))
            print(pyautogui.locateCenterOnScreen('assets/book.png',confidence=0.9))
            pyautogui.click()
"""


def mouseAutoclickThing():
    for i in range(10):
        pyautogui.mouseDown()
        pyautogui.mouseUp()


#sidetask3()
def main():
    startGame()
    x,y=getmidCoords()
 #   while True:
    maintask(x,y,23)
        
    

main()