import pyautogui
import keyboard

def validate_press(key):
    return (keyboard.is_pressed('ctrl') & keyboard.is_pressed(str(key)))

def auto_clicker():
    flag = False
    if (validate_press('f7')):
        flag = True
    while (flag == True):
        pyautogui.click(clicks=5)
        if (validate_press('f8')):
            flag = False

if __name__ == '__main__':
    while (True):
        auto_clicker()