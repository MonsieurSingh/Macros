import glob
import pyautogui
from groups import groupFunc

groups = groupFunc()

groups.sort(reverse=True)

pyautogui.PAUSE = 2
pyautogui.FAILSAFE = True
pyautogui.DARWIN_CATCH_UP_TIME

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)


# for group in groups:
#     pyautogui.typewrite(group, interval=0.25)

pyautogui.press('ctrl')
pyautogui.hotkey('ctrl', 'left')
pyautogui.press('space')
# pyautogui.scroll(1.9)


# Getting the coordinates of the all the buttons

coordArr = []

images = glob.glob('ImagesDT/*.png')
images.sort()

iteration = -1

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
            pyautogui.click(0+100, screenHeight-100)
            pyautogui.click(0+100, screenHeight-100)
            pyautogui.click(0+100, screenHeight-100)
        elif idx != 5:
            pyautogui.click(coords)

        if idx == 3:
            pyautogui.write("coords")
            with pyautogui.hold('command'):
                pyautogui.press(['backspace', 'backspace', 'backspace'])
            pyautogui.write(groups[0])
            with pyautogui.hold('command'):
                pyautogui.press(['backspace', 'backspace', 'backspace'])
            pyautogui.write(groups[1])
            with pyautogui.hold('command'):
                pyautogui.press(['backspace', 'backspace', 'backspace'])
            pyautogui.write(groups[2])
            with pyautogui.hold('command'):
                pyautogui.press(['backspace', 'backspace', 'backspace'])
        coordArr.append(coords)
        print(idx)
        iteration = idx

        def clickAll():
            x1, y1 = coordArr[0]
            x2, y2 = coordArr[1]
            x3, y3 = coordArr[2]
            x4, y4 = coordArr[3]
            x5, y5 = coordArr[4]
            x6, y6 = coordArr[5]

            for group in groups:
                pyautogui.click(x1, y1)  # click on share button
                pyautogui.click(x2, y2)  # click on more options
                pyautogui.click(x3, y3)  # click on share to a group
                pyautogui.click(x4, y4)  # click on search box
                pyautogui.write(group)
                pyautogui.click(x5, y5)  # click on first result
                pyautogui.click(x6, y6, interval=2)  # move cursor on post
                # click on the empty space
                pyautogui.click(0+100, screenHeight-100)
                # click on the empty space
                pyautogui.click(0+100, screenHeight-100)
                # click on the empty space
                pyautogui.click(0+100, screenHeight-100)
                print(group + " - " + str(len(group)))

            with pyautogui.hold('shift'):
                pyautogui.press('space')
            pyautogui.hotkey('ctrl', 'right')
except:
    if iteration == 1:
        for idx, image in enumerate(images):
            if idx == 0:
                continue
            if idx == 1:
                continue
            clickHere = list(pyautogui.locateCenterOnScreen(
                image, confidence=0.9))
            clickHereX = clickHere[0]
            clickHereY = clickHere[1]
            if idx == 4:
                clickHereY = clickHereY + 100
            coords = tuple([clickHereX, clickHereY])
            if idx == 5:
                pyautogui.tripleClick(0+10, screenHeight-10)
            elif idx != 5:
                pyautogui.click(coords)
            if idx == 3:
                pyautogui.write("coords")
            coordArr.append(coords)
            print(idx + "two")
            iteration = idx
        print('No second image found')
    elif idx == 4:
        print('Incorrect keywords')
    print('No image found')

    def clickAll():
        x1, y1 = coordArr[0]
        x2, y2 = coordArr[1]
        x3, y3 = coordArr[2]
        x4, y4 = coordArr[3]
        x5, y5 = coordArr[4]
        x6, y6 = coordArr[5]

        for group in groups:
            pyautogui.click(x1, y1)  # click on share button
            pyautogui.click(x2, y2)  # click on more options
            pyautogui.click(x3, y3)  # click on share to a group
            pyautogui.click(x4, y4)  # click on search box
            pyautogui.write(group)
            pyautogui.click(x5, y5)  # click on first result
            pyautogui.click(x6, y6, interval=2)  # move cursor on post
            # click on the empty space
            pyautogui.click(0+100, screenHeight-100)
            # click on the empty space
            pyautogui.click(0+100, screenHeight-100)
            # click on the empty space
            pyautogui.click(0+100, screenHeight-100)
            print(group + " - " + str(len(group)))

        with pyautogui.hold('shift'):
            pyautogui.press('space')
        pyautogui.hotkey('ctrl', 'right')
finally:
    print(coordArr)
    clickAll()


# --------------------------------------------------------------------------------------------------------------

# Click the coordinates of the all the buttons


# x=1448, y=985 Share
# x=1392, y=813 More Options
# x=1375, y=894 Share to a group
# x=600, y=433  Search for groups
# x=1055, y=290 Close
# x=1053, y=197 Close2
# x=392, y=606  Empty area
# x=815, y=527  First result
# x=834, y=598  Second result
# x=837, y=912  Post
# x=621, y=200
