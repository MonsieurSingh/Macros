from email.mime import image
import pyperclip
import json
import pyautogui
import glob

import pyautogui as py
from PIL import Image

# pyautogui.displayMousePosition()


# import time  # Import Time

# while True:  # Start loop
#     print(py.position())
#     time.sleep(1)


# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')


# def _workaround_write(text):
#     """
#     This is a work-around for the bug in pyautogui.write() with non-QWERTY keyboards
#     It copies the text to clipboard and pastes it, instead of typing it.
#     """
#     pyperclip.copy(text)
#     pyautogui.hotkey('ctrl', 'v')
#     pyperclip.copy('')


# # Test
# text_with_special_chars = '@/:;\\.ABCabc?!~^[]{}()'
# # pyautogui.write(text_with_special_chars)
# # # >>> //;\.ABCabc?§¨[]5°      -> NOK


# def preprocess(something):
#     something = str(something)
#     output = []
#     for x in range(len(something)):
#         output.append(something[x])
#         output.append(',')
#     return output


# print(preprocess(text_with_special_chars))


pyautogui.PAUSE = 2
pyautogui.FAILSAFE = True

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)

pyautogui.press('ctrl')
pyautogui.hotkey('ctrl', 'left')
pyautogui.press('space')

coordArr = []

images = glob.glob('ImagesDT/*.png')
images.sort()
print(images)

iteration = -1

try:
    for idx, image in enumerate(images):
        clickHere = list(pyautogui.locateCenterOnScreen(
            image, confidence=0.9))
        print(clickHere)
        clickHereX = clickHere[0]
        clickHereY = clickHere[1]
        if idx == 4:
            clickHereY = clickHereY + 40
        coords = tuple([clickHereX, clickHereY])
        pyautogui.click(coords)
        print(coords)
        coordArr.append(coords)
        iteration = idx
except:
    if iteration == 1:
        for idx, image in enumerate(images):
            if idx == 1:
                continue
            clickHere = list(pyautogui.locateCenterOnScreen(
                image, confidence=0.9))
            clickHereX = clickHere[0]
            clickHereY = clickHere[1]
            if idx == 4:
                clickHereY = clickHereY + 100
            coords = tuple([clickHereX, clickHereY])
            pyautogui.click(coords)
            if idx == 3:
                pyautogui.write("coords")
            coordArr.append(coords)
            iteration = idx
        print('No second image found')
    print('No image found')
finally:
    print(coordArr)


# pyautogui.moveTo(clickHereX, clickHereY, duration=0.25)

# print(clickHereX, clickHereY)
# pyautogui.click(clickHereX, clickHereY)

# for item in clickHere:
#     process_item(item)
#     x, y, width, height = item
#     print(x, y, width, height)
# print(clickHere - pyautogui.size())
# pyautogui.click(clickHere)
