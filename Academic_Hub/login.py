from tkinter import *
from tkinter import messagebox, ttk
import PIL.Image
from PIL import Image, ImageTk, ImageDraw
from datetime import *
from math import sin, cos, radians
import time
from math import *
import sqlite3
import os
import subprocess
import random


class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title("Login system")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        # ================back ground color=================
        left_lbl = Label(self.root, bg="#08A3D2", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)
        # ====================Frames=====================

        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white",
                      fg="#08A3D2").place(x=250, y=50)

        email = Label(login_frame, text="Email address", font=("times new roman", 18, "bold"), bg="white",
                      fg="gray").place(x=250, y=150)
        self.txt_email = Entry(login_frame, font=("times new roman", 15),
                               bg="lightgray")
        self.txt_email.place(x=250, y=180, width=350, height=35)

        pass_ = Label(login_frame, text="Password", font=("times new roman", 18, "bold"), bg="white",
                      fg="gray").place(x=250, y=250)
        self.txt_email_pass_ = Entry(login_frame, font=("times new roman", 15),
                                     bg="lightgray")
        self.txt_email_pass_.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(login_frame, cursor="hand2", text="Register New Account?", command=self.register_window,
                         font=("times new roman", 14), bg="white", bd=0, fg="#B08857").place(x=250, y=320)
        btn_forget = Button(login_frame, cursor="hand2", text="Forget Password?", command=self.forget_password_window,
                            font=("times new roman", 14), bg="white", bd=0, fg="red").place(x=450, y=320)

        self.btn_login = Button(login_frame, text="login", font=("times new roman", 20, "bold"), fg="white",
                           bg="#B08857", cursor="hand2", command=self.login)
        self.btn_login.place(x=250, y=380, width=180, height=40)


        self.cmd_quest1=ttk.Combobox(login_frame,font=("times new roman",20),state='readonly',justify=CENTER)
        self.cmd_quest1['values'] = ("Select", "Admin", "Trainee")
        self.cmd_quest1.place(x=470, y=380, width=180)
        self.cmd_quest1.current(0)

        identity = Label(login_frame, text="Identity", font=("times new roman", 18, "bold"), bg="white", fg="gray")
        identity.place(x=520, y=430)

        # ====================clock=====================
        self.lbl = Label(self.root, text="\nAcademic Analog", font=("book Antiqua", 25, "bold"), fg="white", compound=BOTTOM,
                         bg='#081923', bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)
        self.working()

    def reset(self):
        self.cmd_quest.current(0)
        self.cmd_quest1.current(0)
        self.txt_new_password.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_email_pass_.delete(0, END)

    def forget_password(self):
        if self.cmd_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_new_password.get() == "":
            messagebox.showerror("Error", "All fields  are required", parent=self.root2)
        else:
            try:
                con = con = sqlite3.connect(database="pqr.db")
                cur = con.cursor()
                cur.execute("select * from employee where email_id=?  and question = ? and answer=?",
                            (self.txt_email.get(), self.cmd_quest.get(), self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "please select the correct sequrity question and answer",
                                         parent=self.root)
                else:
                    cur.execute("update employee set password=? where email_id=? ",
                                (self.txt_new_password.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success ", "your password has been reset, pls login with new password",
                                        parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to :{str(es)}", parent=self.root)

    def forget_password_trainee(self):
        if self.cmd_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_new_password.get() == "":
            messagebox.showerror("Error", "All fields  are required", parent=self.root2)
        else:
            try:
                con = con = sqlite3.connect(database="pqr.db")
                cur = con.cursor()
                cur.execute("select * from trainee where email_id=?  and question = ? and answer=?",
                            (self.txt_email.get(), self.cmd_quest.get(), self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "please select the correct security question and answer",
                                         parent=self.root)
                else:
                    cur.execute("update trainee set password=? where email_id=? ",
                                (self.txt_new_password.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success ", "your password has been reset, pls login with new password",
                                        parent=self.root2)
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to :{str(es)}", parent=self.root)



    def forget_password_window(self):
        # self.root2=Tk()
        if self.txt_email.get() == "" :
            messagebox.showerror("Error", "please enter the  email address and mark the select option  to reset your password", parent=self.root)
        elif self.cmd_quest1.get()=="Select":
            messagebox.showerror("Error","pls take a choice from select box as Admin or Trainee")

        else:
            if self.cmd_quest1.get()=="Admin":
                try:
                    con = con=sqlite3.connect(database="pqr.db")
                    cur = con.cursor()
                    cur.execute("select * from employee where email_id=? ", (self.txt_email.get(),))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "no such mail is found as Admin",
                                             parent=self.root)

                    else:
                        con.close()
                        self.root2 = Toplevel()
                        self.root2.title("Forget password")
                        self.root2.geometry("350x470+495+150")
                        self.root2.config(bg="white")
                        self.root2.focus_force()
                        self.root2.grab_set()

                        t = Label(self.root2, text="forget password", font=("times new roman", 20, "bold"), bg="white",
                                  fg="red").place(x=0, y=10, relwidth=1)
                        # -------------forget password===========
                        question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"),
                                         bg="white",
                                         fg="gray").place(x=50, y=100)

                        self.cmd_quest = ttk.Combobox(self.root2, font=("times new roman", 13), state='readonly',
                                                      justify=CENTER)
                        self.cmd_quest['values'] = (
                            "Select", "Your First pet Name", "Your Birth Place", "Your Best Friends")
                        self.cmd_quest.place(x=50, y=130, width=250)
                        self.cmd_quest.current(0)

                        answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="white",
                                       fg="gray").place(x=50, y=180)
                        self.txt_answer = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                        self.txt_answer.place(x=50, y=210, width=250)

                        new_password = Label(self.root2, text="New password", font=("times new roman", 15, "bold"),
                                             bg="white",
                                             fg="gray").place(x=50, y=260)
                        self.txt_new_password = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                        self.txt_new_password.place(x=50, y=290, width=250)

                        btn_change_password = Button(self.root2, text="Reset password", command=self.forget_password,
                                                     bg="green", fg="white",
                                                     font=("times new roman", 15, "bold")).place(x=90, y=340)
                except Exception as es:
                    messagebox.showerror("Error", f"Error due to :{str(es)}", parent=self.root)

            if self.cmd_quest1.get() == "Trainee":
                try:
                    con = con = sqlite3.connect(database="pqr.db")
                    cur = con.cursor()
                    cur.execute("select * from trainee where email_id=? ", (self.txt_email.get(),))
                    row = cur.fetchone()
                    if row == None:
                        messagebox.showerror("Error", "no such mail found as Trainee",
                                             parent=self.root)

                    else:
                        con.close()
                        self.root2 = Toplevel()
                        self.root2.title("Forget password")
                        self.root2.geometry("350x470+495+150")
                        self.root2.config(bg="white")
                        self.root2.focus_force()
                        self.root2.grab_set()

                        t = Label(self.root2, text="forget password", font=("times new roman", 20, "bold"), bg="white",
                                  fg="red").place(x=0, y=10, relwidth=1)
                        # -------------forget password===========
                        question = Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"),
                                         bg="white",
                                         fg="gray").place(x=50, y=100)

                        self.cmd_quest = ttk.Combobox(self.root2, font=("times new roman", 13), state='readonly',
                                                      justify=CENTER)
                        self.cmd_quest['values'] = (
                            "Select", "Your First pet Name", "Your Birth Place", "Your Best Friends")
                        self.cmd_quest.place(x=50, y=130, width=250)
                        self.cmd_quest.current(0)

                        answer = Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="white",
                                       fg="gray").place(x=50, y=180)
                        self.txt_answer = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                        self.txt_answer.place(x=50, y=210, width=250)

                        new_password = Label(self.root2, text="New password", font=("times new roman", 15, "bold"),
                                             bg="white",
                                             fg="gray").place(x=50, y=260)
                        self.txt_new_password = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
                        self.txt_new_password.place(x=50, y=290, width=250)

                        btn_change_password = Button(self.root2, text="Reset password", command=self.forget_password_trainee,
                                                     bg="green", fg="white",
                                                     font=("times new roman", 15, "bold")).place(x=90, y=340)
                except Exception as es:
                    messagebox.showerror("Error", f"Error due to :{str(es)}", parent=self.root)

    def register_window(self):
        self.root.destroy()
        subprocess.Popen(
            ["python",
             r"D:\admin\Academic_Hub\register.py"])

    def move_button_randomly(self):
        x = random.randint(100, 500)
        y = random.randint(100, 300)
        self.btn_login.place(x=x, y=y, width=180, height=40)

    def login(self):
        if self.txt_email.get() == "" or self.txt_email_pass_.get() == "" :
           messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.cmd_quest1.get() == "Select":
            messagebox.showerror("Error", "select your identity", parent=self.root)
        else:
            if self.cmd_quest1.get()=="Admin":
                try:
                    con = con=sqlite3.connect(database="pqr.db")
                    cur = con.cursor()
                    cur.execute("select * from employee where email_id=? and password =?",
                                (self.txt_email.get(), self.txt_email_pass_.get()))
                    row = cur.fetchone()
                    if row == None:
                        self.move_button_randomly()
                    else:
                        messagebox.showinfo("SuccessR", f"welcome:{self.txt_email.get()}", parent=self.root)
                        self.root.destroy()
                        subprocess.Popen(
                            ["python",
                             r"D:\admin\Academic_Hub\student_management.py"])
                    con.close()
                except Exception as es:
                    messagebox.showerror("Error", f"Error due to :{str(es)}", parent=self.root)
            else:
                if self.cmd_quest1.get() == "Trainee":
                    try:
                        con = con = sqlite3.connect(database="pqr.db")
                        cur = con.cursor()
                        cur.execute("select * from trainee where email_id=? and password =?",
                                    (self.txt_email.get(), self.txt_email_pass_.get()))
                        row = cur.fetchone()
                        if row == None:
                            self.move_button_randomly()
                        else:
                            messagebox.showinfo("SuccessR", f"welcome:{self.txt_email.get()}", parent=self.root)
                            self.root.destroy()
                            subprocess.Popen(
                                ["python",
                                 r"D:\admin\Academic_Hub\only_for_student.py"])

                        con.close()

                    except Exception as es:
                        messagebox.showerror("Error", f"Error due to :{str(es)}", parent=self.root)

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


    def handle_messagebox_close(self):
        # Add your desired behavior when the messagebox is closed
        root.destroy()


root = Tk()
obj = Clock(root)
root.protocol("WM_DELETE_WINDOW", obj.handle_messagebox_close)
root.mainloop()



'''
                if self.cmd_quest1.get() == "Trainee":
                    try:
                        con = con = sqlite3.connect(database="pqr.db")
                        cur = con.cursor()
                        cur.execute("select * from trainee where Email=? and password =?",
                                    (self.txt_email.get(), self.txt_email_pass_.get()))
                        row = cur.fetchone()
                        if row == None:
                            messagebox.showerror("error",  "invalid Username and password or choose the select option correctly", parent=self.root)

                        else:
                            messagebox.showinfo("SuccessR", f"welcome:{self.txt_email.get()}", parent=self.root)
                            self.root.destroy()
                            subprocess.Popen(
                                ["python",
                                 r"D:\admin\Academic_Hub\only_for_student.py"])

                        con.close()
                    except Exception as es:
                        messagebox.showerror("Error", f"Error due to :{str(es)}", parent=self.root)


'''
