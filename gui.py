import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image,ImageTk
import numpy as np

from tensorflow.keras.models import load_model
model=load_model('Age_sex_detection.keras')
top=tk.Tk()
top.geometry('800x600')
top.title('Age and gender detector')
top.configure(background='#CDCDCD')


label1=Label(top,background='#CDCDCD',font=('arial',15,'bold'))
label2=Label(top,background='#CDCDCD',font=('arial',15,'bold'))
sign_image=Label(top)

def Detect(file_path):
    global label_packed
    image=Image.open(file_path)
    image=image.resize((48,48))
    image=np.expand_dims(image,axis=0)
    image=np.array(image)
    image=np.delete(image,0,1)
    image=np.resize(image,(48,48,3))
    print(image.shape)
    sex_f=['Male','Female']
    image=np.array([image])/255
    pred=model.predict(image)
    age=int(np.round(pred[1][0]))
    sex=int(np.round(pred[0][0]))
    print('Predicted age is:'+ str(age))
    print('Predicted Gender is:'+ sex_f[sex])
    label1.configure(foreground='#011638',text=age)
    label2.configure(foreground='#011638',text=sex_f[sex])

def show_detect_button(file_path):
    detect_b=Button(top,text="Detect Image",command=lambda:Detect(file_path),padx=10,pady=5)
    detect_b.configure(background='#364156',foreground='white',font=('arial',10,'bold'))
    detect_b.place(relx=0.79,rely=0.46)


def upload_image():
    try:
        filepath=filedialog.askopenfilename()
        uploaded=Image.open(filepath)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label1.configure(text='')
        label2.configure(text='')
        show_detect_button(filepath)
        
    except:
        pass
        
    
upload=Button(top,text='Upload an image',command=upload_image,padx=10,pady=5)
upload.configure(background='#364156',foreground='white',font=('arial',10,'bold'))  
upload.pack(side='bottom',pady=50)
sign_image.pack(side='bottom',expand=True) 
label1.pack(side='bottom',padx=10,expand=True)
label2.pack(side='bottom',pady=50,expand=True)
heading=Label(top,text='Age and gender Detector',pady=20,font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()