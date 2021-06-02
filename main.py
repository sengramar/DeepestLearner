from tkinter import *
from PIL import Image, ImageTk
from tkmacosx import Button

window = Tk()

app_width = 800
app_height = 550

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (app_width/2))
y = int((screen_height/2) - (app_height/2))

window.geometry(f'{app_width}x{app_height}+{x}+{y}')
window.title("Marine Garbage Classifier")
window.configure(bg='light sea green')

img = Image.open("/Users/jiwonyou/Desktop/DL_CNN/A3/Clone/DeepestLearner/image1.jpg")
resized = img.resize((520, 350))
pic = ImageTk.PhotoImage(resized)
lab = Label(image=pic)
lab.pack(anchor=CENTER,pady=20)
bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)
bottomFrame.configure(bg='light sea green')

def exit1():
    exit()


def next_page():
    window.destroy()
    import page_picture


label1 = Label(window, text="Welcome to Marine Garbage Classifier", fg="light sea green", bg="ghost white",borderwidth=0,
               relief = "solid", font=("arial", 25, "bold")).pack()
label2 = Label(window, text="BY DEEPEST LEARNERS", fg="light sea green", bg="ghost white",borderwidth=0,
               relief = "solid", font=("arial", 10, "italic")).pack(pady=5)

button_start = Button(bottomFrame, text="START", fg='white', bg='dark green', relief=RIDGE,
                      font=("arial", 12, "bold"), command=next_page,height = 30, width = 100) #relief args: RIDGE, GROOVE, SUKEN, RAISED
button_start.grid(column=1, row = 0, padx=30,pady=30)

button_quit = Button(bottomFrame, text="QUIT", fg='white', bg='maroon', relief=RIDGE,
                     font=("arial", 12, "bold"), command=exit1,height = 30, width = 100)
button_quit.grid(column=2, row = 0, padx=30,pady=30)
window.mainloop()