import pyautogui, webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone=+573216692365')
sleep(5)

for i in range(4):
    pyautogui.typewrite('Prueba envio de mensaje')
    pyautogui.press('enter')


