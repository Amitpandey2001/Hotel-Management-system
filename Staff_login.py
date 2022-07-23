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


      #(-----------------------------------------------------------------------------------------)

mydb = pymysql.connect(host = "localhost", user = "root",passwd = "1916Pr@th@m",database = "Hotel")
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


home = Tk()
home.title("Staff Login")
home.config(bg = 'white')
home.geometry("450x700+550+80")
home.resizable(0,0)


Staff = Label(home,text = "Staff Login",font=("Flexure",30,"bold"), background="white")
Staff.place(x=110, y=10)


def login():
    username = e1.get()
    password = e2.get()
    
    if (username=="" and password==""):
        messagebox.showwarning("ERROR !!","All fields are required")
    elif (username=="p" and password=="0"):
        messagebox.showinfo("Welcome !!","Login Successful")
        
        def desk():
            home.destroy()
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
            logo1 = Label(image = img)
            logo1.place(x=3,y=0)

            def hotel_status():
                global b_frame
                b_frame = Frame(desk,height=550,width=1260,bg='powder blue')
                b_frame.place(x=280,y=210+6+20+60+11)
                b_frame.pack_propagate(False)
                
                mycursor.execute("select count(Room_no) from Roomd")
                x = mycursor.fetchone()
                mycursor.execute("select count(Room_no) from Roomd where reserve_status = 'yes'")
                y = mycursor.fetchone()
                tor = x[0]
                rer = y[0]
                tos = 28
                avr = int(tor)-int(rer)
                avr = str(avr)
                hts = Label(b_frame,text='Hotel Status',font='msserif 15',fg='black',bg='gray91',height=1)

                
                                #------------inner frames of bottom frame-------------------------

                smf1 = Frame(b_frame,height=150,width=175,bg='white')
                tr = Label(smf1,text='Total Rooms:',fg='white',bg='cyan4',width=100,height=2,font='helvetica 15')
                tr.pack(side='top')
                smf1.pack_propagate(False)
                smf1.place(x=150,y=150)
                Label(smf1,text=tor,fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')

                smf2 = Frame(b_frame,height=150,width=175,bg='white')
                ar = Label(smf2,text='Available Rooms:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
                ar.pack(side='top')
                smf2.pack_propagate(False)
                smf2.place(x=350,y=150)
                Label(smf2,text=avr,fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')

                smf3 = Frame(b_frame,height=150,width=175,bg='white')
                tre = Label(smf3,text='Total reservations:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
                tre.pack(side='top')
                smf3.pack_propagate(False)
                smf3.place(x=550,y=150)
                Label(smf3,text = rer,fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')

                smf5 = Frame(b_frame,height=150,width=175,bg='white')
                ts = Label(smf5,text='Total Staff:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
                ts.pack(side='top')
                smf5.pack_propagate(False)
                smf5.place(x=750,y=150)
                Label(smf5,text=tos,fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')
                redf1 = Frame(b_frame,height=8,width=1080,bg='cyan4')

                smf6 = Frame(b_frame,height=150,width=175,bg='white')
                ts = Label(smf6,text='Under renovation:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
                ts.pack(side='top')
                smf6.pack_propagate(False)
                smf6.place(x=950,y=150)
                Label(smf6,text='5',fg='cyan4',bg='white',font='msserif 50').place(x=60,y=60)
                redf1 = Frame(b_frame,height=8,width=1080,bg='cyan4')

            img1 = PhotoImage(file = "F:\Hotel Management\Images\\hotelstatus.png")
            hotelstatus = Label(desk,text = "Hotel Status",bg ="black",fg="white",font=("Flexure",15,"bold"))
            hotelstatus.place(x=350,y=170)
            hotelstatus_bt = Button(desk,image = img1,bd = 0,bg = "#000000",activebackground ='#000000',command = hotel_status)
            hotelstatus_bt.place(x=360,y=203)

            ("--------------------------------- Check In -------------------------------------------")

            def reserves():
                b_frame = Frame(desk,height=550,width=1260,bg='cyan')
                b_frame.place(x=280,y=210+6+20+60+11)
                b_frame.pack_propagate(False)

                vline = Frame(b_frame,height=600,width=7,bg='black').place(x=800,y=0)

                Label(b_frame,text='Personal Information',font='msserif 15',bg='cyan',fg = "black").place(x=290,y=10)

                def calendar():
                    win= Tk()
                    win.title("Calendar")
                    win.geometry("200x250+1000+430")
                    win.resizable(0,0)
                    cal= DateEntry(win,date_patten="yy-mm-dd",width=16,bg="megenta3",fg='white',bd=2)
                    cal.pack(pady=20)
                    #Define Function to select the date
                    def get_date():
                        doa.delete(0,END)
                        x = doa.insert(0,cal.get_date())
                        win.destroy()
                    #Create a button to pick the date from the calendar
                    button= Button(win, text= "Select the Date", command= get_date)
                    button.place(x=60,y=220)
                    win.mainloop()

                fullN = StringVar()
                fn = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable = fullN,justify =LEFT)
                fn.place(x=30,y=50)
                fn.insert(0, 'Full Name *')

                Adh =StringVar()
                adhar = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable =Adh,justify =LEFT)
                adhar.place(x=450,y=50)
                adhar.insert(0, 'Adhar Number *')

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
                
                Label(b_frame,text='Reservation Information',font='msserif 15',bg='cyan',fg = 'black').place(x=290,y=200)

                NOP = StringVar()
                nop = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable =NOP,justify =LEFT)
                nop.place(x=30,y=250)
                nop.insert(0, "Number Of Persons *")

                DOA = StringVar()
                doa = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable =DOA,justify =LEFT)
                doa.place(x=290,y=285)
                doa.insert(0, "Date Of Arrival *")

                calendar = Button(b_frame,text='C',font=("COOPER BLACK",12,"bold"),bd = 0,bg = "black",fg='white',command = calendar)
                calendar.place(x=486,y=285)

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

                def on_entry_click1(event):
                        if fn.get() == 'Full Name *' :
                            fn.delete(0,END)
                            fn.insert(0,'')
                def on_entry_click2(event):
                        if adhar.get() == 'Adhar Number *' :
                            adhar.delete(0,END)
                            adhar.insert(0,'')
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
                                
                def on_exit1(event):
                        if fn.get()=='':
                            fn.insert(0,'Full Name *')
                def on_exit2(event):
                        if adhar.get()=='':
                            adhar.insert(0,'Adhar Number *')
                def on_exit4(event):
                        if cn.get()=='':
                                cn.insert(0,'Contact Number *')
                def on_exit5(event):
                        if em.get()=='':
                                em.insert(0,'Email *')
                def on_exit6(event):
                        if add.get()=='':
                                add.insert(0,"Guest's Address *")
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

                                
                fn.bind('<FocusIn>', on_entry_click1)
                adhar.bind('<FocusIn>', on_entry_click2)
                cn.bind('<FocusIn>', on_entry_click4)
                em.bind('<FocusIn>', on_entry_click5)
                add.bind('<FocusIn>', on_entry_click6)
                nop.bind('<FocusIn>', on_entry_click7)
                doa.bind('<FocusIn>', on_entry_click8)
                dpa.bind('<FocusIn>', on_entry_click9)
                rno.bind('<FocusIn>', on_entry_click10)
                vp.bind('<FocusIn>', on_entry_click11)
                
                fn.bind('<FocusOut>',on_exit1)
                adhar.bind('<FocusOut>',on_exit2)
                cn.bind('<FocusOut>',on_exit4)
                em.bind('<FocusOut>',on_exit5)
                add.bind('<FocusOut>',on_exit6)
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

                ##----------------------------------------------- Filter ------------------------------------------

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
            reserve = Label(desk,text = "Check-in",bg ="black",fg="white",font=("Flexure",15,"bold"))
            reserve.place(x=530,y=170)
            reserve_bt = Button(desk,image =img2,bd = 0,bg = "#000000",activebackground ='#000000',command=reserves)
            reserve_bt.place(x=520,y=203)

            ("--------------------------------- check-out -----------------------------------------")

            def check_out():
                b_frame = Frame(desk,height=550,width=1260,bg='salmon')
                b_frame.place(x=280,y=210+6+20+60+11)
                b_frame.pack_propagate(False)
                b_frame.tkraise()

                def search():
                    mycursor.execute ("SELECT * FROM check_in WHERE Alloted_room = '{}'".format(RNO.get()))
                    y = mycursor.fetchone()

                    fn.delete(0,END)
                    fn.insert(0,y[1])
                    doa.delete(0,END)
                    doa.insert(0,y[7])
                    da.delete(0,END)
                    da.insert(0,y[8])

                def calendar():
                    win= Tk()
                    win.title("Calendar")
                    win.geometry("200x250+1000+430")
                    win.resizable(0,0)
                    cal= DateEntry(win,date_patten="yy-mm-dd",width=16,bg="megenta3",fg='white',bd=2)
                    cal.pack(pady=20)
                    #Define Function to select the date
                    def get_date():
                        dod.delete(0,END)
                        x = dod.insert(0,cal.get_date())
                        win.destroy()
                    #Create a button to pick the date from the calendar
                    button= Button(win, text= "Select the Date", command= get_date)
                    button.place(x=60,y=220)
                    win.mainloop()

                def Datetime():
                    date1 = datetime.datetime.strptime(DOA.get(), "%Y-%m-%d").date()
                    date2 = datetime.datetime.strptime(DOD.get(), "%Y-%m-%d").date()
                    diff =  (date2 - date1).days
                    xyz = int(diff)
                    doh.delete(0,END)
                    doh.insert(0,xyz)

                    mycursor.execute("select price from roomd where Room_no = '{}'".format(rno.get()))
                    xd = mycursor.fetchone()

                    rent = (DOH.get())* xd[0]
                    rr.delete(0,END)
                    rr.insert(0,rent)

                    balance = RR.get() - DA.get()
                    ba.delete(0,END)
                    ba.insert(0,balance)

                def check_out_done():
                    try :
                        mycursor.execute(" create table Check_out (Sr_no int(50) AUTO_INCREMENT PRIMARY KEY,Alloted_room int(10),Name varchar(50),Date_Arrival date,Date_Departure date,No_dayshalt int(20),Room_Rent int(50),Deposit_Amount int(50),Balance_amount int(50))")  
                        mydb.commit()
                        print('You have sucessfully created your Table ')

                    except pymysql.err.OperationalError:
                        print('table already exist')

                    mycursor.execute("insert into Check_out (Alloted_room,Name,Date_Arrival,Date_Departure,No_dayshalt,Room_Rent,Deposit_Amount,Balance_amount)values({},'{}','{}','{}',{},{},{},{})".format(RNO.get(),fullN.get(),DOA.get(),DOD.get(),DOH.get(),RR.get(),DA.get(),BA.get()))
                    mydb.commit()

                    mycursor.execute("update roomd set reserve_status = 'no' where Room_no = {} ".format(RNO.get()))

                    mycursor.execute('Delete from check_in where Alloted_room = "{}"'.format(RNO.get()))
                    mydb.commit()

                mycursor.execute("select Alloted_room from check_in")
                y = mycursor.fetchall()
                a = []
                for i in range(len(y)):
                    a.append(y[i][0])

                RNO = StringVar()
                rno = ttk.Combobox(b_frame,font=("Flexure",16,"bold"),width=20,value = a,textvariable =RNO,justify =LEFT)
                rno.place(x=200,y=50)
                rno.insert(0, "Room Number *")

                fullN = StringVar()
                fn = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable = fullN,justify =LEFT)
                fn.place(x=30,y=120)
                fn.insert(0, 'Full Name *')

                DOA = StringVar()
                doa = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable =DOA,justify =LEFT)
                doa.place(x=30,y=180)
                doa.insert(0, "Date Of Arrival *")

                DOD = StringVar()
                dod = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable =DOD,justify =LEFT)
                dod.place(x=410,y=180)
                dod.insert(0, "Date Of Departure *")

                DOH =  IntVar()
                doh = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable =DOH,justify =LEFT)
                doh.place(x=30,y=240)
                doh.insert(0, "Days Of Halt *")

                RR = IntVar()
                rr = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable =RR,justify =LEFT)
                rr.place(x=410,y=240)
                rr.insert(0, "Room Rent *")

                DA = IntVar()
                da = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable = DA,justify =LEFT)
                da.place(x=410,y=120)
                da.insert(0, 'Deposite Amount *')

                BA = IntVar()
                ba = Entry(b_frame,font=("Flexure",14,"bold"),bg = "White",width=20,textvariable = BA,justify =LEFT)
                ba.place(x=30,y=300)
                ba.insert(0, 'Balance Amount *')


                def on_entry_click1(event):
                        if fn.get() == 'Full Name *' :
                            fn.delete(0,END)
                            fn.insert(0,'')
                def on_exit1(event):
                        if fn.get()=='':
                            fn.insert(0,'Full Name *')

                def on_entry_click2(event):
                        if rno.get() == 'Room Number *' :
                            rno.delete(0,END)
                            rno.insert(0,'')
                def on_exit2(event):
                        if rno.get()=='':
                            rno.insert(0,'Room Number *')

                def on_entry_click3(event):
                        if doa.get() == 'Date Of Arrival *' :
                            doa.delete(0,END)
                            doa.insert(0,'')
                def on_exit3(event):
                        if doa.get()=='':
                            doa.insert(0,'Date Of Arrival *')

                def on_entry_click4(event):
                        if dod.get() == 'Date Of Departure *' :
                            dod.delete(0,END)
                            dod.insert(0,'')
                def on_exit4(event):
                        if dod.get()=='':
                            dod.insert(0,'Date Of Departure *')

                def on_entry_click5(event):
                        if doh.get() == 'Days Of Halt *' :
                            doh.delete(0,END)
                            doh.insert(0,'')
                def on_exit5(event):
                        if doh.get()=='':
                            doh.insert(0,'Days Of Halt *')

                def on_entry_click6(event):
                        if doh.get() == 'Room Rent *' :
                            doh.delete(0,END)
                            doh.insert(0,'')
                def on_exit6(event):
                        if doh.get()=='':
                            doh.insert(0,'Room Rent *')

                def on_entry_click7(event):
                        if da.get() == 'Deposite Amount *' :
                            da.delete(0,END)
                            da.insert(0,'')
                def on_exit7(event):
                        if da.get()=='':
                            da.insert(0,'Deposite Amount *')

                def on_entry_click8(event):
                        if da.get() == 'Balance Amount *' :
                            da.delete(0,END)
                            da.insert(0,'')
                def on_exit8(event):
                        if da.get()=='':
                            da.insert(0,'Balance Amount *')

                fn.bind('<FocusIn>', on_entry_click1) 
                rno.bind('<FocusIn>', on_entry_click2)
                doa.bind('<FocusIn>', on_entry_click3)
                dod.bind('<FocusIn>', on_entry_click4)
                doh.bind('<FocusIn>', on_entry_click5)
                rr.bind('<FocusIn>', on_entry_click6)
                da.bind('<FocusIn>', on_entry_click7)
                ba.bind('<FocusIn>', on_entry_click8)
                
                fn.bind('<FocusOut>',on_exit1)
                rno.bind('<FocusOut>',on_exit2)
                doa.bind('<FocusOut>',on_exit3)
                dod.bind('<FocusOut>',on_exit4)
                doh.bind('<FocusOut>',on_exit5)
                rr.bind('<FocusOut>',on_exit6)
                da.bind('<FocusOut>',on_exit7)
                ba.bind('<FocusOut>',on_exit8)

                search = Button(b_frame,text='Search',font=("Flexure",12,"bold"),bd = 0,bg = "black",fg = 'white',command = search)
                search.place(x=470,y=50)

                calendar = Button(b_frame,text='C',font=("Flexure",12,"bold"),bd = 0,bg = "black",fg='white',command = calendar)
                calendar.place(x=620,y=180)

                done = Button(b_frame,text = 'Done',font=("Flexure",12,"bold"),bd = 0,bg = "black",fg = 'white',command = Datetime)
                done.place(x=650,y=180)

                done1 = Button(b_frame,text = 'Done',font=("Flexure",20,"bold"),bd = 0,bg = "black",fg = 'white',command = check_out_done)
                done1.place(x=600,y=370)              

            img3 = PhotoImage(file = "F:\Hotel Management\Images\\check-out1.png")
            check_out1 = Label(desk,text = "Check-out",bg ="black",fg="white",font=("Flexure",15,"bold"))
            check_out1.place(x=840,y=170)
            check_out_bt = Button(desk,image =img3,bd = 0,bg = "#000000",activebackground ='#000000',command =check_out)
            check_out_bt.place(x=840,y=203)

            ("--------------------------------- Rooms -----------------------------------------")

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

            img4 = PhotoImage(file = "F:\Hotel Management\Images\\rooms.png")
            room = Label(desk,text = "Room Info",bg ="black",fg="white",font=("Flexure",15,"bold"))
            room.place(x=680,y=170)
            room_bt = Button(desk,image = img4,bd = 0,bg = "#000000",activebackground ='#000000',command = rooms)
            room_bt.place(x=680,y=203)

            img7 = PhotoImage(file = "F:\Hotel Management\Images\\employee.png")
            emp = Label(desk,text = "Employees",bg ="black",fg="white",font=("Flexure",15,"bold"))
            emp.place(x=1020,y=170)
            emp_bt = Button(desk,image = img7,bd = 0,bg = "#000000",activebackground ='#000000')
            emp_bt.place(x=1020,y=203)

            ("--------------------------------- Show Guest list -------------------------------------------")

            def Show_guest_list():
                
                b_frame = Frame(desk,height=550,width=1260,bg='grey')
                b_frame.place(x=280,y=210+6+20+60+11)
                b_frame.pack_propagate(False)
                b_frame.tkraise()

                def search():
                    mycursor.execute ("SELECT * FROM tbt WHERE Name = '{}'".format(q.get()))
                    y = mycursor.fetchone()
                    
                    z2.insert(0,y[5])
                    z3.insert(0,y[7])
                    z4.insert(0,y[6])
                    z5.insert(0,y[8])
                    z2.config(state ='readonly')
                    z3.config(state ='readonly')
                    z4.config(state ='readonly')
                    z5.config(state ='readonly')

                mycursor.execute("select Name from tbt")
                y = mycursor.fetchall()
                a = []
                for i in range(len(y)):
                    a.append(y[i][0])
                    
                q = StringVar()
                z1 = Label(f1,text = ' Full Name - ',font=("Flexure",25,"bold"),bg = "wheat",fg = "black",bd = 2)
                z1.place(x=240,y=122)
                z1 = AutocompleteCombobox(f1,font=("Flexure",18,"bold"),width=24,justify =LEFT,completevalues = a,textvariable = q)
                z1.place(x=550,y=130)

                r = StringVar()
                z2 = Label(f1,text = 'Alloted Room - ',font=("Flexure",25,"bold"),bg = "wheat",fg = "black",bd = 2)
                z2.place(x=240,y=182)
                z2 = Entry(f1,font=("Flexure",18,"bold"),bg = "White",width=25,justify =LEFT,textvariable = r)
                z2.place(x=550,y=190)

                s = StringVar()
                z3 = Label(f1,text = 'Arrival Date - ',font=("Flexure",25,"bold"),bg = "wheat",fg = "black",bd = 2)
                z3.place(x=250,y=242)
                z3 = Entry(f1,font=("COOPER BLACK",18,"bold"),bg = "White",width=25,justify =LEFT,textvariable = s)
                z3.place(x=550,y=250)

                t = StringVar()
                z4 = Label(f1,text = 'Mobil Number - ',font=("Flexure",25,"bold"),bg = "wheat",fg = "black",bd = 2)
                z4.place(x=240,y=302)
                z4 = Entry(f1,font=("Flexure",18,"bold"),bg = "White",width=25,justify =LEFT,textvariable = t)
                z4.place(x=550,y=310)

                u = StringVar()
                z5 = Label(f1,text = 'Deposite Amount - ',font=("Flexure",25,"bold"),bg = "wheat",fg = "black",bd = 2)
                z5.place(x=220,y=362)
                z5 = Entry(f1,font=("Flexure",18,"bold"),bg = "White",width=25,justify =LEFT,textvariable = u)
                z5.place(x=550,y=370)

