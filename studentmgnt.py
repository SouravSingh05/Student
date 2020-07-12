from tkinter import *
from tkinter import ttk  # allows to use combobox
import pymysql  # importing module for database connenction
from tkinter import messagebox


class Student:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x690+0+0")
        self.root.resizable(0, 0)
        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE, font=("algerian", 30),
                      bg="#48BF91")
        title.pack(side=TOP, fill=X)  # packing the label at top and making it occupy full space
        # ============Creating frame1==============================================================
        frame1 = Frame(self.root, bd=4, relief=RIDGE, bg="#3DED97")
        frame1.place(x=10, y=75, width=480, height=605)

        f1title = Label(frame1, text="Manage Students", font=("algerian", 25), bg="#3DED97")
        f1title.grid(row=0, columnspan=2, pady=10, padx=70)

        roll = Label(frame1, text="Roll No", font=("algerian", 15), bg="#3DED97")
        roll.grid(row=1, column=0, pady=20, sticky="e")  # sticks the component w for west
        self.sroll = StringVar()
        rolle = Entry(frame1, textvariable=self.sroll, font=("", 13))
        rolle.grid(row=1, column=1, sticky="w")

        name = Label(frame1, text="Name", font=("algerian", 15), bg="#3DED97")
        name.grid(row=2, column=0, sticky="e")  # sticks the component w for west
        self.sname = StringVar()
        namee = Entry(frame1, textvariable=self.sname, font=("", 13))
        namee.grid(row=2, column=1, sticky="w")

        email = Label(frame1, text="Email", font=("algerian", 15), bg="#3DED97")
        email.grid(row=3, column=0, pady=20, sticky="e")  # sticks the component w for west
        self.semail = StringVar()
        emaile = Entry(frame1, textvariable=self.semail, font=("", 13))
        emaile.grid(row=3, column=1, sticky="w")

        gender = Label(frame1, text="Gender", font=("algerian", 15), bg="#3DED97")
        gender.grid(row=4, column=0, sticky="e")
        self.sgender = StringVar()
        gendere = ttk.Combobox(frame1, font=("", 11), state="readonly", textvariable=self.sgender)
        # stopping the user to write in combobox
        gendere['values'] = ("Male", "Female", "Others")  # giving values to combobox
        gendere.grid(row=4, column=1, sticky="w")

        contact = Label(frame1, text="Contact", font=("algerian", 15), bg="#3DED97")
        contact.grid(row=5, column=0, pady=20, sticky="e")  # sticks the component w for west
        self.scontact = StringVar()
        contacte = Entry(frame1, textvariable=self.scontact, font=("", 13))
        contacte.grid(row=5, column=1, sticky="w")

        dob = Label(frame1, text="D.O.B", font=("algerian", 15), bg="#3DED97")
        dob.grid(row=6, column=0, sticky="e")  # sticks the component w for west
        self.sdob = StringVar()
        dobe = Entry(frame1, textvariable=self.sdob, font=("", 13))
        dobe.grid(row=6, column=1, sticky="w")

        address = Label(frame1, text="Address", font=("algerian", 15), bg="#3DED97")
        address.grid(row=7, column=0, pady=20, sticky="e")
        # Text field cannot be accessed by textvariable command
        self.addresse = Text(frame1, width=20, height=4, font=("", 13))
        self.addresse.grid(row=7, column=1, pady=20, sticky="w")  # using self to access the value
        # ============== creating frame for buttons================================================
        bframe = Frame(frame1, bg="#3DED97", bd=4, relief=GROOVE)
        bframe.place(x=2, y=470, width=470, height=100)

        add = Button(bframe, text="Add", width=10, bg="gray", font=("algerian", 10), command=self.add_student)
        add.grid(row=0, column=0, padx=13, pady=20, ipady=10, sticky="w")

        update = Button(bframe, text="Update", width=10, bg="gray", font=("algerian", 10), command=self.update)
        update.grid(row=0, column=1, padx=13, pady=20, ipady=10, sticky="w")

        delete = Button(bframe, text="Delete", width=10, bg="gray", font=("algerian", 10), command=self.delete)
        delete.grid(row=0, column=2, padx=13, pady=20, ipady=10, sticky="w")

        clear = Button(bframe, text="Clear", width=10, bg="gray", font=("algerian", 10), command=self.clear)
        clear.grid(row=0, column=3, padx=13, pady=20, ipady=10, sticky="w")
        # ============Creating frame2==============================================================
        frame2 = Frame(self.root, bd=4, relief=RIDGE, bg="#32612D")
        frame2.place(x=500, y=75, width=838, height=605)

        search = Label(frame2, text="Search By", font=("algerian", 15), bg="#32612D")
        search.grid(row=0, column=0, padx=7, pady=10, sticky="w")
        self.ssearch = StringVar()
        searche = ttk.Combobox(frame2, font=("", 11), width=12, state="readonly", textvariable=self.ssearch)
        # stopping the user to write in combobox
        searche['values'] = ("Roll No", "Name", "Contact")  # giving values to combobox
        searche.grid(row=0, column=1, padx=15, sticky="w")

        self.searchtext = StringVar()
        txtsearch = Entry(frame2, textvariable=self.searchtext, width=20, font=("", 11))
        txtsearch.grid(row=0, column=2, padx=15, sticky="w")

        searchbtn = Button(frame2, text="Search", width=10, bg="gray", font=("algerian", 10), command=self.search)
        searchbtn.grid(row=0, column=3, padx=15, sticky="w")

        showall = Button(frame2, text="Show All", width=10, bg="gray", font=("algerian", 10),
                         command=self.fetch_in_table)
        showall.grid(row=0, column=4, padx=15, sticky="w")

        clearbox = Button(frame2, text="CLear", width=10, bg="gray", font=("algerian", 10), command=self.cleaersearch)
        clearbox.grid(row=0, column=5, padx=15, sticky="w")
        # creating frame for table=================================================================
        table = Frame(frame2, bd=6, relief=GROOVE, bg="#32612D") # creating frame for table
        table.place(x=15, y=50, width=800, height=530)

        scrollx = Scrollbar(table, orient=HORIZONTAL)  # creating x axis scrollbar
        scrolly = Scrollbar(table, orient=VERTICAL)  # creating x axis scrollbar
        self.student = ttk.Treeview(table, columns=("roll", "name", "email", "gender", "contact", "dob", "address")
                               , xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        # creating table to view the details using ttk.treeview and setting scrollbar to it
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.student.xview)
        scrolly.config(command=self.student.yview)
        self.student.heading("roll", text="Roll No")  # creating headings
        self.student.heading("name", text="Name")
        self.student.heading("email", text="Email")
        self.student.heading("gender", text="Gender")
        self.student.heading("contact", text="Contact")
        self.student.heading("dob", text="D.O.B")
        self.student.heading("address", text="Address")
        self.student['show'] = 'headings' # treeview keeps the 1st column for index.
        # here we are asking to just show to headings and not the index
        self.student.column("roll", width=50)  # setting width of each column
        self.student.column("name", width=150)
        self.student.column("email", width=200)
        self.student.column("gender", width=50)
        self.student.column("contact", width=100)
        self.student.column("dob", width=100)
        self.student.column("address", width=250)
        self.student.pack(fill=BOTH, expand=1)  # displaying table in full frame
        self.student.bind("<ButtonRelease-1>", self.getval)
        self.fetch_in_table()

    def add_student(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student_management_system")
        # creating database connection
        cur = con.cursor()  # used to execute query
        cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)", (self.sroll.get(),
                                                                         self.sname.get(),
                                                                         self.semail.get(),
                                                                         self.sgender.get(),
                                                                         self.scontact.get(),
                                                                         self.sdob.get(),
                                                                         self.addresse.get('1.0', END)
                                                                         ))
        # query. getting data from text field starting from 1st line to end
        con.commit()
        self.fetch_in_table()
        self.clear()
        con.close()

    def fetch_in_table(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student_management_system")
        # creating database connection
        cur = con.cursor()  # used to execute query
        cur.execute("select * from student")
        rows = cur.fetchall()  # fetching data from database
        if len(rows)>0:
            self.student.delete(*self.student.get_children())  # deleting the children element of student table
            for row in rows:
                self.student.insert('', END, values=row)
            con.commit()
        con.close()

    def clear(self):
        self.sroll.set("")
        self.sname.set("")
        self.semail.set("")
        self.scontact.set("")
        self.sdob.set("")
        self.sgender.set("")
        self.addresse.delete('1.0', END)

    def getval(self, event):
        get_row = self.student.focus()  # getting data from focused row
        content = self.student.item(get_row)
        row = content['values']
        self.sroll.set(row[0])
        self.sname.set(row[1])
        self.semail.set(row[2])
        self.sgender.set(row[3])
        self.scontact.set(row[4])
        self.sdob.set(row[5])
        self.addresse.delete('1.0', END)
        self.addresse.insert(END, row[6])

    def update(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student_management_system")
        # creating database connection
        cur = con.cursor()  # used to execute query
        cur.execute("update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s", (
                                                                         self.sname.get(),
                                                                         self.semail.get(),
                                                                         self.sgender.get(),
                                                                         self.scontact.get(),
                                                                         self.sdob.get(),
                                                                         self.addresse.get('1.0', END),
                                                                         self.sroll.get()
                                                                         ))
        # query. getting data from text field starting from 1st line to end
        con.commit()
        self.fetch_in_table()
        self.clear()
        con.close()

    def delete(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student_management_system")
        # creating database connection
        cur = con.cursor()  # used to execute query
        cur.execute("delete from student where roll_no=%s", self.sroll.get())
        con.commit()
        self.fetch_in_table()
        self.clear()
        con.close()

    def cleaersearch(self):
        self.ssearch.set("")
        self.searchtext.set("")

    def search(self):
        str = self.ssearch.get()
        con = pymysql.connect(host="localhost", user="root", password="", database="student_management_system")
        # creating database connection
        cur = con.cursor()  # used to execute query
        if str == "Roll No":
            cur.execute("select * from student where roll_no=%s", (self.searchtext.get()))
            rows = cur.fetchall()  # fetching data from database
        if str == "Name":
            cur.execute("select * from student  where name LIKE %s", ("%"+self.searchtext.get()+"%"))
            rows = cur.fetchall()  # fetching data from database
        if str == "Contact":
            cur.execute("select * from student  where contact=%s", (self.searchtext.get()))
            rows = cur.fetchall()  # fetching data from database
        if len(rows) == 0:
            messagebox.showwarning("Warning", "No Matching Record found")
            self.student.delete(*self.student.get_children())  # deleting the children element of student table
            for row in rows:
                self.student.insert('', END, values=row)
            con.commit()
        elif len(rows) > 0:
            self.student.delete(*self.student.get_children())  # deleting the children element of student table
            for row in rows:
                self.student.insert('', END, values=row)
            con.commit()
        con.close()


root = Tk()
ob = Student(root)
root.mainloop()