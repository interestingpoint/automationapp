import tkinter as tk
from tkinter import *
import pyautogui
wn = tk.Tk()
from defs import *
wn.title("automations")
wn.geometry("450x150")
bigol = tk.Button(text="autoclicker", bg="red", activebackground="blue", command=autoclicker, height= 2, width = 9)
bigol.grid(row=0, column=0)
biggy = tk.Button(text="mouseholder", bg="blue", activebackground="red", command=mouseholder, height=2, width=9)
biggy.grid(row=0, column=2)
biggo = tk.Button(text="mousemover", bg="green", activebackground="yellow", command=mousemover, height=2, width=9)
biggo.grid(row=0, column=1)
check1 = Checkbutton(text="autoclicker", variable=vars[1])
check2 = Checkbutton(text="mouseholder", variable=vars[2])
check3 = Checkbutton(text="mousemover", variable=vars[3])
check1.grid(row=2, column=0)
check2.grid(row=2, column=2)
check3.grid(row=2, column=1)
keyboard.add_hotkey("enter", lambda: enter())
wn.mainloop()