##                done = Button(f1,text = 'Done',font=("COOPER BLACK",20,"bold"),bd = 0,bg = "black",fg = 'white')
##                done.place(x=600,y=570)
                
                search = Button(f1,text='Search',font=("Flexure",15,"bold"),bd = 0,bg = "black",fg = 'white',command = search)
                search.place(x=940,y=130)

                clear = Button(f1,text='Clear',font=("Flexure",20,"bold"),bd = 0,bg = "black",fg = 'white',command = clear)
                clear.place(x=600,y=570)

            img6 = PhotoImage(file = "F:\Hotel Management\Images\\info1.png")
            information = Label(desk,text = "Guest Info",bg ="black",fg="white",font=("Flexure",15,"bold"))
            information.place(x=1220,y=170)
            information_bt = Button(desk,image = img6,bd = 0,bg = "#000000",activebackground ='#000000')
            information_bt.place(x=1220,y=203)

            ("---------------------------------------- Exit -----------------------------------------------")

            def exit():
                q = messagebox.askyesno("Exit","Do you really want to exit ?")
                if(q):
                    desk.destroy()
                    import Main_page

            img10 = PhotoImage(file = "F:\Hotel Management\Images\\exit1.png")
            exit1 = Label(desk,text = "Exit",bg ="black",fg="white",font=("Flexure",15,"bold"))
            exit1.place(x=1430,y=170)
            exit2 = Button(desk,image =img10,bd = 0,bg = "#000000",activebackground ='#000000',command = exit)
            exit2.place(x=1400,y=203)

            desk.mainloop()
        desk()
    else:
        messagebox.showwarning("ERROR !!","Invalid Username or Password")

("------------------------------------------------- Background --------------------------------------------")

load = Image.open('F:\Hotel Management\Images\\Staff_login_img.jpg')
render = ImageTk.PhotoImage(load)
img = Label(home,image = render)
img.place(x =75,y = 100)

("--------------------------------------------------- Login Button-----------------------------------------")

img13 = PhotoImage(file = "F:\Hotel Management\Images\\button.png")
btn = Button(home,image = img13,bd = 0,bg = "white",activebackground ='white',command = login)
btn.place(x=170,y=500)
    
x1 = Label(home,text = 'Username',font=("Tahoma",20,"bold"),bg = "White",fg = "black",bd = 2)
x1.place(x=30,y=350)
x2 = Label(home,text = 'Password',font=("Tahoma",20,"bold"),bg = 'white',fg = "black",bd = 2)
x2.place(x=30,y=420)

e1 = Entry(home,font=("Tahoma",20,"bold"),bg = "White",bd = 2,width=12,justify =LEFT)
e1.place(x=200,y=350)
e2 = Entry(home,font=("Tahoma",20,"bold"),bg = "White",bd = 2,width=12,show="*",justify =LEFT)
e2.place(x=200,y=420)

("----------------------------------------------------------------------------------------------------------")

home.mainloop()
