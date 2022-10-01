import glob
import pyautogui

screenWidth, screenHeight = pyautogui.size()

pyautogui.PAUSE = 2
pyautogui.FAILSAFE = True

images = glob.glob('ImagesDT/*.png')

pyautogui.press('ctrl')
pyautogui.hotkey('ctrl', 'left')
pyautogui.press('space')

coordArr = []

clickHere = list(pyautogui.locateCenterOnScreen(
    './ImagesDT/Image1.png', confidence=0.9))
print(clickHere)
images.sort()
print(images)

try:
    for idx, image in enumerate(images):
        clickHere = list(pyautogui.locateCenterOnScreen(
            image, confidence=0.9))
        clickHereX = clickHere[0]
        clickHereY = clickHere[1]
        if idx == 4:
            clickHereY = clickHereY + 40
        coords = tuple([clickHereX, clickHereY])
        if idx == 5:
            pyautogui.tripleClick(0+10, screenHeight-10)
        elif idx != 5:
            pyautogui.click(coords)
        if idx == 3:
            pyautogui.write("coords")
        coordArr.append(coords)
        print(idx)
        iteration = idx
except:
    print('No image found')
