#One key ewgf

import keyboard
import time
import pickle


with open("e:\ewgf.bin", "rb") as f:
    ewgf = pickle.load(f)


with open("e:\launcher.bin", "rb") as f:
    launcher = pickle.load(f)

def main():
    keyboard.add_hotkey("]", do_launcher)
    keyboard.add_hotkey("[", do_ewgf)
    
def do_ewgf():
    keyboard.play(ewgf, 2)

def do_launcher():
    keyboard.play(launcher, 2)


if __name__ == "__main__":
    main()
    
