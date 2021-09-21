from tkinter import*
from tkinter import ttk
from typing import Sized
import mysql.connector
from tkinter import messagebox #for showing a message after successfully adding a record in the database
import datetime #for due date and fine related stuff in book info
class lms:
    def __init__(self,root):
        self.root=root
        self.root.title("LIBRARY MANAGEMENT SYSTEM")
        self.root.geometry('1550x800+0+0')
        #-----------------------VARIABLES----------------------------------------------------------
        self.a1=StringVar()
        self.a2=StringVar()
        self.a3=StringVar()
        self.a4=StringVar()
        self.a5=StringVar()
        self.a6=StringVar()
        self.a7=StringVar()
        self.a8=StringVar()
        self.a9=StringVar()
        self.a10=StringVar()
        self.a11=StringVar()
        self.a12=StringVar()
        self.a13=StringVar()
        self.a14=StringVar()
        self.a15=StringVar()
        self.a16=StringVar()
        self.a17=StringVar()
        self.a18=StringVar()


        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=10,relief=RIDGE,font=("Times New Roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)#to display the label and determine the side on which it'll be shown

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=100,width=1510,height=500)

        #-------------------------LEFT FRAME INSIDE FRAME FOR MEMBER INFO----------------------------

        left=LabelFrame(frame,text="LIBRAY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=10,relief=RIDGE,font=("Times New Roman",10,"bold"))
        left.place(x=0,y=5,width=800,height=378)

        lbl1=Label(left,text="Member Type",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl1.grid(row=0,column=0,sticky=W)

        com1=ttk.Combobox(left,font=("Times New Roman",15,"bold"),textvariable=self.a1,width=27,state="readonly")
        com1["value"]=("Admin Staff","Student","Lecturer")
        com1.grid(row=0,column=1)

        lbl2=Label(left,text="PRN No.",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl2.grid(row=1,column=0,sticky=W)

        txt2=Entry(left,font=("Times New Roman",15,"bold"),textvariable=self.a2,width=29)
        txt2.grid(row=1,column=1)

        lbl3=Label(left,text="ID No.",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl3.grid(row=2,column=0,sticky=W)

        txt3=Entry(left,font=("Times New Roman",15,"bold"),textvariable=self.a3,width=29)
        txt3.grid(row=2,column=1)

        lbl4=Label(left,text="First Name",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl4.grid(row=3,column=0,sticky=W)

        txt4=Entry(left,font=("Times New Roman",15,"bold"),textvariable=self.a4,width=29)
        txt4.grid(row=3,column=1)

        lbl5=Label(left,text="Last Name",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl5.grid(row=4,column=0,sticky=W)

        txt5=Entry(left,font=("Times New Roman",15,"bold"),width=29,textvariable=self.a5)
        txt5.grid(row=4,column=1)

        lbl6=Label(left,text="Address 1",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl6.grid(row=5,column=0,sticky=W)

        txt6=Entry(left,font=("Times New Roman",15,"bold"),textvariable=self.a6,width=29)
        txt6.grid(row=5,column=1)

        lbl7=Label(left,text="Address 2",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl7.grid(row=6,column=0,sticky=W)

        txt7=Entry(left,font=("Times New Roman",15,"bold"),width=29,textvariable=self.a7)
        txt7.grid(row=6,column=1)

        lbl8=Label(left,text="Post Code",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl8.grid(row=7,column=0,sticky=W)

        txt8=Entry(left,font=("Times New Roman",15,"bold"),width=29,textvariable=self.a8)
        txt8.grid(row=7,column=1)

        lbl9=Label(left,text="Mobile Number",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl9.grid(row=8,column=0,sticky=W)

        txt9=Entry(left,font=("Times New Roman",15,"bold"),width=29,textvariable=self.a9)
        txt9.grid(row=8,column=1)

        lbl10=Label(left,text="Book Id",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl10.grid(row=0,column=3,sticky=W)

        txt10=Entry(left,font=("Times New Roman",15,"bold"),width=20,textvariable=self.a10)
        txt10.grid(row=0,column=4)

        lbl11=Label(left,text="Book Title",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl11.grid(row=1,column=3,sticky=W)

        txt11=Entry(left,font=("Times New Roman",15,"bold"),width=20,textvariable=self.a11)
        txt11.grid(row=1,column=4)

        lbl12=Label(left,text="Author Name",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl12.grid(row=2,column=3,sticky=W)

        txt12=Entry(left,font=("Times New Roman",15,"bold"),width=20,textvariable=self.a12)
        txt12.grid(row=2,column=4)

        lbl13=Label(left,text="Date Borrowed",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl13.grid(row=3,column=3,sticky=W)

        txt13=Entry(left,font=("Times New Roman",15,"bold"),width=20,textvariable=self.a13)
        txt13.grid(row=3,column=4)

        lbl14=Label(left,text="Date Due",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl14.grid(row=4,column=3,sticky=W)

        txt14=Entry(left,font=("Times New Roman",15,"bold"),width=20,textvariable=self.a14)
        txt14.grid(row=4,column=4)

        lbl15=Label(left,text="Days on Book",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl15.grid(row=5,column=3,sticky=W)

        txt15=Entry(left,font=("Times New Roman",15,"bold"),width=20,textvariable=self.a15)
        txt15.grid(row=5,column=4)

        lbl16=Label(left,text="Late return fine",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl16.grid(row=6,column=3,sticky=W)

        txt16=Entry(left,font=("Times New Roman",15,"bold"),width=20,textvariable=self.a16)
        txt16.grid(row=6,column=4)

        lbl17=Label(left,text="Date over due",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl17.grid(row=7,column=3,sticky=W)

        txt17=Entry(left,font=("Times New Roman",15,"bold"),width=20,textvariable=self.a17)
        txt17.grid(row=7,column=4)

        lbl18=Label(left,text="Actual Price",bg="powder blue",font=("Times New Roman",15,"bold"),padx=2,pady=6)
        lbl18.grid(row=8,column=3,sticky=W)

        txt18=Entry(left,font=("Times New Roman",15,"bold"),width=20,textvariable=self.a18)
        txt18.grid(row=8,column=4)

        
        #-------------------RIGHT FRAME INSDIDE FRAME FOR BOOK DETAILS-----------------------

        right=LabelFrame(frame,text="BOOK DETAILS",bg="powder blue",fg="green",bd=10,relief=RIDGE,font=("Times New Roman",10,"bold"))
        right.place(x=810,y=5,width=590,height=378)

        self.txtbox=Text(right,font=("Times New Roman",10,"bold"),width=32,height=22,padx=2,pady=6)
        self.txtbox.grid(row=0,column=2)

        
        sb=Scrollbar(right,)
        sb.grid(row=0,column=1,sticky="ns")

        listbook=['Head firt book','Learn python the hard way','hssh','jshbs','jsjsj','Python programming','dhbdh','xsvx','jsnjbbnxnj','secret rahshy','pyhton cookbook','into to machine learning','fluent python','machine techno','my python','advance python','red chilli python','ishq python','piiit','tycoon','gotohell','subtle art of python','amazing world']


        def SelectBook(event=""):
            index=listbox.curselection()
            value=listbox.get(index[0])
            if(value=="hssh"):
                self.a10.set("BKID678")
                self.a11.set("Python manual")
                self.a12.set("nandini")

                d1=datetime.datetime.today() #this gives todays date,ie,date of borrowing the book
                d2=datetime.timedelta(days=15) #for calculating the date on which the book is supposed to be returned after 15 days
                d3=d1+d2 #for date over due

                self.a13.set(d1)
                self.a14.set(d3)
                self.a15.set(15)
                self.a16.set("Rs. 50")
                self.a17.set("NO")
                self.a18.set("Rs 750")
            elif(value=="Head firt book"):
                self.a10.set("vgghv")
                self.a11.set("ctgcgcvg")
                self.a12.set("ccfgcg")

                d1=datetime.datetime.today() #this gives todays date,ie,date of borrowing the book
                d2=datetime.timedelta(days=15) #for calculating the date on which the book is supposed to be returned after 15 days
                d3=d1+d2 #for date over due

                self.a13.set(d1)
                self.a14.set(d3)
                self.a15.set(15)
                self.a16.set("rs 50")
                self.a17.set("no")
                self.a18.set("rs 500")



        listbox=Listbox(right,font=("Times New Roman",10,"bold"),width=20,height=22)
        listbox.bind("<<ListboxSelect>>",SelectBook) #for binding list box to the event desccribed earlier
        listbox.grid(row=0,column=0,padx=4)
        sb.config(command=listbox.yview)

        for item in listbook:
            listbox.insert(END,item)




        #--------------------FRAME FOR BUTTONS----------------------------------

        frameButton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frameButton.place(x=0,y=500,width=1510,height=60)

        btn1=Button(frameButton,text="Add Data",command=self.add_data,font=("Times New Roman",10,"bold"),width=29,bg="blue",fg="white") #command keyword is used for specifying what has to be done when the button is pressed;hence here we are passing the function which does the task of adding the data
        btn1.grid(row=0,column=0)

        btn1=Button(frameButton,text="Show data",font=("Times New Roman",10,"bold"),width=29,bg="blue",fg="white")
        btn1.grid(row=0,column=1)

        btn1=Button(frameButton,text="Update Data",font=("Times New Roman",10,"bold"),width=29,bg="blue",fg="white")
        btn1.grid(row=0,column=2)

        btn1=Button(frameButton,text="Delete Data",font=("Times New Roman",10,"bold"),width=29,bg="blue",fg="white")
        btn1.grid(row=0,column=3)

        btn1=Button(frameButton,text="Reset Data",font=("Times New Roman",10,"bold"),width=29,bg="blue",fg="white")
        btn1.grid(row=0,column=4)

        btn1=Button(frameButton,text="Exit",font=("Times New Roman",10,"bold"),width=29,bg="blue",fg="white")
        btn1.grid(row=0,column=5)

        #--------------------INFORMATION FRAME-----------------------------------

        frameInfo=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="white")
        frameInfo.place(x=0,y=550,width=1510,height=150)

        table_frame=Frame(frameInfo,bd=6,relief=RIDGE,bg="powder blue")
        table_frame.place(x=0,y=2,width=1300,height=120)

        xscroll=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(table_frame,orient=HORIZONTAL)


        self.table=ttk.Treeview(table_frame,columns=("membertype","prno","idno","frstname","lastname","adress1","adress2","postid","mobile","bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        xscroll.config(command=self.table.xview)
        yscroll.config(command=self.table.yview)

        self.table.heading("membertype",text="Member type")
        self.table.heading("prno",text="PRN No")
        self.table.heading("idno",text="ID No")
        self.table.heading("frstname",text="First Name")
        self.table.heading("lastname",text="Last name")
        self.table.heading("adress1",text="Address 1")
        self.table.heading("adress2",text="Address 2")
        self.table.heading("postid",text="Post ID")
        self.table.heading("mobile",text="Mobile")
        self.table.heading("bookid",text="Book ID")
        self.table.heading("booktitle",text="Book title")
        self.table.heading("author",text="Author")
        self.table.heading("dateborrowed",text="Date borrowed")
        self.table.heading("datedue",text="Date Due")
        self.table.heading("days",text="Days")
        self.table.heading("latereturnfine",text="Late Return Fine")
        self.table.heading("dateoverdue",text="Date Over Due")
        self.table.heading("finalprice",text="Final price")

        self.table["show"]="headings"
        self.table.pack(fill=BOTH,expand=1)

        self.table.column("membertype",width=100)
        self.table.column("prno",width=100)
        self.table.column("idno",width=100)
        self.table.column("frstname",width=100)
        self.table.column("lastname",width=100)
        self.table.column("adress1",width=100)
        self.table.column("adress2",width=100)
        self.table.column("postid",width=100)
        self.table.column("mobile",width=100)
        self.table.column("bookid",width=100)
        self.table.column("booktitle",width=100)
        self.table.column("author",width=100)
        self.table.column("dateborrowed",width=100)
        self.table.column("datedue",width=100)
        self.table.column("days",width=100)
        self.table.column("latereturnfine",width=100)
        self.table.column("dateoverdue",width=100)
        self.table.column("finalprice",width=100)
        self.table.column("membertype",width=100)

        self.fetch_data()

    #---------------TO ADD THE ENTERED DATA INTO THE DATABASE-----------------------------    
    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="nandini08",database="mydata")
        my_cursor=conn.cursor() #cursor to enter the data in database
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(    #for accessing the data entered by the user;specifying variable names
        
                                                                                                                self.a1.get(),
                                                                                                                self.a2.get(),
                                                                                                                self.a3.get(),
                                                                                                                self.a4.get(),
                                                                                                                self.a5.get(),
                                                                                                                self.a6.get(),
                                                                                                                self.a7.get(),
                                                                                                                self.a8.get(),
                                                                                                                self.a9.get(),
                                                                                                                self.a10.get(),
                                                                                                                self.a11.get(),
                                                                                                                self.a12.get(),
                                                                                                                self.a13.get(),
                                                                                                                self.a14.get(),
                                                                                                                self.a15.get(),
                                                                                                                self.a16.get(),
                                                                                                                self.a17.get(),
                                                                                                                self.a18.get(),

                                                                                                              ))

        conn.commit()  #used to commit the changes made by the user to the database
        self.fetch_data()
        conn.close()   #for disconnecting from the database

        messagebox.showinfo("success","member has been inserted successfully!")
    def fetch_data(self): #TO SHOW DATA IN THE TABLE BELOW
        conn=mysql.connector.connect(host="localhost",username="root",password="nandini08",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("", END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self):
        cursor_row=self.table.focus() #sets the cursor on that specific widget when gui is opened
        content=self.table.item(cursor_row)
        row=content['values']

        




if __name__=="__main__":
    root=Tk()
    obj=lms(root)
    root.mainloop()