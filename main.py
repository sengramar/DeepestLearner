from tkinter import *
from PIL import Image, ImageTk
window = Tk()

app_width = 800
app_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (app_width/2))
y = int((screen_height/2) - (app_height/2))

window.geometry(f'{app_width}x{app_height}+{x}+{y}')
window.title("Marine Garbage Classifier")

img = Image.open("C:/Users/hyuny/OneDrive/Desktop/42028 Deep learning and Convolutional neural network/Assignment3/GUI/image1.jpg")
resized = img.resize((520, 350))
pic = ImageTk.PhotoImage(resized)
lab = Label(image=pic)
lab.pack()


def exit1():
    exit()


def next_page():
    window.destroy()
    import page_picture


label1 = Label(window, text="Welcome to Marine Garbage Classifier", fg="blue", bg="yellow",
               relief = "solid", font=("arial", 16, "bold")).pack()

button_start = Button(window, text="START", fg='white', bg='brown', relief=RIDGE,
                      font=("arial", 12, "bold"), command=next_page) #relief args: RIDGE, GROOVE, SUKEN, RAISED
button_start.place(x=250, y=450)

button_quit = Button(window, text="QUIT", fg='white', bg='brown', relief=RIDGE,
                     font=("arial", 12, "bold"), command=exit1)
button_quit.place(x=400, y=450)
window.mainloop()