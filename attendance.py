import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

# project module
import show_attendance
import takeImage
import trainImage
import automaticAttedance

# engine = pyttsx3.init()
# engine.say("Welcome!")
# engine.say("Please browse through your options..")
# engine.runAndWait()


def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()


haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "E:/Attendance-Management-system-using-face-recognition-master/TrainingImageLabel/Trainner.yml"
)
trainimage_path = "E:/Attendance-Management-system-using-face-recognition-master/TrainingImage"
if not os.path.exists(trainimage_path):
    os.makedirs(trainimage_path)

studentdetail_path = (
    "E:/Attendance-Management-system-using-face-recognition-master/StudentDetails/studentdetails.csv"
)
attendance_path = "Attendance"

window = Tk()
window.title("Face Recognizer")
window.geometry("1280x720")
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
window.configure(background="#DDD0C8")  # Beige theme


# to destroy screen
def del_sc1():
    sc1.destroy()


# error message for name and no
def err_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.iconbitmap("AMS.ico")
    sc1.title("Warning!!")
    sc1.configure(background="#DDD0C8")
    sc1.resizable(0, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="#323232",
        bg="#DDD0C8",  # Beige background for the error window
        font=("Allura", 16, "bold"),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="#323232",
        bg="#DBD96D",  # lighter button color
        width=9,
        height=1,
        activebackground="red",
        font=("Allura", 16, "bold"),
    ).place(x=110, y=50)

def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True


logo = Image.open("UI_Image/0001.png")
logo = logo.resize((50, 45), Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="#DDD0C8", relief=RIDGE, bd=10, font=("Allura", 30, "bold"))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1, bg="#DDD0C8",)
l1.place(x=470, y=10)


titl = tk.Label(
    window, text="FaceSense", bg="#DDD0C8", fg="#323232", font=("Avenir", 27, "bold"),
)
titl.place(x=525, y=10)

a = tk.Label(
    window,
    text="Welcome to FaceSense!",
    bg="#DDD0C8",  # Beige background for the main text
    fg="#323232",  # Bright yellow text color
    bd=10,
    font=("Allura", 35),
)
a.pack()


ri = Image.open("UI_Image/register.png")
ri = ri.resize((200, 200), Image.LANCZOS)
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=100, y=270)

ai = Image.open("UI_Image/attendance.png")
ai = ai.resize((200, 200), Image.LANCZOS)
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=980, y=270)

vi = Image.open("UI_Image/verifyy.png")
vi = vi.resize((200, 200), Image.LANCZOS)
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=600, y=270)


def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Take Student Image")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="#DDD0C8")  # Dark background for the image window
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="#DDD0C8", relief=RIDGE, bd=10, font=("Allura", 30, "bold"))
    titl.pack(fill=X)
    # image and title
    titl = tk.Label(
        ImageUI, text="Register Your Face", bg="#DDD0C8", fg="green", font=("Allura", 30, "bold"),
    )
    titl.place(x=270, y=12)

    # heading
    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="#DDD0C8",  # Beige background for the details label
        fg="#323232",  # Bright yellow text color
        bd=10,
        font=("Allura", 24, "bold"),
    )
    a.place(x=280, y=75)

    # ER no
    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=10,
        height=2,
        bg="#DDD0C8",
        fg="#323232",
        bd=5,
        relief=RIDGE,
        font=("Allura", 14),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="#E09B6F",  # Dark input background
        fg="#323232",  # Bright text color for input
        relief=RIDGE,
        font=("Allura", 18, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # name
    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="#DDD0C8",
        fg="#323232",
        bd=5,
        relief=RIDGE,
        font=("Allura", 14),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="#E29F64",  # Dark input background
        fg="#323232",  # Bright text color for input
        relief=RIDGE,
        font=("Allura", 18, "bold"),
    )
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="#DDD0C8",
        fg="#323232",
        bd=5,
        relief=RIDGE,
        font=("Allura", 14),
    )
    lbl3.place(x=120, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="#ECA56E",  # Dark background for messages
        fg="#323232",  # Bright text color for messages
        relief=RIDGE,
        font=("Allura", 14, "bold"),
    )
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        takeImage.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    # take Image button
    # image
    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=10,
        font=("Allura", 18, "bold"),
        bg="#EEAB58",  # Dark background for the button
        fg="#323232",  # Bright text color for the button
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

    def train_image():
        trainImage.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    # train Image function call
    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("Allura", 18, "bold"),
        bg="#EEAA56",  # Dark background for the button
        fg="#323232",  # Bright text color for the button
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=350)


r = tk.Button(
    window,
    text="Register a new student",
    command=TakeImageUI,
    bd=10,
    font=("Allura", 14),
    bg="#DDD0C8",
    fg="#323232",
    height=2,
    width=17,
)
r.place(x=100, y=520)


def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)


r = tk.Button(
    window,
    text="Take Attendance",
    command=automatic_attedance,
    bd=10,
    font=("Allura", 16),
    bg="#DDD0C8",
    fg="#323232",
    height=2,
    width=17,
)
r.place(x=600, y=520)


def view_attendance():
    show_attendance.subjectchoose(text_to_speech)


r = tk.Button(
    window,
    text="View Attendance",
    command=view_attendance,
    bd=10,
    font=("Allura", 16),
    bg="#DDD0C8",
    fg="#323232",
    height=2,
    width=17,
)
r.place(x=1000, y=520)
r = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=quit,
    font=("Allura", 16),
    bg="#DDD0C8",
    fg="#323232",
    height=2,
    width=17,
)
r.place(x=600, y=660)


window.mainloop()
