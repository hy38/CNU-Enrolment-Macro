from PIL import Image, ImageGrab
from imagesearch import *
import pytesseract
import time
import pyperclip
import pyautogui

# imagesearch.py by drov0(https://github.com/drov0/python-imagesearch)

# #=== Variables to FIX ===#
# numCodeX (constant area), numCodeY (constant area)
# width, height
# emptyX (constant area), emptyY (constant area)
# Line 36 : click parameters
# Line 44 : parameters of imagesearcharea() -> 4th, 5th parameter
# #===========================

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# time.sleep(1)

# #=== How does this Work? ===#
# #=== FOLLOWING 6 STEPS =====#
# 1. Click the "신청" button on your page
# 2. The imagesearcharea() function will find where the randomly appearing "Macro Protection Popup"
# 3. Then we will grab the Macro Protection NUM CODE using imageGrab. This will be saved as 'capture.png'
# 4. We have to recognize the NUM CODE. We do this by using function image_to_string() in pytesseract
# 5. We copy the NUM CODE to our clip board, then paste it to the "Macro Protection Popup".
# 6. DONE!
# +) YOU MAY PUT time.sleep(aTime) between wherever you need
# +) After runnning this program, you should put CHROME the foreground process.
# +) THe developer is not responsible for any disadvantages that may result from using this program.
# #===========================#

pX = 0 # x-coordinate of the "신청" button
pY = 0 # y-coordinate of the "신청" button
def macro(pX, pY) :
    # STEP 1:
    pyautogui.click(pX, pY)

    # time.sleep(0.05)

    # STEP 2:
    accur = 1
    while True:
        #   Searching from the whole SCREEN(default : (1920, 1200)
        pos = imagesearcharea("MacroProtectionPopup.png", 0, 0, 1920, 1080, accur, None)
        if pos[0] != -1:
            print("position : ", pos[0], pos[1])
            pyautogui.moveTo(pos[0], pos[1])
            break
        else:
            print("image not found")
            accur -= 0.05
    time.sleep(0.1)

    # STEP 3:
    # numBox cord : (x1, y1) ~ (x1 + width, y1 + height)
    numCodeX = pos[0] + 80
    numCodeY = pos[1] + 70
    width = 50
    height = 20
    ImageGrab.grab(bbox=(numCodeX, numCodeY, numCodeX + width, numCodeY + height)).save("capture.png", "png")

    # STEP 4, 5:
    txt = pytesseract.image_to_string(Image.open('capture.png'))
    print(txt)
    pyperclip.copy(txt)

    # STEP 6:
    # click the empty box (Not neccessary)


    # emptyX = numCodeX + 25
    # emptyY = numCodeY + 70
    # pyautogui.click(emptyX, emptyY)
# 수강신청 리뉴얼 후 클릭 안 눌러도 알아서 커서가 위치해있음


    # PRINT THE NUM CODE !
    ## ctrl v is not allowed in new version of enrollment program
    time.sleep(1)
    pyautogui.typewrite(txt , interval=0.1)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

while True:
    macro(461, 296)