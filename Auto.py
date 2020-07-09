import keyboard
import time
import PySimpleGUI as gui

from pynput.mouse import Button, Controller as MouseController


mouse = MouseController()
gui.theme("DarkAmber")

layout = [[gui.Text("Click to Enable AutoMiner")],
          [gui.Text("                                                      ")],
          [gui.Button('Enable'), gui.Button('Disable')]]

def autoMiner():
    mouse.press(Button.right)
    mouse.press(Button.left)


def autoRelease():
    mouse.release(Button.left)
    mouse.release(Button.right)

def main():
    autoMine = False
    window = gui.Window('AutoMiner', layout)
    while True:
        event, values = window.read()

        if event == gui.WIN_CLOSED or event == 'Disable':
            break

        if event == "Enable":
            while True:
                if keyboard.is_pressed("h"):
                    autoMine = True

                if keyboard.is_pressed("esc"):
                    autoMine = False
                    autoRelease()

                if autoMine:
                    time.sleep(1)
                    autoMiner()

    window.close()

main()
