import datetime
import pymysql
import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
import calendar
from tkcalendar import *
import pymysql
from ttkwidgets.autocomplete import AutocompleteCombobox
import smtplib
import math, random

home = Tk()
home.title("Hotel")
width = home.winfo_screenwidth()
height = home.winfo_screenheight()
home.geometry('%dx%d'%(width,height))
home.resizable(1,1)

("------------------------------------------------- Background -------------------------------------------------")

load = Image.open('F:\Hotel Management\Images\\background5.jpg')
render = ImageTk.PhotoImage(load)
img = Label(home,image = render,bg= "black")
img.place(x = 0,y = 0)

frame = Frame(home,bg="black",width=700,height=900)
frame.place(x=1000,y=0)

def Staff_login():
    home.destroy()
    import Staff_login

def User_login():
    home.destroy()
    import User_login

def Sign_up():

    f1 = Frame(home,bg="#371d10",width=700,height=900)
    f1.place(x=1000,y=0)

    def register():
        
        mydb = pymysql.connect(host = "localhost", user = "root",passwd = "1916Pr@th@m",database = "Hotel")
        mycursor = mydb.cursor()
        
        name1 = name.get()
        email1 = email.get()
        mobile1 = mobile.get()
        password1 = password.get()
        re_password1 = re_password.get()

        if((((name1=="" or email1=="")or mobile1=="")or variable.get()=="Select")or password==""):
            messagebox.showwarning("Warning","Please fill All the Credentials !!")
        else:
            if(password1==re_password1):
                if(("@" in email1) and ((".com") in email1)):
                    try:
                        # Create your SMTP session
                        smtp = smtplib.SMTP('smtp.gmail.com', 587)
                        # Use TLS to add security
                        smtp.starttls()
                        # User Authentication
                        smtp.login("imperialhotel401@gmail.com","1916pratham")

                        OTP =random.randrange(100001,999999)
                
                        if __name__ == "_main_" :
                            print("OTP of 6 digits:",OTP)
                        # Defining The Message
                        message = "\t\t\t\t Welcome to Imperial Hotel \n\n\nHii {},\n\nYour One time Password(OTP) for Verification is \n{}".format(name1,OTP)
                        # Sending the Email
                        smtp.sendmail("pnemade1916@gmail.com", "{}".format(email1), message)
                        # Terminating the session
                        smtp.quit()
                        messagebox.showinfo("OTP","Email sent successfully")
                        
                    except Exception as ex:
                        messagebox.showwarning("Warning","Some Error Occuried\n Try Again Later",ex)

                    frame = Frame(f1,bg="black",width=600,height=400)
                    frame.place(x=0,y=600)

                    OtpBox = StringVar()
                    a7 = Label(frame, text="     Verify You'r Email\n Enter 6 Digit OTP Recived on Registered Email", font=("Flexure",15,"bold"),bg = "black",fg="white",bd = 2)
                    a7.place(x=45,y=25)
                    a7 = Entry(frame, font=("Flexure ",15,"bold"),bg = "White",bd = 2,width=15,justify =LEFT,textvariable=OtpBox)
                    a7.place(x=180,y=100)

                    def done():
                        
                        if(int(OTP)==int(OtpBox.get())):
                            messagebox.showinfo("Welcome !!"," Email Verified\n You Have Registered Successfully")

                            try :
                                mycursor.execute(" create table Register (Sr_no int(100) AUTO_INCREMENT PRIMARY KEY,Name varchar(50),Email text(50),Mobile text(50),Gender text(10),Password text(50),Re_password text(50))")  
                                mydb.commit()
                                print('You have sucessfully created your Table ')

                            except pymysql.err.OperationalError:
                                print('table already exist')

                            mycursor.execute("insert into Register (Name,Email,Mobile,Gender,Password,Re_password)values('{}','{}','{}','{}','{}','{}')".format(name1,email1,mobile1,variable.get(),password1,re_password1))
                            mydb.commit()
                        else:
                            messagebox.showwarning("ERROR!!","OTP Didn't Match")

                    done = Button(frame,text='Done',font=("Flexure",12,"bold"),bd = 3,bg = "white",fg='black',command = done)
                    done.place(x=240,y=150)
                    
                else:
                    messagebox.showwarning("Warning","Plzzzz Enter Valid Email_Id")
            else:
                messagebox.showwarning("Warning","Password Didn't Match")

    name = StringVar()
    a1 = Label(f1, text="Enter Name", font=("msserif 15",15,"bold"),fg = "white",bg ="#371d10",bd = 2)
    a1.place(x=60,y=200)
    a1 = Entry(f1, font=("COOPER BLACK ",15,"bold"),bg = "White",bd = 2,width=15,justify =LEFT,textvariable = name)
    a1.place(x=270,y=200)
    a1.insert(0,"Enter Name *")
    def OnEntryClick1(event):
        if a1.get() == "Enter Name *":
            a1.delete(0,END)
            a1.insert(0,"")
    a1.bind("<FocusIn>",OnEntryClick1)
        

    email = StringVar()
    a2 = Label(f1, text="Enter Email", font=("Flexure",15,"bold"),fg = "white",bg ="#371d10",bd = 2)
    a2.place(x=60,y=250)
    a2 = Entry(f1, font=("COOPER BLACK ",15,"bold"),bg = "White",bd = 2,width=15,justify =LEFT,textvariable = email)
    a2.place(x=270,y=250)
    a2.insert(0,"Enter Email *")
    def OnEntryClick2(event):
        if a2.get() == "Enter Email *":
            a2.delete(0,END)
            a2.insert(0,"")
    a2.bind("<FocusIn>",OnEntryClick2)

    mobile = StringVar()
    a3 = Label(f1, text="Enter Mobile",font=("Flexure",15,"bold"),fg = "white",bg ="#371d10",bd = 2)
    a3.place(x=60,y=300)
    a3 = Entry(f1,font=("COOPER BLACK ",15,"bold"),bg = "White",bd = 2,width=15,justify =LEFT,textvariable = mobile)
    a3.place(x=270,y=300)
    a3.insert(0,"Enter Mobile *")
    def OnEntryClick3(event):
        if a3.get() == "Enter Mobile *":
            a3.delete(0,END)
            a3.insert(0,"")
    a3.bind("<FocusIn>",OnEntryClick3)
    
    gender = StringVar()
    a4 = Label(f1, text="Select Gender",font=("Flexure",15,"bold"),fg = "white",bg ="#371d10",bd = 2)
    a4.place(x=60,y=350)
    variable = StringVar(f1)
    gender = ("Male","Female","Other")
    variable.set("Select")
    gen = OptionMenu(f1,variable,*gender)
    gen.place(x=270,y=350)

    password = StringVar()
    a5 = Label(f1, text="Enter Password",font=("Flexure",15,"bold"),fg = "white",bg ="#371d10",bd = 2)
    a5.place(x=60,y=400)
    a5 = Entry(f1,font=("COOPER BLACK ",15,"bold"),bg = "White",bd = 2,width=15,justify =LEFT,textvariable = password,show='*')
    a5.place(x=270,y=400)

    re_password = StringVar()
    a6 = Label(f1, text="Re-Enter Password",font=("Flexure",15,"bold"),fg = "white",bg ="#371d10",bd = 2)
    a6.place(x=60,y=450)
    a6 = Entry(f1,font=("COOPER BLACK ",15,"bold"),bg = "White",bd = 2,width=15,justify =LEFT,textvariable = re_password,show='*')
    a6.place(x=270,y=450)

    register = Button(f1, text='Register',font=("Flexure",12,"bold"),bd = 3,bg = "white",fg='black', command= register)
    register.place(x=200,y=510)
    
Heading=Label(home,text="Imperial Hotel",font=("COOPER BLACK",35,"bold"), background="black",foreground='cyan')
Heading.place(x=1050,y=0)
    
motto=Label(home,text="A great hotel needs a great location, great staff,\n and a memorable experience. We have those all",font=("Flexure",16,"italic"), background="black",foreground='cyan')
motto.place(x=1030,y=300)


("--------------------------------------------------- Home ------------------------------------------------")

img106 = PhotoImage(file = "F:\Hotel Management\Images\\staff.png")
btn = Button(home,image = img106,bd = 0,bg = "#b59b7f",activebackground ='#b59b7f',command = Staff_login)
btn.place(x=830,y=40)

img13 = PhotoImage(file = "F:\Hotel Management\Images\\user_login.png")
btn = Button(home,image = img13,bd = 0,bg = "white",activebackground ='white',command = User_login)
btn.place(x=830,y=200)

img45 = PhotoImage(file = "F:\Hotel Management\Images\\sign_up.png")
btn = Button(home,image = img45,bd = 0,bg = "white",activebackground ='white',command=Sign_up)
btn.place(x=845,y=120)
