from tkinter import *
import tkinter as tk
from tkmacosx import Button
from PIL import Image, ImageTk
import cv2
import os
import numpy as np
from tensorflow import keras
from keras.models import model_from_json
from keras import optimizers
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
from tensorflow.keras.applications.densenet import preprocess_input, decode_predictions 

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("saved_model.h5")
print("Loaded model from disk")

optimizer = optimizers.SGD(lr=0.0001, momentum=0.9, nesterov=True)
loaded_model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
print('done')

window = Tk()
app_width = 1000
app_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (app_width/2))
y = int((screen_height/2) - (app_height/2))

window.geometry(f'{app_width}x{app_height}+{x}+{y}')
window.configure(bg='light sky blue')
window.title("Marine Garbage Classifier")


l_frame = tk.Frame(window, width=450, height=450, bg='white')
l_frame.place(x=30, y=40)
l_frame.propagate(0)
lmain = Label(l_frame)
lmain.pack(side=TOP)

r_frame = tk.Frame(window, width=450, height=450, bg='white')
r_frame.place(x=500, y=40)
r_frame.propagate(0)

def exit1():
    exit()


def wd_main():
    window.destroy()
    import main


def wd_upload():
    window.destroy()
    import page_upload

width, height = 400,400
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

#webcam connect 

def get_frame():
    if cap.isOpened():
        ret,frame = cap.read()
        frame = cv2.resize(frame,(350,350))
        if ret:
            return(ret,cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
        else:
            return(ret,None)
    else:
        return(ret,None)

def snapshot():
        ret, frame = get_frame()
        if ret:
            frame = cv2.resize(frame, (350, 350))
            cv2.imwrite("frame.jpeg",cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
            showtakenpic()
            
def showtakenpic():
    global img_path
    cap.release()
    lmain.destroy()
    btn_snapshot.destroy()
    lmain2 = Label(l_frame)
    shotimg = ImageTk.PhotoImage(Image.open("frame.jpeg"))
    lmain2.image= shotimg
    lmain2.configure(image=shotimg)
    lmain2.pack()
    btn_refresh = Button(l_frame,text="Retake photo",width=50,command=refresh)
    btn_refresh.pack(side=BOTTOM, expand=True, fill=X)
    btn_process = Button(l_frame,text='Predict', width=50, command=predict)
    btn_process.pack(side=BOTTOM, expand=True, fill=X)
    img_path = "/Users/hyuny/Downloads/DeepestLearner-main/DeepestLearner-main/frame.jpeg"
    
def refresh():
    window.destroy()
    exec(open("./page_picture.py").read())    
        
def predict():
    test_img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(test_img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_ppd = preprocess_input(img_batch)
    prediction = loaded_model.predict(img_ppd)
    resulttext = "Cardbaord: " + "{:.2%}".format(prediction[0][0]) + "\n" + "Glass: " + "{:.2%}".format(prediction[0][1]) + "\n" + "Metal: " + "{:.2%}".format(prediction[0][2]) + "\n" + "Paper: " + "{:.2%}".format(prediction[0][3]) + "\n" + "Plastic: " + "{:.2%}".format(prediction[0][4]) + "\n" + "Trash: " + "{:.2%}".format(prediction[0][5])
    result.configure(text=resulttext)
    
def updateframe():  
        ret, frame = get_frame()
        
        if ret:
            img = ImageTk.PhotoImage(image=Image.fromarray(frame))
            lmain.image = img
            lmain.configure(image=img)
        
        lmain.after(15,updateframe)
        
updateframe()


#Snapshot button
btn_snapshot=Button(l_frame, text="Snapshot", command=snapshot)
btn_snapshot.pack(side=BOTTOM, expand=True, fill=X)

button_pic = Button(window, text="LIVE PICTURE", fg='white', bg='light sky blue', relief=RIDGE,
                    font=('arial', 12, 'bold'))
button_pic.place(x=30, y=0)


button_upload = Button(window, text='UPLOAD FILE', fg='white', bg='light slate blue', relief=RIDGE,
                      font=('arial', 12, 'bold'), command=wd_upload)
button_upload.place(x=170, y=0)

label_result = Label(window, text="RESULT", fg="white", bg='light sky blue', relief='flat',
                     font=("arial", 16, "bold"))
label_result.place(x=675, y=0)

result = Label(r_frame,text='Take a Photo of Image before prediction',font=('arial',15,'bold'))
result.place(relx = 0.5, rely = 0.5, anchor=CENTER)

rightFrame = Frame(window)
rightFrame.pack(side=RIGHT, anchor=N)
rightFrame.configure(bg='light sky blue')

button_home = Button(rightFrame, text=u'\u2302', font=('arial', 15, 'bold'), bg='light sky blue',
                    command=wd_main,height = 25, width = 25)
button_home.grid(column=1, row = 0, padx=5,pady=5)
button_exit = Button(rightFrame, text="X", font=('arial', 14, 'bold'), bg='light sky blue',
                     command=exit1,height = 25, width = 25)
button_exit.grid(column=2, row = 0, padx=5,pady=5)

window.mainloop()