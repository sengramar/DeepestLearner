from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import cv2
from tkinter import filedialog

window = Tk()
app_width = 1000
app_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (app_width/2))
y = int((screen_height/2) - (app_height/2))

window.geometry(f'{app_width}x{app_height}+{x}+{y}')
window.configure(bg='light slate blue')
window.title("Marine Garbage Classifier")


l_frame = tk.Frame(window, width=450, height=450, bg='white')
l_frame.place(x=30, y=40)

r_frame = tk.Frame(window, width=450, height=450, bg='white')
r_frame.place(x=500, y=40)


def exit1():
    exit()


def wd_main():
    window.destroy()
    import main


def wd_video():
    window.destroy()
    import page_video


def wd_picture():
    window.destroy()
    import page_picture


def open_file():
    global img
    l_frame.filename = filedialog.askopenfilename(title="upload file")
    lab = Label(l_frame, text=l_frame.filename).pack()
    img = ImageTk.PhotoImage(Image.open(l_frame.filename))
    img_lab = Label(l_frame, image=img).pack()


btn_open = Button(l_frame, text='UPLOAD FILE', command=open_file).pack()


button_pic = Button(window, text="LIVE PICTURE", fg='white', bg='light sky blue', relief=RIDGE,
                    font=('arial', 12, 'bold'), command=wd_picture)
button_pic.place(x=0, y=0)

button_video = Button(window, text='LIVE VIDEO', fg='white', bg='steel blue', relief=RIDGE,
                      font=('arial', 12, 'bold'), command=wd_video)
button_video.place(x=130, y=0)

button_upload = Button(window, text='UPLOAD FILE', fg='white', bg='light slate blue', relief='flat',
                      font=('arial', 12, 'bold'))
button_upload.place(x=238, y=0)

label_result = Label(window, text="RESULT", fg="white", bg='light slate blue', relief='flat',
                     font=("arial", 16, "bold"))
label_result.place(x=675, y=0)

button_home = Button(window, text=u'\u2302', font=('arial', 15, 'bold'), bg='light slate blue',
                    command=wd_main).place(x=960, y=0)
button_exit = Button(window, text="X", font=('arial', 14, 'bold'), bg='light slate blue',
                     command=exit1).place(x=960, y=450)


window.mainloop()