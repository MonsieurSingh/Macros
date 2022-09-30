import pyautogui
import json

f = open('./groups.json')
groups = json.load(f)


def preprocess(something):
    something = str(something)
    output = []
    for x in range(len(something)):
        output.append(something[x])
    return output


pyautogui.PAUSE = 2
pyautogui.FAILSAFE = True

pyautogui.press('ctrl')
pyautogui.hotkey('ctrl', 'left')
pyautogui.press('space')
pyautogui.scroll(1.9)

for group in groups:
    pyautogui.click(x=1448, y=985, clicks=1, interval=0.25,
                    button='left')  # click on share button
    pyautogui.click(x=1392, y=813, clicks=1, interval=0.25,
                    button='left')  # click on more options
    pyautogui.click(x=1375, y=894, clicks=1, interval=0.25,
                    button='left')  # click on share to a group
    pyautogui.click(x=600, y=433, clicks=3, interval=0.25,
                    button='left')  # click on search box
    pyautogui.typewrite(group, interval=0.25)
    pyautogui.click(x=815, y=527, clicks=1, interval=0.25,
                    button='left')  # click on first result
    pyautogui.moveTo(x=837, y=912)  # move cursor on post
    pyautogui.click(x=392, y=606, clicks=3, interval=0.25,
                    button='left')  # click on the empty space
    print(group + " - " + str(len(group)))

with pyautogui.hold('shift'):
    pyautogui.press('space')
pyautogui.hotkey('ctrl', 'right')


f.close()

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
