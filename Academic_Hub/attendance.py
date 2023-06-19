from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class attendance_Class:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Create the title label================
        Label(self.root, text="Update attendance for student ", font=("goudy old style", 20, "bold"), bg='orange', fg="#262626",
              cursor="hand2").place(x=10, y=15, width=1180, height=35)

        #=========widgets===============
         #==========variables==========
        self.var_roll=StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_cls_attended = StringVar()##var_cls_attended var_no_of_class
        self.var_no_of_class = StringVar()
        self.roll_list = []
        self.fetch_roll()

        lbl_select=Label(self.root,text="Select Student",font=("goudy old style",15,'bold'),bg='white').place(x=50,y=100)
        lbl_name= Label(self.root, text="Name", font=("goudy old style", 15, 'bold'), bg='white').place(x=50, y=160)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, 'bold'), bg='white').place(x=50, y=220)
        lbl_class_done = Label(self.root, text="Class attended", font=("goudy old style", 15, 'bold'), bg='white').place(x=50, y=280)
        lbl_total_class = Label(self.root, text="No. of clsss", font=("goudy old style", 15, 'bold'), bg='white').place(x=50, y=340)

        self.txt_student = ttk.Combobox(self.root, textvariable = self.var_roll,values=self.roll_list,font=("goudy old style", 15, 'bold'), state='readonly',justify=CENTER)
        self.txt_student.place(x=280, y=100, width=200)
        self.txt_student.set("Select")
        self.btn_search = Button(self.root, text='Search', command=self.search,font=("goudy old style", 15, "bold"), bg="#03a9f4",fg="white", cursor="hand2").place(x=500, y=100, width=100,height=28)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, 'bold'),bg='lightyellow',state='readonly').place(x=280, y=160, width=320)
        txt_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 20, 'bold'),bg='lightyellow',state='readonly').place(x=280, y=220, width=320)
        txt_class = Entry(self.root, textvariable=self.var_cls_attended, font=("goudy old style",20, 'bold'),bg='lightyellow').place(x=280, y=280, width=320)
        txt_total_class = Entry(self.root, textvariable=self.var_no_of_class, font=("goudy old style", 20, 'bold'),bg='lightyellow').place(x=280, y=340, width=320)
        #======button========
        btn_add=Button(self.root,text='Submit',command=self.add,font=("times new roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2").place(x=300,y=420,width=120,height=35)
        btn_clear = Button(self.root, text='Clear', command=self.clear,font=("times new roman", 15), bg="lightgreen",activebackground="lightgray", cursor="hand2").place(x=450, y=420, width=120, height=35)
        btn_update = Button(self.root, text='Update', command=self.update, font=("times new roman", 15), bg="lightgreen",
                           activebackground="lightgray", cursor="hand2").place(x=150, y=420, width=120, height=35)

        #=====image============
        self.bg_img = Image.open("att.png")
        self.bg_img = self.bg_img.resize((500, 300), Image.LANCZOS)

        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=650, y=100)

        #=======================================================
    def fetch_roll(self):
        con = sqlite3.connect(database="pqr.db")
        cur = con.cursor()
        try:
            cur.execute("select roll from student")
            rows = cur.fetchall()
            if len(rows) != 0:
                for row in rows:
                    self.roll_list.append(row[0])
        except EXCEPTION as ex:
            messagebox.showerror(("Error", f"Error due to {str(ex)}"))

    def search(self):
        con = sqlite3.connect(database="pqr.db")
        cur = con.cursor()
        try:
            cur.execute(f"select name,course from student where roll=?", (self.var_roll.get(),))
            row = cur.fetchone()
            if row != None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])

            else:
                messagebox.showerror("Error", "No record Found", parent=self.root)

        except EXCEPTION as ex:
               messagebox.showerror(("Error", f"Error due to {str(ex)}"))


    def add(self):
        con = sqlite3.connect(database="pqr.db")
        cur = con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","pls first search student record ",parent=self.root)
            elif self.var_name.get()=="Select" or self.var_cls_attended.get()=="" or self.var_no_of_class.get()=="":
                messagebox.showerror("Error", "pls fill the record first ", parent=self.root)
            elif int(self.var_cls_attended.get()) > int(self.var_no_of_class.get()):
                messagebox.showerror("Error", "maximum value exceed ", parent=self.root)

            else:
                cur.execute("select * from attendance where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "attendance already present ", parent=self.root)
                else:
                    if self.var_cls_attended.get() > self.var_no_of_class.get():
                        messagebox.showerror("Error", "maximum value exceed ", parent=self.root)
                    else:
                        per = round(int(self.var_cls_attended.get()) * 100 / int(self.var_no_of_class.get()), 2)

                        cur.execute("insert into attendance (roll,name,course,class_done,total_class,per) values(?,?,?,?,?,?)",(
                            self.var_roll.get(),
                            self.var_name.get(),
                            self.var_course.get(),
                            self.var_cls_attended.get(),
                            self.var_no_of_class.get(),
                            str(per)
                        ))
                        con.commit()
                        messagebox.showinfo("Success","Attendance Added Successfully", parent=self.root)

        except EXCEPTION as ex:
               messagebox.showerror(("Error",f"Error due to {str(ex)}"))

    def update(self):
        con = sqlite3.connect(database="pqr.db")
        cur = con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","pls first search student record  ",parent=self.root)
            if self.var_name.get()=="Select" or self.var_cls_attended.get()=="" or self.var_no_of_class.get()=="":
                messagebox.showerror("Error", "pls fill the record first ", parent=self.root)
            if self.var_cls_attended.get() >self.var_no_of_class.get():
                messagebox.showerror("Error", "maximum value exceed ", parent=self.root)


            else:
                per = round(int(self.var_cls_attended.get()) * 100 / int(self.var_no_of_class.get()), 2)

                cur.execute("select * from attendance where roll=? and course=?",(self.var_roll.get(), self.var_course.get()))

                row=cur.fetchone()
                if row!=None:
                    op=messagebox.askyesno("hello", "do you want to update attendance ", parent=self.root)
                    if op == True:
                        cur.execute("update attendance set class_done = ?,total_class = ?,per = ? where roll=?",(

                            self.var_cls_attended.get(),
                            self.var_no_of_class.get(),
                            str(per),
                            self.var_roll.get()
                        ))
                        con.commit()
                        messagebox.showinfo("Success","Attendance updated Successfully", parent=self.root)
                else:
                    messagebox.showerror("Error","first add attendance",parent=self.root)
        except EXCEPTION as ex:
                   messagebox.showerror(("Error",f"Error due to {str(ex)}"))



    def clear(self):
        self.var_roll.set("select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_cls_attended.set(""),
        self.var_no_of_class.set("")

if __name__ == "__main__":
    root = Tk()
    obj = attendance_Class(root)
    root.mainloop()
