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


mydb = pymysql.connect(host = "localhost", user = "root",passwd = "amit1345",database = "Hotel")
mycursor = mydb.cursor()

try:
    mycursor.execute('create database Hotel')
    mydb.commit()
except:
    pass

try :
    mycursor.execute("create table Roomd(Room_no int(50) AUTO_INCREMENT primary key,beds int(50),ac varchar(10),tv varchar(10),internet varchar(10),price int(50),reserve_status varchar(20))")
    mydb.commit()
except pymysql.err.OperationalError:
    pass

##mycursor.execute("insert into Roomd (beds,ac,tv,internet,price,reserve_status)values(2,'yes','no','yes',4500,'no')")
##mydb.commit()


user = Tk()
user.title("User Login")
user.config(bg = 'white')
user.geometry("450x700+550+80")
user.resizable(0,0)

User = Label(user,text = "User Login",font=("COOPER BLACK",30,"bold"), background="white")
User.place(x=110, y=10)

def login():
    email1 = E1.get()
    password1 = E2.get()

    mycursor.execute(F"SELECT Email FROM Register WHERE Email = '{email1}' AND Password = '{password1}'")

    if (email1=="" and password1==""):
        messagebox.showinfo("ERROR","Please fill All the Credentials !!")

    else:
        (mycursor.execute(F"SELECT Email FROM Register WHERE Email = '{email1}' AND Password = '{password1}'"))
        if not mycursor.fetchone():
            messagebox.showinfo("ERROR !!","Incorrect Username Or Password")

        else :
            messagebox.showinfo("WELCOME","Succesfully Login")
            
            def desk():
                user.destroy()
                desk = Tk()
                width = desk.winfo_screenwidth()
                height = desk.winfo_screenheight()
                desk.geometry('%dx%d'%(width,height))
                desk.title("User Desk :)")

                l2 = Label(desk,text = "Imperial Hotel",bg ="#F0F0F0",fg="black",font=("COOPER BLACK",35,"bold"))
                l2.place(x=670,y=50)

                def time():
                    string = strftime('%H:%M:%S %p\n%d %B %Y')
                    lab0.config(text=string)
                    lab0.after(100, time)

                lab0 = Label(desk, font=("Flexure",15,"bold"), background="#F0F0F0", foreground="black")
                lab0.place(x=1300, y=50)
                time()

                a = Frame(desk,bg="black",width=1300,height=140 )
                a.place(x=270,y=170)

                a1= Frame(desk,bg="black",width=280,height=850)
                a1.place(x=0,y=0)

                img = ImageTk.PhotoImage(Image.open("Imperial.jpg"))
                logo1 = Label(desk,image = img)
                logo1.place(x=3,y=0)

                def reserves():
                    b_frame = Frame(desk,height=550,width=1260,bg='cyan')
                    b_frame.place(x=280,y=210+6+20+60+11)
                    b_frame.pack_propagate(False)

                    vline = Frame(b_frame,height=400,width=7,bg='black').place(x=800,y=0)

                    Label(b_frame,text='Personal Information',font='msserif 15',bg='cyan',fg = "black").place(x=290,y=10)

                    fullN = StringVar()
                    fn = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable = fullN,justify =LEFT)
                    fn.place(x=30,y=50)
                    fn.insert(0, 'Full Name *')

                    Adh =StringVar()
                    adhar = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable =Adh,justify =LEFT)
                    adhar.place(x=540,y=50)
                    adhar.insert(0, 'Adhar Number *')

                    def on_entry_click1(event):
                            if fn.get() == 'Full Name *' :
                                fn.delete(0,END)
                                fn.insert(0,'')
                    def on_exit1(event):
                            if fn.get()=='':
                                fn.insert(0,'Full Name *')

                    def on_entry_click2(event):
                            if adhar.get() == 'Adhar Number *' :
                                adhar.delete(0,END)
                                adhar.insert(0,'')
                    def on_exit2(event):
                            if adhar.get()=='':
                                adhar.insert(0,'Adhar Number *')

                    fn.bind('<FocusIn>', on_entry_click1)
                    fn.bind('<FocusOut>',on_exit1)
                    adhar.bind('<FocusIn>', on_entry_click2)
                    adhar.bind('<FocusOut>',on_exit2)


                    Label(b_frame,text='Contact Information',font='msserif 15',bg='cyan',fg = "black").place(x=290,y=90)

                    Contact = StringVar()
                    cn = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable =Contact,justify =LEFT)
                    cn.place(x=30,y=150)
                    cn.insert(0, 'Contact Number *')

                    Email = StringVar()
                    em = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable =Email,justify =LEFT)
                    em.place(x=290,y=150)
                    em.insert(0, 'Email *')

                    Address = StringVar()
                    add = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable =Address,justify =LEFT)
                    add.place(x=540,y=150)
                    add.insert(0, "Guest's Address *")

                    def on_entry_click4(event):
                            if cn.get() == 'Contact Number *' :
                                    cn.delete(0,END)
                                    cn.insert(0,'')
                    def on_entry_click5(event):
                            if em.get() == 'Email *' :
                                    em.delete(0,END)
                                    em.insert(0,'')
                    def on_entry_click6(event):
                            if add.get() == "Guest's Address *" :
                                    add.delete(0,END)
                                    add.insert(0,'')
                    def on_exit4(event):
                            if cn.get()=='':
                                    cn.insert(0,'Contact Number *')
                    def on_exit5(event):
                            if em.get()=='':
                                    em.insert(0,'Email *')
                    def on_exit6(event):
                            if add.get()=='':
                                    add.insert(0,"Guest's Address *")

                    cn.bind('<FocusIn>', on_entry_click4)
                    em.bind('<FocusIn>', on_entry_click5)
                    add.bind('<FocusIn>', on_entry_click6)
                    cn.bind('<FocusOut>',on_exit4)
                    em.bind('<FocusOut>',on_exit5)
                    add.bind('<FocusOut>',on_exit6)

                    Label(b_frame,text='Reservation Information',font='msserif 15',bg='cyan',fg = 'black').place(x=290,y=200)

                    NOP = StringVar()
                    nop = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable =NOP,justify =LEFT)
                    nop.place(x=30,y=250)
                    nop.insert(0, "Number Of Persons *")

                    DOA = StringVar()
                    doa = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable =DOA,justify =LEFT)
                    doa.place(x=290,y=285)
                    doa.insert(0, "Date Of Arrival *")

                    DPA = StringVar()
                    dpa = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable = DPA,justify =LEFT)
                    dpa.place(x=540,y=250)
                    dpa.insert(0, "Deposit Amount *")

                    RNO = StringVar()
                    rno = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable =RNO,justify =LEFT)
                    rno.place(x=30,y=320)
                    rno.insert(0, "Room Number *")

                    VP = StringVar()
                    vp = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable = VP,justify =LEFT)
                    vp.place(x=540,y=320)
                    vp.insert(0, "Visit Purpose *")

                    def on_entry_click7(event):
                            if nop.get() == 'Number Of Persons *' :
                                    nop.delete(0,END)
                                    nop.insert(0,'')
                    def on_entry_click8(event):
                            if doa.get() == 'Date Of Arrival *' :
                                    doa.delete(0,END)
                                    doa.insert(0,'')
                    def on_entry_click9(event):
                            if dpa.get() == 'Deposit Amount *' :
                                    dpa.delete(0,END)
                                    dpa.insert(0,'')
                    def on_entry_click10(event):
                            if rno.get() == 'Room Number *' :
                                    rno.delete(0,END)
                                    rno.insert(0,'')
                    def on_entry_click11(event):
                            if vp.get() == 'Visit Purpose *' :
                                    vp.delete(0,END)
                                    vp.insert(0,'')
                    def on_exit7(event):
                            if nop.get()=='':
                                    nop.insert(0,'Number Of Persons *')
                    def on_exit8(event):
                            if doa.get()=='':
                                    doa.insert(0,'Date Of Arrival *')
                    def on_exit9(event):
                            if dpa.get()=='':
                                    dpa.insert(0,'Deposit Amount *')
                    def on_exit10(event):
                            if rno.get()=='':
                                    rno.insert(0,'Room Number *')
                    def on_exit11(event):
                            if vp.get()=='':
                                    vp.insert(0,'Visit Purpose *')

                    nop.bind('<FocusIn>', on_entry_click7)
                    doa.bind('<FocusIn>', on_entry_click8)
                    dpa.bind('<FocusIn>', on_entry_click9)
                    rno.bind('<FocusIn>', on_entry_click10)
                    vp.bind('<FocusIn>', on_entry_click11)
                    nop.bind('<FocusOut>',on_exit7)
                    doa.bind('<FocusOut>',on_exit8)
                    dpa.bind('<FocusOut>',on_exit9)
                    rno.bind('<FocusOut>',on_exit10)
                    vp.bind('<FocusOut>',on_exit10)

                    
                    def booking():
                        try :
                            mycursor.execute(" create table Check_in (Sr_no int(100) AUTO_INCREMENT PRIMARY KEY,Name text(50),Adhar_number varchar(50),Mobil_number varchar(50),Email varchar(50),Address varchar(50),No_of_persons int(50),Date_Arrival date,Deposit_Amount int(50),Alloted_room int(10),Purpose_visit text(50))")  
                            mydb.commit()
                            print('You have sucessfully created your Table ')

                        except pymysql.err.OperationalError:
                            print('table already exist')

                        if fullN.get() == 'Full Name *' or Adh.get() == 'Adhar Number *' or Contact.get() == 'Contact Number *' or Email.get() == 'Email *' or Address.get() == "Guest's Address *" or NOP.get() == 'Number Of Persons *' or DOA.get() == 'Date Of Arrival *'or DPA.get() == 'Deposit Amount *' or RNO.get() == 'Room Number *' or VP.get() == "Visit Purpose *":
                            messagebox.showinfo('Incomplete','Fill All the Fields marked by *')
                        elif fullN.get() == '' or Adh.get() == '' or Contact.get() == '' or Email.get() == '' or Address.get() == "" or NOP.get() == '' or DOA.get() == '' or DPA.get() == '' or RNO.get() == '' or VP.get()=='':
                            messagebox.showinfo('Incomplete','Fill All the Fields marked by')
                        else :
                            mycursor.execute("Select Alloted_room from Check_in")
                            y1 = mycursor.fetchall()
                            l = []
                            for j in y1:
                                l.append(int(j[0]))
                            if int(RNO.get()) in l:
                                messagebox.showinfo('','Room  {} is Occupied'.format(RNO.get()))
                            else:
                                messagebox.showinfo("Congrats","You Successfully Reserved a Room"+str(RNO.get()))
                                mycursor.execute("insert into Check_in (Name,Adhar_number,Mobil_number,Email,Address,No_of_persons,Date_Arrival,Deposit_Amount,Alloted_room,Purpose_visit)values('{}','{}','{}','{}','{}',{},'{}',{},{},'{}')".format(fullN.get(),Adh.get(),Contact.get(),Email.get(),Address.get(),NOP.get(),DOA.get(),DPA.get(),RNO.get(),VP.get()))
                                mydb.commit()

                                mycursor.execute("update roomd set reserve_status = 'yes' where Room_no = {} ".format(RNO.get()))

                    ##-------------------- Filter --------------------

                    Label(b_frame,text='Filter',font=('msserif',20,'bold'),bg='cyan').place(x=1000,y=20)
                    nbb = IntVar()
                    acb = IntVar()
                    tvb = IntVar()
                    wifib = IntVar()

                    style = ttk.Style()
                    style.map('TCombobox', fieldbackground=[('readonly','white')])
                    Label(b_frame,text='Bed(s) :',bg='cyan',font='17').place(x=880,y=100)
                    nb = ttk.Combobox(b_frame,values=['please select...','1','2','3'],font="10",state='readonly',width=20)
                    nb.place(x=980,y=100)
                    nb.current(0)

                    Label(b_frame,text='AC :',font='17 ',bg='cyan').place(x=880,y=150)
                    ac = ttk.Combobox(b_frame,values=['please select...','Yes','No'],font="10",state='readonly',width=20)
                    ac.place(x=980,y=150)
                    ac.current(0)


                    Label(b_frame,text='TV :',font='17 ',bg='cyan').place(x=882,y=200)
                    tv = ttk.Combobox(b_frame,values=['please select...','Yes','No'],font="10",state='readonly',width=20)
                    tv.place(x=980,y=200)
                    tv.current(0)

                    Label(b_frame,text='Wifi :',font='17',bg='cyan').place(x=882,y=250)
                    wifi = ttk.Combobox(b_frame,values=['please select...','Yes','No'],font="10",state='readonly',width=20)
                    wifi.place(x=980,y=250)
                    wifi.current(0)
                    listofrooms = Listbox(b_frame,height=6,width=36)
                    listofrooms.place(x=885,y=300)
                    listofrooms.insert(END,'Rooms of Your Choice will appear Here')
                    listofrooms.insert(END,'once you apply filter')
                    
                    def findrooms():
                        mycursor.execute('select Room_no,price,reserve_status from roomd where beds = "{}" and ac = "{}" and tv = "{}" and internet = "{}" order by price asc'.format(nb.get(),ac.get(),tv.get(),wifi.get()))
                        x = mycursor.fetchall()
                        listofrooms.delete(0,END)
                        if x == []:
                            listofrooms.insert(END,'No Matching Found')
                        for i in x :
                            listofrooms.insert(END,'Room Number '+str(i[0])+' - Price - '+str(i[1]))
                                    
                    Res = Button(b_frame,text='Reserve',bg='white',fg='cyan4',font='timenewroman 11',activebackground='green',command=booking).place(x=235,y=400)
                    findrooms = Button(b_frame,text='Find Rooms',bg='white',fg='cyan4',font='timenewroman 9 bold',activebackground='green',command = findrooms).place(x=980,y=430)

                    scrollbar = Scrollbar(b_frame, orient="vertical")
                    scrollbar.config(command=listofrooms.yview)
                    scrollbar.place(x=1164,y=300,height=111)
                    listofrooms.config(yscrollcommand=scrollbar.set)

                img2 = PhotoImage(file = "F:\Hotel Management\Images\\reserve.png")
                reserve = Label(desk,text = "Reserve",bg ="black",fg="white",font=("Flexure",15,"bold"))
                reserve.place(x=470,y=170)
                reserve_bt = Button(desk,image =img2,bd = 0,bg = "#000000",activebackground ='#000000',command =reserves)
                reserve_bt.place(x=460,y=203)

                def rooms():
                    b_frame = Frame(desk,height=550,width=1260,bg='grey')
                    b_frame.place(x=280,y=210+6+20+60+11)
                    b_frame.pack_propagate(False)
                    b_frame.tkraise()

                    def roomdet(rno):
                        Label(b_frame,text='Room %s'% rno,font='msserif 15',fg='white',bg='cyan4',width=10).place(x = 660,y=10)
                        mycursor.execute("select * from roomd where Room_no = {}".format(rno))
                        rdata=mycursor.fetchall()
                        smf1 = Frame(b_frame,height=120,width=145,bg='white')
                        tr = Label(smf1,text='Total Bed(s):',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
                        tr.pack(side='top')
                        smf1.pack_propagate(False)
                        smf1.place(x=300,y=130)
                        Label(smf1,text=str(rdata[0][1]),fg='cyan4',bg='white',font='msserif 35').pack()
                        smf2 = Frame(b_frame,height=120,width=145,bg='white')
                        tr = Label(smf2,text='AC Available?',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
                        tr.pack(side='top')
                        smf2.pack_propagate(False)
                        smf2.place(x=450,y=130)
                        Label(smf2,text=str(rdata[0][2]),fg='cyan4',bg='white',font='msserif 35').pack()
                        smf2 = Frame(b_frame,height=120,width=145,bg='white')
                        tr = Label(smf2,text='TV Available?',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
                        tr.pack(side='top')
                        smf2.pack_propagate(False)
                        smf2.place(x=600,y=130)
                        Label(smf2,text=str(rdata[0][3]),fg='cyan4',bg='white',font='msserif 35').pack()
                        smf2 = Frame(b_frame,height=120,width=145,bg='white')
                        tr = Label(smf2,text='  Wifi ?',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
                        tr.pack(side='top')
                        smf2.pack_propagate(False)
                        smf2.place(x=750,y=130)
                        Label(smf2,text=str(rdata[0][4]),fg='cyan4',bg='white',font='msserif 35').pack()
                        smf2 = Frame(b_frame,height=120,width=145,bg='white')
                        tr = Label(smf2,text=' Price ?',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
                        tr.pack(side='top')
                        smf2.pack_propagate(False)
                        smf2.place(x=900,y=130)
                        Label(smf2,text=str(rdata[0][5]),fg='cyan4',bg='white',font='msserif 35').pack()
                        smf2 = Frame(b_frame,height=120,width=145,bg='white')
                        tr = Label(smf2,text='Reserved ?',fg='white',bg='cyan4',width=100,height=2,font='msserif 15')
                        tr.pack(side='top')
                        smf2.pack_propagate(False)
                        smf2.place(x=1050,y=130)
                        p=''
                        if rdata[0][6]=='no':
                            p = 'No'
                        else :
                            p = 'Yes'
                        Label(smf2,text=p,fg='cyan4',bg='white',font='msserif 35').pack()
                        
                    roomdet(1)

                    bt1  = Button(b_frame,font='mssherif 10', text="Room 1", bg='white',fg='cyan4',width=30,command=lambda:roomdet(1))
                    bt1.place(x=15,y=10)
                    bt2  = Button(b_frame,font='mssherif 10', text="Room 2", bg='white',fg='cyan4',width=30,command=lambda:roomdet(2))
                    bt2.place(x = 15,y = 40)
                    bt3  = Button(b_frame,font='mssherif 10', text="Room 3", bg='white',fg='cyan4',width=30,command=lambda:roomdet(3))
                    bt3.place(x = 15,y = 70)
                    bt4  = Button(b_frame,font='mssherif 10', text="Room 4", bg='white',fg='cyan4',width=30,command=lambda:roomdet(4))
                    bt4.place(x = 15,y = 100)
                    bt5  = Button(b_frame,font='mssherif 10', text="Room 5", bg='white',fg='cyan4',width=30,command=lambda:roomdet(5))
                    bt5.place(x = 15,y = 130)
                    bt6  = Button(b_frame,font='mssherif 10', text="Room 6", bg='white',fg='cyan4',width=30,command=lambda:roomdet(6))
                    bt6.place(x = 15,y = 160)
                    bt7  = Button(b_frame,font='mssherif 10', text="Room 7", bg='white',fg='cyan4',width=30,command=lambda:roomdet(7))
                    bt7.place(x = 15,y = 190)
                    bt8  = Button(b_frame,font='mssherif 10', text="Room 8", bg='white',fg='cyan4',width=30,command=lambda:roomdet(8))
                    bt8.place(x = 15,y = 220)
                    bt9  = Button(b_frame,font='mssherif 10', text="Room 9", bg='white',fg='cyan4',width=30,command=lambda:roomdet(9))
                    bt9.place(x = 15,y = 250)
                    bt10 = Button(b_frame,font='mssherif 10', text="Room 10",bg='white',fg='cyan4',width=30,command=lambda:roomdet(10))
                    bt10.place(x = 15,y = 280)
                    bt11 = Button(b_frame,font='mssherif 10', text="Room 11",bg='white',fg='cyan4',width=30,command=lambda:roomdet(11))
                    bt11.place(x = 15,y = 310)
                    bt12 = Button(b_frame,font='mssherif 10', text="Room 12",bg='white',fg='cyan4',width=30,command=lambda:roomdet(12))
                    bt12.place(x = 15,y = 340)
                    bt13 = Button(b_frame,font='mssherif 10', text="Room 13",bg='white',fg='cyan4',width=30,command=lambda:roomdet(13))
                    bt13.place(x = 15,y = 370)
                    bt14 = Button(b_frame,font='mssherif 10', text="Room 14",bg='white',fg='cyan4',width=30,command=lambda:roomdet(14))
                    bt14.place(x = 15,y = 400)
                    bt15 = Button(b_frame,font='mssherif 10', text="Room 15",bg='white',fg='cyan4',width=30,command=lambda:roomdet(15))
                    bt15.place(x = 15,y = 430)
                    bt16 = Button(b_frame,font='mssherif 10', text="Room 16",bg='white',fg='cyan4',width=30,command=lambda:roomdet(16))
                    bt16.place(x = 15,y = 460)
                    bt17 = Button(b_frame,font='mssherif 10', text="Room 17",bg='white',fg='cyan4',width=30,command=lambda:roomdet(17))
                    bt17.place(x = 15,y = 490)
                    bt18 = Button(b_frame,font='mssherif 10', text="Room 18",bg='white',fg='cyan4',width=30,command=lambda:roomdet(18))
                    bt18.place(x = 15,y = 520)
                    bt19 = Button(b_frame,font='mssherif 10', text="Room 19",bg='white',fg='cyan4',width=30,command=lambda:roomdet(19))
                    bt19.place(x = 15,y = 550)
                    bt20 = Button(b_frame,font='mssherif 10', text="Room 20",bg='white',fg='cyan4',width=30,command=lambda:roomdet(20))
                    bt20.place(x = 15,y = 580)

                img3 = PhotoImage(file = "F:\Hotel Management\Images\\rooms.png")
                room = Label(desk,text = "Room Info",bg ="black",fg="white",font=("Flexure",15,"bold"))
                room.place(x=620,y=170)
                room_bt = Button(desk,image = img3,bd = 0,bg = "#000000",activebackground ='#000000',command = rooms)
                room_bt.place(x=620,y=203)

                def staff():
                    b_frame = Frame(desk,height=550,width=1260,bg='white')
                    b_frame.place(x=280,y=210+6+20+60+11)
                    b_frame.pack_propagate(False)
                    b_frame.tkraise()

                    emp1f = Frame(b_frame)
                    path1 = "images/manager.jpg"
                    img1 = ImageTk.PhotoImage(Image.open(path1))
                    emp1 = Label(emp1f,image = img1)
                    emp1.image=img1
                    emp1.pack()
                    emp1f.place(x=0,y=0)
                    emp1inf = Frame(b_frame,bg='white',height=122,width=280)
                    Label(emp1inf,text="Manager",bg='white',font='msserif 17 bold').place(x=60,y=0)
                    Label(emp1inf,text="Mr. Pratham Nemade",bg='white',fg="green",font='msserif 10 bold').place(x=60,y=37)
                    Label(emp1inf,text="Contact : 9665920869 ",bg='white',fg="Grey",font='msserif 10').place(x=60,y=59)
                    Label(emp1inf,text="Mail : Manager@imperialhotel.com",bg='white',fg="Grey",font='msserif 10').place(x=60,y=83)
                    emp1inf.pack_propagate(False)
                    emp1inf.place(x=160,y=26)

                    emp1f = Frame(b_frame)
                    path3 = "images/chef.png"
                    img3 = ImageTk.PhotoImage(Image.open(path3))
                    emp1 = Label(emp1f,image = img3)
                    emp1.image=img3
                    emp1.pack()
                    emp1f.place(x=0,y=160)
                    emp1inf = Frame(b_frame,bg='white',height=121,width=280)
                    Label(emp1inf,text="Restaurant",bg='white',font='msserif 17 bold').place(x=60,y=0)
                    Label(emp1inf,text="Mr. Rishi Jain (Head)",bg='white',fg="Green",font='msserif 10 bold').place(x=60,y=37)
                    Label(emp1inf,text="Contact : 9668744125",bg='white',fg="Grey",font='msserif 10').place(x=60,y=59)
                    Label(emp1inf,text="Mail : Restaurant@imperialhotel.com",bg='white',fg="Grey",font='msserif 10').place(x=60,y=83)
                    emp1inf.pack_propagate(False)
                    emp1inf.place(x=160,y=185)
                    emp1inf.tkraise()


                    emp1f = Frame(b_frame)
                    path2 = "images/ReceptionWelcome.jpg"
                    img2 = ImageTk.PhotoImage(Image.open(path2))
                    emp1 = Label(emp1f,image = img2)
                    emp1.image=img2
                    emp1.pack()
                    emp1f.place(x=790,y=0)
                    emp1inf = Frame(b_frame,bg='white',height=116,width=280)
                    Label(emp1inf,text="Reception",bg='white',font='msserif 17 bold').place(x=45,y=0)
                    Label(emp1inf,text="Ms. Kanishya Shrivastava",bg='white',fg="Green",font='msserif 10 bold').place(x=45,y=37)
                    Label(emp1inf,text="Contact : 7885544741",bg='white',fg="Grey",font='msserif 10').place(x=45,y=59)
                    Label(emp1inf,text="Mail : Reception@imperialhotel.com",bg='white',fg="Grey",font='msserif 10').place(x=45,y=83)
                    emp1inf.pack_propagate(False)
                    emp1inf.place(x=950,y=27)

                    emp1f = Frame(b_frame)
                    path4 = "images/RoomService.jpg"
                    img4 = ImageTk.PhotoImage(Image.open(path4))
                    emp1 = Label(emp1f,image = img4)
                    emp1.image=img4
                    emp1.pack()
                    emp1f.place(x=790,y=160)
                    emp1inf = Frame(b_frame,bg='White',height=121,width=280)
                    Label(emp1inf,text="Room Service",bg='white',font='msserif 17 bold').place(x=45,y=0)
                    Label(emp1inf,text="Ms. Palak Tiwari (Head)",bg='white',fg="green",font='msserif 10 bold').place(x=45,y=37)
                    Label(emp1inf,text="Contact : 8554788203",bg='white',fg="Grey",font='msserif 10').place(x=45,y=59)
                    Label(emp1inf,text="Mail : Roomsserv@imperialhotel.com",bg='white',fg="Grey",font='msserif 10').place(x=45,y=83)
                    emp1inf.pack_propagate(False)
                    emp1inf.place(x=950,y=185)

                    emp1f = Frame(b_frame)
                    path5 = "images/cab.jpg"
                    img5 = ImageTk.PhotoImage(Image.open(path5))
                    emp1 = Label(emp1f,image = img5)
                    emp1.image=img5
                    emp1.pack()
                    emp1f.place(x=0,y=320)
                    emp1inf = Frame(b_frame,bg='White',height=121,width=280)
                    Label(emp1inf,text="Taxi Service",bg='white',font='msserif 17 bold').place(x=60,y=0)
                    Label(emp1inf,text="Mr. Hitesh Kadukar",bg='white',fg="green",font='msserif 10 bold').place(x=60,y=37)
                    Label(emp1inf,text="Contact : 8554788203",bg='white',fg="Grey",font='msserif 10').place(x=60,y=59)
                    Label(emp1inf,text="Mail : Taxi@imperialhotel.com",bg='white',fg="Grey",font='msserif 10').place(x=60,y=83)
                    emp1inf.pack_propagate(False)
                    emp1inf.place(x=160,y=344)

                img4 = PhotoImage(file = "F:\Hotel Management\Images\\contacts.png")
                contacts = Label(desk,text = "Contacts",bg ="black",fg="white",font=("Flexure",15,"bold"))
                contacts.place(x=785,y=170)
                contacts_bt = Button(desk,image =img4,bd = 0,bg = "#000000",activebackground ='#000000',command = staff)
                contacts_bt.place(x=780,y=203)

                img5 = PhotoImage(file = "F:\Hotel Management\Images\\food.png")
                food = Label(desk,text = "Food & Beverages",bg ="black",fg="white",font=("Flexure",15,"bold"))
                food.place(x=900,y=170)
                food_bt = Button(desk,image =img5,bd = 0,bg = "#000000",activebackground ='#000000')
                food_bt.place(x=940,y=203)

                
                def reviews():
                    b_frame = Frame(desk,height=550,width=1260,bg='purple')
                    b_frame.place(x=280,y=210+6+20+60+11)
                    b_frame.pack_propagate(False)
                    b_frame.tkraise()

                    Rating = Label(b_frame,text='Rating',bg ="purple",fg="white",font=("Flexure",15,"bold"))
                    Rating.place(x=20,y=10)
                    Rating1 = ttk.Combobox(b_frame,values=['*','**','***','*****','******'],font=("Flexure",12,"bold"),state='readonly',width=15)
                    Rating1.place(x= 20,y = 40)

                    Review = Label(b_frame,text='Review',bg ="purple",fg="white",font=("Flexure",15,"bold"))
                    Review.place(x=230,y=10)
                    rev = StringVar()
                    Review1 = Entry(b_frame,font=("Flexure",15,"bold"),width=25,textvariable=rev)
                    Review1.place(x= 230,y = 40)
                    
                    tbl = ttk.Treeview(b_frame,selectmode ="browse",show='headings',height=18)
                    tbl.place(x=30,y=100)
                    scrl = ttk.Scrollbar(b_frame,orient='vertical',command=tbl.yview)
                    scrl.pack(side='right',fill='y')
                    tbl.configure(xscrollcommand= scrl.set)
                    tbl['columns'] = ("1","2","3","4")
                    tbl.column("1",width= 100,anchor ="c",stretch=False)
                    tbl.column("2",width= 200,anchor ="c",stretch=False)
                    tbl.column("3",width= 200,anchor ="c",stretch=False)
                    tbl.column("4",width= 500,anchor ="c",stretch=False)
                    tbl.heading("1",text='Sr no')
                    tbl.heading("2",text='Name')
                    tbl.heading("3",text='Rating')
                    tbl.heading("4",text='Review')
                    tbl.tag_configure('oddrow',background='white')
                    tbl.tag_configure('evenrow',background='blue')
                    mycursor.execute("select * from Review_t")
                    revi = mycursor.fetchall()
                    for dt in revi:
                        tbl.insert("","end",iid=dt[0],values=(dt[0],dt[1],dt[2],dt[3]))
                    
                    style=ttk.Style()
                    style.theme_use("default")

                    def submitrev():
                        try :
                            mycursor.execute(" create table Review_t(Sr_no int(100) AUTO_INCREMENT PRIMARY KEY,Name varchar(50),Rating varchar(50),Reviews varchar(100))")  
                            mydb.commit()
                            print('You have sucessfully created your Table ')

                        except pymysql.err.OperationalError:
                            print('table already exist')

                        mycursor.execute("select Name from Register where Email = '{}'".format(E1.get()))
                        naam = mycursor.fetchone()
                            
                        mycursor.execute("insert into Review_t(Name,Rating,Reviews)values('{}','{}','{}')".format(naam[0],Rating1.get(),rev.get()))
                        mydb.commit()

                    rev_bt = Button(b_frame,text="Submit",bd = 3,bg = "green",activebackground ='blue',command=submitrev)
                    rev_bt.place(x=530,y=40)
                
                img6 = PhotoImage(file = "F:\Hotel Management\Images\\review.png")
                review = Label(desk,text = "Reviews",bg ="black",fg="white",font=("Flexure",15,"bold"))
                review.place(x=1110,y=170)
                review_bt = Button(desk,image =img6,bd = 0,bg = "#000000",activebackground ='#000000',command=reviews)
                review_bt.place(x=1100,y=203)

                def exit():
                    q = messagebox.askyesno("Exit","Do you really want to exit ?")
                    if(q):
                        desk.destroy()
                        import Main_page

                img10 = PhotoImage(file = "F:\Hotel Management\Images\\exit1.png")
                exit1 = Label(desk,text = "Exit",bg ="black",fg="white",font=("Flexure",15,"bold"))
                exit1.place(x=1270,y=170)
                exit2 = Button(desk,image =img10,bd = 0,bg = "#000000",activebackground ='#000000',command = exit)
                exit2.place(x=1260,y=203)
    
                desk.mainloop()
            desk()

("------------------------------------------------- Background --------------------------------------------")

load = Image.open('F:\Hotel Management\Images\\User_login_img1.jpg')
render = ImageTk.PhotoImage(load)
img = Label(user,image = render)
img.place(x = 75,y =100)

("--------------------------------------------------- Login Button-----------------------------------------")

img13 = PhotoImage(file = "F:\Hotel Management\Images\\button.png")
btn = Button(user,image = img13,bd = 0,bg = "white",activebackground ='white',command = login)
btn.place(x=170,y=500)

x1 = Label(user,text = 'Username',font=("Tahoma",20,"bold"),bg = "white",fg = "black",bd = 2)
x1.place(x=30,y=350)
x2 = Label(user,text = 'Password',font=("Tahoma",20,"bold"),bg = 'white',fg = "black",bd = 2)
x2.place(x=30,y=420)

E1 = StringVar()
e1 = Entry(user,font=("Tahoma",20,"bold"),bg = "White",bd = 2,width=12,justify =LEFT,textvariable=E1)
e1.place(x=200,y=350)

E2 = StringVar()
e2 = Entry(user,font=("Tahoma",20,"bold"),bg = "White",bd = 2,width=12,show = "*",justify =LEFT,textvariable=E2)
e2.place(x=200,y=420)
