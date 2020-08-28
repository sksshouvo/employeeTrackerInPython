from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import tkinter.ttk
from tkinter import Canvas, Frame, BOTH
import pyautogui
import threading

global count
count = 0
class newClass:
        def __init__(self, inputTime):
                self.inputTime  = inputTime

        def setInterval(self, func,time):
                e = threading.Event()
                while not e.wait(time):
                        func()
        def takeScreenShot(self):
                global count
                count = count+1
                inc_numb = str(count)
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(r'C:\Users\Public\Pictures\Sample Pictures\New_'+inc_numb+'Now_.png')
                print(count)
                self.setInterval(self.takeScreenShot, self.inputTime)
                pass
