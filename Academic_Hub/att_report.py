from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class att_report_Class:
    def __init__(self, root):
        self.root = root
        self.root.title("student attendance System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Create the title label================
        Label(self.root, text="view student result ", font=("goudy old style", 20, "bold"), bg='orange', fg="#262626",
              cursor="hand2").place(x=10, y=15, width=1180, height=35)

        #=========search======
        self.var_search=StringVar()
        self.var_id=""
        lbl_search = Label(self.root, text="search by roll no", font=("goudy old style", 20, 'bold'), bg='white').place(x=280, y=100)
        txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 20, 'bold'), bg='lightyellow').place(x=520, y=100,width=150)

        self.btn_search = Button(self.root, text='Search',command=self.search, font=("goudy old style", 15, "bold"),
                                 bg="#03a9f4", fg="white", cursor="hand2").place(x=680, y=100, width=100, height=35)
        self.btn_clear = Button(self.root, text='Clear',command=self.clear, font=("goudy old style", 15, "bold"),
                                 bg="gray", fg="white", cursor="hand2").place(x=800, y=100, width=100, height=35)


       #=======result label==============
        lbl_roll=Label(self.root,text="Select Student",font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name= Label(self.root, text="Name", font=("goudy old style", 15, 'bold'), bg='white',bd=2,relief=GROOVE).place(x=300, y=230,width=150,height=50)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 15, 'bold'), bg='white',bd=2,relief=GROOVE).place(x=450, y=230,width=150,height=50)
        lbl_attended = Label(self.root, text="Class attended ", font=("goudy old style", 15, 'bold'), bg='white',bd=2,relief=GROOVE).place(x=600, y=230,width=150,height=50)
        lbl_total_cls = Label(self.root, text="Total class", font=("goudy old style", 15, 'bold'), bg='white',bd=2,relief=GROOVE).place(x=750, y=230,width=150,height=50)
        lbl_per= Label(self.root, text="Percentage", font=("goudy old style", 15, 'bold'), bg='white',bd=2,relief=GROOVE).place(x=900, y=230,width=150,height=50)

        self.roll=Label(self.root,font=("goudy old style",15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.roll.place(x=150,y=280,width=150,height=50)
        self.name= Label(self.root, font=("goudy old style", 15, 'bold'), bg='white',bd=2,relief=GROOVE)
        self.name.place(x=300, y=280,width=150,height=50)
        self.course = Label(self.root,  font=("goudy old style", 15, 'bold'), bg='white',bd=2,relief=GROOVE)
        self.course.place(x=450, y=280,width=150,height=50)
        self.attended = Label(self.root,  font=("goudy old style", 15, 'bold'), bg='white',bd=2,relief=GROOVE)
        self.attended.place(x=600, y=280,width=150,height=50)
        self.total_cls = Label(self.root, font=("goudy old style", 15, 'bold'), bg='white',bd=2,relief=GROOVE)
        self.total_cls.place(x=750, y=280,width=150,height=50)
        self.per= Label(self.root, font=("goudy old style", 15, 'bold'), bg='white',bd=2,relief=GROOVE)
        self.per.place(x=900, y=280,width=150,height=50)

        self.btn_delete = Button(self.root, text='delete',command=self.delete, font=("goudy old style", 15, "bold"),
                                bg="red", fg="white", cursor="hand2").place(x=500, y=350, width=150, height=35)

    def search(self):
        con = sqlite3.connect(database="pqr.db")
        cur = con.cursor()
        try:
            if self.var_search.get()=="":
                messagebox.showerror("Error","Roll no . should be required ",parent=self.root)
            else:
                cur.execute(f"select * from attendance where roll=?", (self.var_search.get(),))
                row = cur.fetchone()
                if row != None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.attended.config(text=row[4])
                    self.total_cls.config(text=row[5])
                    self.per.config(text=row[6])

                else:
                    messagebox.showerror("Error", "No record Found", parent=self.root)

        except EXCEPTION as ex:
               messagebox.showerror(("Error", f"Error due to {str(ex)}"))

    def clear(self):
        self.var_id=""
        self.roll.config(text="")
        self.name.config(text="")
        self.course.config(text="")
        self.attended.config(text="")
        self.total_cls.config(text="")
        self.per.config(text="")
        self.var_search.set("")

    def delete(self):
        con = sqlite3.connect(database="pqr.db")
        cur = con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","search student attendance first ",parent=self.root)
            else:
                cur.execute("select * from attendance where aid=?",(self.var_id,))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "invalid student attendance ", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from attendance where aid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Attendance deleted Successfully",parent=self.root)
                        self.clear()

        except EXCEPTION as ex:
               messagebox.showerror(("Error",f"Error due to {str(ex)}"))

if __name__ == "__main__":
    root = Tk()
    obj = att_report_Class(root)
    root.mainloop()
