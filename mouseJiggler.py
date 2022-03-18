import pyautogui, time, math
from pynput import keyboard

go = True

def on_press(key):
    if key == keyboard.Key.esc:
        print("yes")
    circleSpin()


def on_release(key):
    global go
    if key == keyboard.Key.esc:
        go = False
        return False

def ltor():
    startTime = time.time()
    newTime = time.time()
    dir = 'l'
    run = True
    while run:
        newTime = time.time()
        if dir == 'l':
            if (newTime - startTime) > 5:
                print("works")
                pyautogui.dragRel(200, 0, 1)
                print("works")
                startTime = time.time()
                dir = 'r'
        else:
            if (newTime - startTime) > 5:
                pyautogui.dragRel(-200, 0, 1)
                startTime = time.time()
                dir = 'l'

def circleSpin():
    rad = 50
    X, Y = pyautogui.size()
    x, y = pyautogui.position(X/2, Y/2)
    pyautogui.moveTo(x+rad, y)
    yes = 0
    while (yes < 360):
        if yes % 6 == 0:
            pyautogui.moveTo(x + rad * math.cos(math.radians(yes)), y + rad * math.sin(math.radians(yes)))
        yes+=1



with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



