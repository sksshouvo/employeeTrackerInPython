from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import tkinter.ttk
from tkinter import Canvas, Frame, BOTH
from tkinter import messagebox
import webbrowser

class login:
    def __init__(self):

        self.email_text = None
        self.password_text = None
        self.root = Tk()
        self.canvas = Canvas()
        self.canvas2 = Canvas()
        self.returnData = False

    def callback(self):
        webbrowser.open_new(self)
    
    def loginValidation(self):

        if self.email_text.get() == "sksshouvo2@gmail.com" and self.password_text.get() == "skspor@92":
            messagebox.showinfo("information","Success")
            self.root.destroy()
            self.returnData = True
            
        else:
            messagebox.showinfo("information","Invalid")
        pass
    
    def rightFunction(self):
        self.root.title("Login Panel")
        self.root.geometry("452x250")
        self.root.resizable(False,False)

        # a horizontal line
        
        self.canvas.create_line(0, 25, 600, 25)
        self.canvas.config(width=452)
        self.canvas.place(x = 0 , y= 20)
        
        # a vertical line
        self.canvas2.create_line(250, 0, 250, 150, dash=(4, 2))
        self.canvas2.place(x=0, y=70)

        # label intro
        intro_label = Label(self.root, text=" Log in",foreground ="grey", background="white",font=("Arial", 20))
        intro_label.config(width=452)
        intro_label.place(x = 0, y = 5)

        

        #email label and entry
        email_label = Label(self.root, text="Email: ", foreground="black",font=("Arial", 10))
        email_label.place(x = 10, y = 70)
        self.email_text = Entry(self.root, font=('Arial', 10), width=30)
        self.email_text.place(x = 10, y = 95)

        #password label and entry
        password_label = Label(self.root, text="Password: ", foreground="black",font=("Arial", 10))
        password_label.place(x = 10, y = 130)
        self.password_text = Entry(self.root, font=('Arial', 10), width=30)
        self.password_text.place(x = 10, y = 155)

        # Forget password

        forget_password = Label(self.root, text="Forget Password", foreground="blue",font=("Arial", 8), cursor="hand2")
        forget_password.place(x = 140, y = 130)
        forget_password.bind("<Button-1>", lambda e: login.callback("http://www.facebook.com"))

        #login button
        login_button = Button(self.root, text="Log In", command=self.loginValidation)
        login_button.place(x = 10, y = 190)

        # sign up dialouge

        d1 = Label(self.root, text="Don't Have An Account ?", foreground="black",font=("Arial", 10))
        d1.place(x = 270,  y = 70)

        d2 = Label(self.root, text="Sign Up", foreground="blue",font=("Arial", 10), cursor="hand2")
        d2.place(x = 270,  y = 90)
        d2.bind("<Button-1>", lambda e: login.callback("http://www.facebook.com"))
        self.root.mainloop()
        pass