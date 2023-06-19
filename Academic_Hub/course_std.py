from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class Course_Class:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Create the title label
        Label(self.root, text="Available Courses", font=("goudy old style", 20, "bold"), bg='#033054', fg="white",
              cursor="hand2").place(x=10, y=15, width=1180, height=35)

        #=======varables=======
        self.var_roll=StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()
        self.var_amount = StringVar()

        #====Widgets======
        lbl_courseName=Label(self.root,text="Course Name",font=("goudy old style",15,'bold'),bg='white').place(x=10,y=60)
        lbl_duration = Label(self.root, text="Duration", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=100)
        lbl_charges = Label(self.root, text="Charges", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=140)
        lbl_description = Label(self.root, text="Description", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=180)

        # ======Entry fields==========
        self.txt_roll = Entry(self.root,textvariable =self.var_roll, font=("goudy old style", 15, 'bold'), bg='lightyellow',state='readonly')
        self.txt_roll.place(x=150,y=60,width=200)
        txt_duration = Entry(self.root,textvariable = self.var_duration, font=("goudy old style", 15, 'bold'), bg='lightyellow',state='readonly').place(x=150, y=100,width=200)
        txt_charges = Entry(self.root, textvariable = self.var_charges,font=("goudy old style", 15, 'bold'), bg='lightyellow',state='readonly').place(x=150, y=140, width=200)
        self.txt_description = Text(self.root, font=("goudy old style", 15, 'bold'), bg='lightyellow',state='disabled')
        self.txt_description.place(x=150, y=180, width=500, height=130)


        #=====buttons====

        self.btn_clear=Button(self.root,text='Clear',font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=370,y=400,width=200,height=40)

        self.btn_buy = Button(self.root, text='Buy now', font=("goudy old style", 15, "bold"), bg="#f44336", fg="white",cursor="hand2", command=self.open_payment_gateway)
        self.btn_buy.place(x=150, y=400, width=200, height=40)


        #==========Search panel =========

        self.var_search=StringVar()
        lbl_search_courseName = Label(self.root, text="Course Name", font=("goudy old style", 15, 'bold'), bg='white').place(
            x=720, y=60)
        txt_search_courseName = Entry(self.root,textvariable =self.var_search, font=("goudy old style", 15, 'bold'), bg='lightyellow').place(x=870,y=60,width=180)

        self.btn_search=Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=self.search).place(x=1070,y=60,width=120,height=28)

        #======content==============
        self.C_frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_frame.place(x=720,y=100,width=470,height=340)

        scrolly=Scrollbar(self.C_frame,orient=VERTICAL)
        scrollx = Scrollbar(self.C_frame, orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        self.CourseTable=ttk.Treeview(self.C_frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrolly.config(command=self.CourseTable.yview)
        scrollx.config(command=self.CourseTable.xview)



        self.CourseTable.heading("cid",text="Course ID")
        self.CourseTable.heading("name",text="Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("charges",text="Charges")
        self.CourseTable.heading("description",text="Description")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("cid",width=100)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("charges",width=100)
        self.CourseTable.column("description",width=150)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        #============================================
    def clear(self):
        self.show()
        self.var_roll.set("")
        self.var_duration.set("")
        self.var_search.set("")
        self.var_charges.set("")
        self.txt_description.config(state='normal')
        self.txt_description.delete('1.0',END)
        self.txt_description.config(state='disabled')


    def get_data(self, ev):
        self.txt_roll.config(state='readonly')
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]

        if len(row) >= 5:  # Check if row has at least 5 elements
            self.var_roll.set(row[1])
            self.var_duration.set(row[2])
            self.var_charges.set(row[3])
            self.txt_description.config(state='normal')
            self.txt_description.delete('1.0', END)
            self.txt_description.insert(END, row[4])
            self.txt_description.config(state='disabled')

        else:
            pass
            #messagebox.showerror("Error", "Incomplete data row",parent=self.root)
    # Handle the case when the row doesn't have enough elements
    # You can display an error message or take appropriate action

    def show(self):
        con = sqlite3.connect(database="pqr.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("",END,values=row)

        except EXCEPTION as ex:
               messagebox.showerror(("Error",f"Error due to {str(ex)}"))
    def search(self):
        con = sqlite3.connect(database="pqr.db")
        cur = con.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%' ")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert("",END,values=row)

        except EXCEPTION as ex:
               messagebox.showerror(("Error",f"Error due to {str(ex)}"))

    def open_payment_gateway(self):
        if self.var_charges.get()=="":
            messagebox.showinfo("hello","first select a  course first",parent=self.root)

        else:
            self.payment_window = Toplevel()

            # Payment gateway window configuration
            self.payment_window.title("Payment Gateway")
            self.payment_window.geometry("350x350+495+150")
            self.payment_window.config(bg="white")
            self.payment_window.focus_force()
            self.payment_window.grab_set()

            t = Label(self.payment_window, text="Purchase course", font=("times new roman", 20, "bold"), bg="white",
                      fg="red").place(x=0, y=10, relwidth=1)
            # ___-----payment amount

            charges_value = self.var_charges.get()

            lbl_amount = Label(self.payment_window, text="Amount to pay:", font=("times new roman", 15, "bold"), bg="white",
                               fg="gray")
            lbl_amount.place(x=50, y=80)

            self.var_amount.set(charges_value)  # Set the value of self.var_amount

            txt_amount = Entry(self.payment_window, textvariable=self.var_amount, font=("goudy old style", 15, 'bold'),
                               bg='lightyellow', state='readonly')
            txt_amount.place(x=200, y=80, width=105)

            question = Label(self.payment_window, text="payment option", font=("times new roman", 15, "bold"),bg="white",fg="gray").place(x=50, y=120)

            self.cmd_quest_var = StringVar()  # Create a tkinter variable
            self.cmd_quest = ttk.Combobox(self.payment_window, textvariable=self.cmd_quest_var,
                                          font=("times new roman", 13), state='readonly', justify=CENTER)
            self.cmd_quest['values'] = (
                "Select", "UPI id", "Wallet", "net banking")
            self.cmd_quest.place(x=50, y=150, width=250)
            self.cmd_quest.current(0)

            question = Label(self.payment_window, text="give valid payment details", font=("times new roman", 15, "bold"),bg="white",fg="gray").place(x=50, y=180)
            self.txt_qs = Entry(self.payment_window, font=("times new roman", 15), bg="lightgray")
            self.txt_qs.place(x=50, y=210, width=250)


            btn_reg = Button(self.payment_window, text='Purchase', font=("times new roman", 14, "bold"), bg="#4caf50", fg="white",
                                    cursor="hand2", command=self.redirect_to_payment_page)
            btn_reg.place(x=95, y=260, width=150, height=40)

            # Validation function
            def validate_fields(*args):
                if self.cmd_quest_var.get() != "Select" and self.txt_qs.get() != "":
                    if self.cmd_quest_var.get() == "net banking":
                        messagebox.showinfo("Under Maintenance",
                                            "Please select another payment option. Net banking is under maintenance.",parent=self.payment_window)
                        self.cmd_quest_var.set("Select")  # Reset the combobox selection
                    else:
                        btn_reg.config(state='normal')  # Enable the button
                else:
                    btn_reg.config(state='disabled')  # Disable the button

            validate_fields()  # Initial validation

            # Register the validation function for changes in the combo box
            self.cmd_quest_var.trace_add('write', validate_fields)
            self.txt_qs.bind('<KeyRelease>', validate_fields)

            #btn_reg.place(x=100, y=240, width=150, height=40)
            #self.btn_reg.place(x=100, y=240), width=200, height=40)


    def redirect_to_payment_page(self):
        self.payment_window = Toplevel()

        # Payment gateway window configuration
        self.payment_window.title("Payment page")
        self.payment_window.geometry("350x350+495+150")
        self.payment_window.config(bg="white")
        self.payment_window.focus_force()
        self.payment_window.grab_set()

        t2 = Label(self.payment_window, text="404 page not found ", font=("times new roman", 20, "bold"),
                  bg="white").place(x=0, y=0)

if __name__ == "__main__":
    root = Tk()
    obj = Course_Class(root)
    root.mainloop()
