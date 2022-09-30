import pyperclip
import json
import pyautogui
import pyautogui as py

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

pyautogui.press('d')
