from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart Attendance System")

        # img1
        img=Image.open(r"images\img13.jpg")
        img=img.resize((600,100),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=600,height=100)

        #img2
        img1=Image.open(r"images\img4.jpeg")
        img1=img1.resize((600,100),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=600,y=0,width=600,height=200)

        #background img
        #background img
        img3=Image.open(r"images\img9.jpg")
        img3=img3.resize((1300,700),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="brown")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)




if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()