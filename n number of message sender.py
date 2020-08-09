#Importing the modules requried for the program
import pyautogui
import time
#getting the input
sec=int(input("Enter the number of secinds you need to open the clipboard (5-10 is recommended) : "))
#getting the message
msg=input("Enter the message : ").strip()

n=int(input("Enter the number of time you wanna send : "))

time.sleep(sec)
#actual printing
for i in range(n):
    pyautogui.write(msg)
    pyautogui.press('enter')
    
