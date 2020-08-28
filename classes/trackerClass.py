from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import tkinter.ttk
from tkinter import Canvas, Frame, BOTH
import pyautogui, sqlite3
from sqlite3 import Error

class tracker:
    def __init__(self, takeTime):
        self.root = Tk()
        self.root.title("Employee Tracker")
        self.root.geometry("452x250")
        self.root.resizable(False, False)
        self.t = StringVar()
        self.t.set("00:00:00")
        self.s = StringVar()
        self.s.set("00:00")
        self.task_details = StringVar()
        self.listbox = ""
        self.takeTime = takeTime
        self.count = 0
        self.date_label = ""
        self.conn = sqlite3.connect("test.db")
        self.cursor = None
        self.result = None
        self.start_button = None
        pass

    def add_text(self):
        self.listbox.insert(END, self.task_details.get('1.0', END))
        pass

    def reset(self):
        
        self.count=1
        self.t.set('00:00:00')
        self.s.set("00:00")

    def start(self):
        try:
            self.cursor = self.conn.execute("SELECT input_time from manual_time order by id desc limit 1")
            self.result = self.cursor.fetchone()[0]
            if self.result != self.takeTime:
                self.conn.execute("update manual_time set input_time = '"+str(self.takeTime)+"' where id = 1")
                self.conn.commit()
        except:
            self.conn.execute('''CREATE TABLE manuaL_time (id INTEGER PRIMARY KEY AUTOINCREMENT, input_time INT NOT NULL)''')
            self.conn.execute("INSERT INTO manual_time (`input_time`)VALUES('"+str(self.takeTime)+"')")
            self.conn.commit()
            self.cursor = self.conn.execute("SELECT input_time from manual_time order by id desc limit 1")
            self.result = self.cursor.fetchone()[0]
        pass
        self.count=0
        self.start_button['state'] = DISABLED
        self.start_timer()
        
    
    def start_timer(self):
        self.count
        self.timer()

    def stop_func(self):
        self.count=1
        self.start_button['state'] = NORMAL

    def timer(self):
        self.cursor = self.conn.execute("SELECT input_time from manual_time order by id desc limit 1")
        self.result = self.cursor.fetchone()[0]
        if(self.count==0):
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":"))
            h = int(h)
            m = int(m)
            s = int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s
            self.ss=h+":"+m
            
            self.t.set(self.d)
            self.s.set(self.ss)
            if(self.count==0):
               
                duration_label = Label(self.root, textvariable=self.s,foreground="grey",font=("Arial", "50"))
                duration_label.after(930, self.start_timer)
                duration_label.place(x=5, y=130)

                #calculate all seconds
                hrToSec = int(h)*(3600)
                minToSec = int(m)*(60)
                totalSec = int(hrToSec)+int(minToSec)+int(s)                
                totalTime = self.result
                print(totalSec)
                if totalSec == totalTime:
                   inc_numb = str(totalSec)
                   myScreenshot = pyautogui.screenshot()
                   myScreenshot.save(r'llx\llopyu\oop\kklkl\ppopx\lolklz\New_'+inc_numb+'Now_.png')
                   totalTime+=self.takeTime
                   self.conn.execute("update manual_time set input_time = '"+str(totalTime)+"' where id = 1")
                   self.conn.commit()
                   print('Screen Shot Taken')
               
                    
                
                    
    def trackerFunction(self):
        # root.resizable(False,False)
        label1 = Label(self.root, text="Salman Kabir" ,foreground="grey",font=("Arial", "20"))
        label1.grid(column=0, row=0, padx=5, pady=5)

        #company drop down list
        OptionList = [
        "It Corner",
        "Track Your Time"] 
        variable = tk.StringVar(self.root)
        variable.set(OptionList[0])

        opt = tk.OptionMenu(self.root, variable, *OptionList)
        opt.config(width="25",fg="grey" ,font=('Arial', "12"))
        opt.grid(column=1,row=0)

        # text entry section
        self.task_details = Text(self.root,font=('Arial', "12"), height='1', width='25', padx=0, pady=10)
        self.task_details.place(x=5, y=50)
        
        #start button 
        self.start_button = Button(self.root, text="Start", command=lambda:[self.start(), self.add_text()])
        self.start_button.place(x=260, y=53)

        #stop button 
        stop_button = Button(self.root, text="Stop", command=self.stop_func)
        stop_button.place(x=340, y=53)

        # a vertical line
        canvas = Canvas()
        canvas.create_line(200, 35, 200, 130, dash=(4, 2))
        canvas.place(x=0, y=95)

        # date
        self.date_label = Label(self.root, text="Today",foreground="grey",font=("Arial", "10"))
        self.date_label.place(x=5, y=100)

        # duration
        duration_label = Label(self.root, textvariable=self.s,foreground="grey",font=("Arial", "50"))
        duration_label.place(x=5, y=130)

        

        # item list
        self.listbox = Listbox(self.root)
        self.listbox.config(width=35, height=5)
        self.listbox.place(x=225, y=130)
        #scrollbar 
        scrollbar = Scrollbar(self.root,orient="vertical")
        scrollbar.place(x=420, y=130)
        scrollbar.config(command=self.listbox.yview)
        # listbox.insert(END, "Task List")

        # for item in ["one", "two", "three", "four","three", "four"]:
        #     listbox.insert(END, item)
        self.root.mainloop()