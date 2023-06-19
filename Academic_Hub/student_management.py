from tkinter import *
from PIL import Image, ImageTk
from course import Course_Class
from student import student_Class
from result import result_Class
from report import report_Class
from tkinter import messagebox
from att_report import  att_report_Class
from attendance import  attendance_Class
import os
from tkinter import *
from tkinter import messagebox, ttk
import PIL.Image
from PIL import Image, ImageTk, ImageDraw
from datetime import *
from math import sin, cos, radians
import time
from math import *
import sqlite3
class pqr:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Load the image file and create a PhotoImage object
        #self.logo_dash = ImageTk.PhotoImage(file="logo_p.png")

        # Create a label widget and set the image as its background image
        #logo_label = Label(self.root, image=self.logo_dash)
        #logo_label.pack()

        # Create the title label
        title = Label(self.root, text="Student Result Management System",compound=LEFT,
                      font=("goudy old style", 20, "bold"), bg='#033054', fg="white",cursor="hand2")
        title.pack(fill=X)

        #=====menu====
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1340,height=80)

        btn_course=Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg='#0b5377',fg='white',cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student = Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg='#0b5377',
                            fg='white',cursor="hand2",command=self.add_student).place(x=240, y=5, width=200, height=40)
        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg='#0b5377',
                            fg='white',cursor="hand2",command=self.add_result).place(x=460, y=5, width=200, height=40)
        btn_view = Button(M_Frame, text="View Student Results",command=self.add_report, font=("goudy old style", 15, "bold"), bg='#0b5377',
                            fg='white',cursor="hand2").place(x=680, y=5, width=210, height=40)
        btn_logout = Button(self.root, text="Logout", font=("goudy old style", 15, "bold"), bg='#0b5377',
                            fg='white',cursor="hand2",command=self.logout).place(x=922, y=40, width=200, height=40)
        btn_exit = Button(self.root, text="Exit", command=self.Exit,font=("goudy old style", 15, "bold"), bg='#0b5377',
                            fg='white',cursor="hand2").place(x=1142, y=40, width=200, height=40)

        btn_att = Button(M_Frame, text="Attendance", font=("goudy old style", 15, "bold"), bg='#0b5377',
                            fg='white', cursor="hand2", command=self.add_att).place(x=910, y=5, width=200, height=40)
        btn_chk_att = Button(M_Frame, text="Check attendance", command=self.add_att_chk, font=("goudy old style", 15, "bold"), bg='#0b5377',
                          fg='white', cursor="hand2").place(x=1130, y=5, width=200, height=40)

        #======content_window======
        self.bg_img=Image.open("bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.LANCZOS)

        self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)
        # =====update_details====
        self.lbl_course = Label(self.root, text="Total Course\n[ 0 ]", font=("goudy old style", 20), bd=10,
                                relief=RIDGE, bg='#e43b06', fg='white')
        self.lbl_course.place(x=400, y=530, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Course\n[ 0 ]", font=("goudy old style", 20), bd=10,
                                 relief=RIDGE, bg='#0676ad', fg='white')
        self.lbl_student.place(x=710, y=530, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Course\n[ 0 ]", font=("goudy old style", 20), bd=10,
                                relief=RIDGE, bg='#038074', fg='white')
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        #===========clock=================
        self.lbl = Label(self.root, text="\nTimeGauge", font=("book Antiqua", 25, "bold"), fg="white", compound=BOTTOM,
                         bg='#081923', bd=0)
        self.lbl.place(x=10, y=180, height=450, width=350)
        self.working()
        # ===footer====
        footer = Label(self.root,
                       text="Spqr-Student Result Management System\n Contanct us for any TEchnicall issue :987xxxx01",
                       font=("goudy old style", 12), bg='#262626', fg='white').pack(side=BOTTOM, fill=X)
        self.update_details()

    def update_details(self):
            con = sqlite3.connect(database="pqr.db")
            cur = con.cursor()
            try:
                cur.execute("select * from course")
                cr = cur.fetchall()
                self.lbl_course.config(text=f"Total courses\n[{str(len(cr))}]")

                cur.execute("select * from student")
                cr = cur.fetchall()
                self.lbl_student.config(text=f"Total student\n[{str(len(cr))}]")

                cur.execute("select * from result")
                cr = cur.fetchall()
                self.lbl_result.config(text=f"Total result\n[{str(len(cr))}]")


                self.lbl_course.after(200,self.update_details)

            except EXCEPTION as ex:
                messagebox.showerror(("Error", f"Error due to {str(ex)}"))

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)
        # ==== pasting the image=======

        bg = Image.open("c.png")
        bg = bg.resize((300, 300), Image.LANCZOS)
        clock.paste(bg, (50, 50))

        origin = 200, 200

        # =====Hour ine image==========
        draw.line((origin, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))), fill='#DF005E', width=4)

        # =====min ine image==========
        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill='white', width=3)
        # =====seec ine image==========
        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill='yellow', width=2)
        # ====draw center==========
        draw.ellipse((195, 195, 210, 210), fill='#1AD5D5')
        clock.save("clock_new.png")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h / 12) * 360
        min_ = (m / 60) * 360
        sec_ = (s / 60) * 360
        self.clock_image(hr, min_, sec_)
        self.image = PIL.Image.open("clock_new.png")
        self.img = ImageTk.PhotoImage(self.image)
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)


    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Course_Class(self.new_win)



    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=student_Class(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=result_Class(self.new_win)
    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=report_Class(self.new_win)
    def add_att(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=attendance_Class(self.new_win)
    def add_att_chk(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=att_report_Class(self.new_win)
    def logout(self):
        op=messagebox.askyesno("hello","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def Exit(self):
        op = messagebox.askyesno("Confrom", "Do you really want to Exit?", parent=self.root)
        if op == True:
            self.root.destroy()



if __name__ == "__main__":
    root = Tk()
    obj = pqr(root)
    root.mainloop()
