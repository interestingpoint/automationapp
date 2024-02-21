import pyautogui
import keyboard
from tkinter import *
import tkinter as tk
import time
e = Entry(font=("sans serif", 9))
e.grid(row=3, column=1)
vars = {1: BooleanVar(), 2: BooleanVar(), 3: BooleanVar()}
edic = {1: tk.StringVar()}
prev = {1:"fhdfpgioadfhogaerhoaerh", 2:"fhdfpgioadfhogaerhoaerh", 3:"fhdfpgioadfhogaerhoaerh"}
def mouseholder():
    pyautogui.mouseDown()
    while True:
        if keyboard.is_pressed("esc"):
            pyautogui.mouseUp()
            break


def autoclicker():
    while True:
        if keyboard.is_pressed("esc"):
            break
        pyautogui.click()


def aimbot():
    while True:
        if pyautogui.pixelMatchesColor(pyautogui.position()[0], pyautogui.position()[1], (96, 216, 255), tolerance=100):
            pyautogui.click()
        elif keyboard.is_pressed("ctrl+e"):
            break


def mousemover():
    while True:
        if keyboard.is_pressed("esc"):
            break
        pyautogui.moveTo(10, 10, 1)
        pyautogui.moveTo(100, 100, 1)


def enter():
    m = e.get()
    if vars[1].get() == True:
        if prev[1] == "fhdfpgioadfhogaerhoaerh":
            lmnop=1
        elif prev[1] == "":
            lmnop=1
        else:
            keyboard.remove_hotkey(prev[1])
        m = e.get()
        prev[1] = e.get()
        if m == "":
            return 0
        keyboard.add_hotkey(m, lambda: autoclicker())
    if vars[2].get() == True:
        if prev[2] == "fhdfpgioadfhogaerhoaerh":
            lmnop = 1
        elif prev[2] == "":
            lmnop = 1
        else:
            keyboard.remove_hotkey(prev[2])
        m = e.get()
        prev[2] = e.get()
        if m == "":
            return 0
        keyboard.add_hotkey(m, lambda: mouseholder())
    if vars[3].get() == True:
        if prev[3] == "fhdfpgioadfhogaerhoaerh":
            lmnop = 1
        elif prev[3] == "":
            lmnop = 1
        else:
            keyboard.remove_hotkey(prev[3])
        m = e.get()
        prev[3] = e.get()
        m=e.get()
        if m == "":
            return 0
        keyboard.add_hotkey(m, lambda: mousemover())
