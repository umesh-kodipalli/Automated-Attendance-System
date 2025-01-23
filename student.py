from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart Attendance System")

        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        #self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        #self.var_teacher=StringVar()
        self.var_std_name=StringVar()

        # img1
        img=Image.open(r"C:\Users\saiso\OneDrive\Documents\Smart Attendance\images\img12.webp")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=420,height=100)

        #img2
        img1=Image.open(r"C:\Users\saiso\OneDrive\Documents\Smart Attendance\images\img14.jpeg")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=420,y=0,width=420,height=100)

        #img3
        img2=Image.open(r"C:\Users\saiso\OneDrive\Documents\Smart Attendance\images\img13.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=840,y=0,width=430,height=100)


        #background img
        img3=Image.open(r"C:\Users\saiso\Downloads\A_seamless_futuristic_digital_background_designed_.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=100,width=1530,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="brown")
        title_lbl.place(x=0,y=0,width=1300,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1250,height=500)
        

        #left side label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("tiems new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=600,height=450)
        
        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current course Information",font=("times new roman",12,"bold"),width=10)
        current_course_frame.place(x=10,y=15,width=580,height=120)


        #department  
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)


        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CSE","ECS","ECE","EEE","MECH","CIV")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)


        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","Cse","Csm","Csd","Ece","Eee","Mech","Civ")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)


        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Course","I","II","III","IV")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)


        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Course","I","II")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"),width=10)
        class_Student_frame.place(x=10,y=150,width=580,height=270)

        #Student ID
        studentId_label=Label(class_Student_frame,text="Student ID",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.va_std_id,width=18,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #student Name
        studentName_label=Label(class_Student_frame,text="Name",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=18,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #class Division 
        #class_div_label=Label(class_Student_frame,text="Section",font=("times new roman",12,"bold"),bg="white")
        #class_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        #class_div_entry=ttk.Entry(class_Student_frame,width=20,font=("times new roman",13,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Roll NO
        roll_no_label=Label(class_Student_frame,text="Roll No",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=18,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_Student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,width=18,font=("times new roman",12,"bold"),state="readonly")
        gender_combo["values"]=("Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #gender_entry=ttk.Entry(class_Student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        #gender_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)


        #DOB
        dob_label=Label(class_Student_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=18,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Email
        email_label=Label(class_Student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=18,font=("times new roman",13,"bold"))
        email_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #Phone No
        phoneno_label=Label(class_Student_frame,text="Phone No",font=("times new roman",12,"bold"),bg="white")
        phoneno_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        phoneno_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=18,font=("times new roman",13,"bold"))
        phoneno_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #Address
        address_label=Label(class_Student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=18,font=("times new roman",13,"bold"))
        address_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=4,column=0)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio2,text="No Photo Sample",value="Yes")
        radiobtn2.grid(row=4,column=1)

        #if needed create no photo sample

        #buttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=170,width=580,height=30)

        #save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=3)

        # update_button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=3)

        #delete button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=3)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=3)

        #buttons frame
        btn1_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=0,y=210,width=580,height=30)

        #take photo button
        take_photo_btn=Button(btn1_frame,command=self.generate_dataset,text="Take Photo Sample",width=22,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0,padx=5)

        

        #update photo button
        #reset button
        update_photo_btn=Button(btn1_frame,text="Update Photo sample",width=22,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1,padx=5)



        #Right side label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("tiems new roman",12,"bold"))
        Right_frame.place(x=630,y=10,width=600,height=450)


        #search system
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"),width=10)
        search_frame.place(x=10,y=15,width=580,height=70)

        #search label
        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=10)
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        #search button
        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=5)

        #showAll button
        showAll_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=5)

        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=100,width=580,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","rollno","gender","dob","email","phNo","address","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("rollno",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phNo",text="Phone No")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phNo",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #function declaration
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sowmya@66",database="smart_attendance")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.va_std_id.get(),
                        self.var_std_name.get(),
                        #self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        #self.var_teacher.get(),
                        self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Sowmya@66",database="smart_attendance")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
            
    #get cursor 
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),  
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        #self.var_div.set(data[6]),
        self.var_roll.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        #self.var_teacher.set(data[13]),
        self.var_radio1.set(data[12])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sowmya@66",database="smart_attendance")
                    my_cursor=conn.cursor()
                    my_cursor.execute("UPDATE student SET Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll_No=%s,Gender=%s,Dob=%s,email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        #self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        #self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.va_std_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated.",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student Id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Sowmya@66",database="smart_attendance")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        #self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        #self.var_teacher.set("")
        self.var_radio1.set("")

    #generate photo sample
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Sowmya@66",database="smart_attendance")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Roll_No=%s,Gender=%s,Dob=%s,email=%s,Phone=%s,Address=%s,PhotoSample=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        #self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        #self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.va_std_id.get()==id+1
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                #=========Load predefined data on face frontals from opencv=========
                face_classifier=cv2.CascadeClassifier(r"C:\Users\saiso\OneDrive\Documents\Smart Attendance\haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbour=5 
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

                    

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
