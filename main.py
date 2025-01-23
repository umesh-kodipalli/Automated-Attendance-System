from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart Attendance System")

        # img1
        img=Image.open(r"C:\Users\saiso\OneDrive\Documents\Smart Attendance\images\img1.jpeg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=420,height=130)

        #img2
        img1=Image.open(r"C:\Users\saiso\OneDrive\Documents\Smart Attendance\images\img2.jpeg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=420,y=0,width=420,height=130)

        #img3
        img2=Image.open(r"C:\Users\saiso\OneDrive\Documents\Smart Attendance\images\img3.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=840,y=0,width=430,height=130)


        #background img
        img3=Image.open(r"C:\Users\saiso\Downloads\A_seamless_futuristic_digital_background_designed_.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="SMART ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        #student button
        img4=Image.open(r"C:\Users\saiso\OneDrive\Documents\Smart Attendance\images\img4.jpeg")
        img4=img4.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=50,width=150,height=150)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=200,width=150,height=40)

        #detect  face
        img5=Image.open(r"C:\Users\saiso\OneDrive\Documents\Smart Attendance\images\img6.jpeg")
        img5=img5.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,command=self.face_data,cursor="hand2")
        b2.place(x=300,y=50,width=150,height=150)

        b2_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=300,y=200,width=150,height=40)


        #train data
        img6=Image.open(r"C:\Users\saiso\OneDrive\Documents\Smart Attendance\images\img7.webp")
        img6=img6.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.train_data)
        b3.place(x=500,y=50,width=150,height=150)

        b3_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=500,y=200,width=150,height=40)

         #train data
        img7=Image.open(r"C:\Users\saiso\OneDrive\Documents\Smart Attendance\images\img7.webp")
        img7=img7.resize((150,150),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.open_img)
        b4.place(x=700,y=50,width=150,height=150)

        b4_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=700,y=200,width=150,height=40)


    def open_img(self):
        os.startfile("data")

        #function buttons

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)




if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

