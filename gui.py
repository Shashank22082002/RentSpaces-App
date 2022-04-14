from tkinter import *
from tkcalendar import *
import mysql.connector
import datetime

from tkinter import messagebox
mydb = mysql.connector.connect(host="blymopi5ojrr9mnzhwzg-mysql.services.clever-cloud.com", user="urvbarszie8v9emk", passwd="yEg3905cdju8VaG2D94g")
mycursor = mydb.cursor(buffered=True)
mycursor.execute("use blymopi5ojrr9mnzhwzg")

mycursor.execute("show tables")

for i in mycursor:
    print(i)
mycursor.execute('''SELECT * FROM office''')
info = mycursor.fetchall()
for i in info:
    print(i)

# gui
def welcomePage():
    root = Tk()
    root.title("Welcome to ®RentSpaces ●")
    frame = LabelFrame(root, padx=100, pady=100)
    frame.pack()
    lable = Label(frame, text="Please Sign-up or Login", pady=40).grid(row=0, column=3)
    def signupbtn():
        root.destroy()
        signuppge()

    def loginbtn():
        root.destroy()
        loginpge()
    login = Button(frame, text="Login", command=loginbtn).grid(row=5, column=0)
    signup = Button(frame, text="Sign-up", command=signupbtn).grid(row=5, column=8)
    root.mainloop()

#signup page
# page functions
def signuppge():
    signuppg = Tk()
    signuppg.title("®RentSpaces ●")
    frame = LabelFrame(signuppg, padx=100, pady=100)
    frame.pack()
    lable = Label(frame, text="Sign-up", fg="white", bg="black", padx=15, pady=15).grid(row=0, column=4)
    e = Entry(frame, width=35, borderwidth=5)
    e.grid(row=1, column=3, columnspan=3, padx=10, pady=15)
    e.insert(0, "Name")
    e1 = Entry(frame, width=35, borderwidth=5)
    e1.grid(row=2, column=3, columnspan=3, padx=10, pady=15)
    e1.insert(0, "Email")
    e2 = Entry(frame, width=35, borderwidth=5)
    e2.grid(row=3, column=3, columnspan=3, padx=10, pady=15)
    e2.insert(0, "PhoneNo")
    e3 = Entry(frame, width=35, borderwidth=5)
    e3.grid(row=4, column=3, columnspan=3, padx=10, pady=15)
    e3.insert(0, "Enter a Password")

    def RetBtn():
        signuppg.destroy()
        welcomePage()

    def callupdate():
        # sql query
        name = e.get()
        email = e1.get()
        phoneno = e2.get()
        password = e3.get()
        mycursor.execute('''select case when exists(select email from customer where email=%s or phoneno=%s ) 
                            then 0 else 1 end as val''',(email, phoneno))
        sql_query = mycursor.fetchall()
        sql_query = sql_query[0][0]
        print(sql_query)
        if(sql_query==0):
            messagebox.showinfo("Error", "Email or Phone_no already in use,\nplease use another")
        else:
            mycursor.execute("insert into customer(name,email,phoneno,password) values(%s,%s,%s,%s)", (name, email, phoneno, password))
            mydb.commit()
            mycursor.execute('''select max(customerid) from customer''')
            custId = mycursor.fetchall()
            custId = custId[0][0]
            signuppg.destroy()
            main_page(custId)

    signup1 = Button(frame, text="Sign-up", command=callupdate).grid(row=5, column=4, pady=30)
    RetBt = Button(frame, text="Go-Back", command=RetBtn).grid(row=7, column=4, pady = 10)

#login_page
def loginpge():
    loginpg = Tk()
    loginpg.title("Login To RentSpaces")
    frame = LabelFrame(loginpg, padx=100, pady=100)
    frame.pack()
    lable = Label(frame, text="Login", fg="white", bg="Black", padx=15, pady=15).grid(row=0, column=4)
    e1 = Entry(frame, width=35, borderwidth=5)
    e1.grid(row=2, column=3, columnspan=3, padx=10, pady=15)
    e1.insert(0, "Enter your Email")
    e2 = Entry(frame, width=35, borderwidth=5)
    e2.grid(row=3, column=3, columnspan=3, padx=10, pady=15)
    e2.insert(0, "Enter your Password")

    def callchk():
        email = e1.get()
        password = e2.get()
        mycursor.execute('''select case when (%s in (select distinct email from customer) and 
                                    %s in (select distinct password from customer)) then 1 else 0 end as val''',
                                   (email,password))
        sql_qry = mycursor.fetchone()
        if (sql_qry[0] == 0):
            messagebox.showinfo("Error", "Invalid Credentials! \n Please Try Again...")
        else:
            loginpg.destroy()
            mycursor.execute('''select customerid from customer where email=%s and password=%s''',(email,password))
            custId = mycursor.fetchall()
            custId = custId[0][0]
            main_page(custId)

    login1 = Button(frame, text="Login", command=callchk).grid(row=5, column=4, pady=30)

def main_page(custID):
    main_page = Tk()
    main_page.title("®RentSpaces ●")##try inserting name in title
    frame = LabelFrame(main_page, padx=100, pady=100)
    lable = Label(frame, text="Hello Customer!!\nGreetings of the Day ", pady=30).grid(row=0, column=5)
    frame.pack()
    def Returnbtn():
        main_page.destroy()
        ReturnPage(custID)

    def Rentbtn():
        main_page.destroy()
        RentPage(custID)

    def ViewMoney():
        mycursor.execute('''SELECT balance from customer where customerid = %s''',(custID,))
        mon = mycursor.fetchall()
        st = "Your Current Balance is: "+ str(mon[0][0])
        messagebox.showinfo("Balance",st)
    def AddMoney(custID):
        main_page.destroy()
        AddBalancePage(custID)

    def ViewMessage():
        mycursor.execute('''SELECT messages from customer where customerid = %s''',(custID,))
        s = mycursor.fetchall()[0][0]
        messagebox.showinfo("Messages",s)

    def RetBtn():
        main_page.destroy()
        welcomePage()

    ViewMessage = Button(frame, text="View Messages", command= ViewMessage).grid(row = 1,column = 5,pady = 10)
    ViewMoney = Button(frame, text="View Balance", command=ViewMoney).grid(row=3,column=0)
    AddMn = Button(frame, text="Add Balance", command = lambda : AddMoney(custID)).grid(row=3, column=10)
    lab = Label(frame,text="                                                       ").grid(row=4,column = 5)
    Return = Button(frame, text="Return Car", command=Returnbtn).grid(row=5, column=0)
    Rent = Button(frame, text="Rent Car", command=Rentbtn).grid(row=5, column=10)

    RetBt = Button(frame, text = "Go Back", command=RetBtn).grid(row=7, column = 5, pady = 10)

    main_page.mainloop()

def AddBalancePage(custID):
    AddBalancePage = Tk()
    AddBalancePage.title("Accounts Name")
    frame = LabelFrame(AddBalancePage,padx=100 ,pady = 100)
    frame.pack()
    lable = Label(frame,text="View balance",pady=30,padx=30).grid(row=3,column=0)

    def ViewMoney():
        mycursor.execute('''SELECT balance from customer where customerid=%s''',(custID,))
        mon = mycursor.fetchall()
        st = "Your Current Balance is: "+ str(mon[0][0])
        messagebox.showinfo("Balance",st)

    ViewMoney = Button(frame, text="View Balance", command=ViewMoney).grid(row=1, column=2)
    lable = Label(frame, text="Enter Balance", pady=30).grid(row=3, column=0)
    e2 = Entry(frame, width=30, borderwidth=5)
    e2.grid(row=3, column=3)
    e2.insert(0, "amount")
    def Add(custID):
        mycursor.execute('''UPDATe customer SET balance = balance + %s where customerid = %s''',(e2.get(), custID))
        mydb.commit()
        messagebox.showinfo("Success", "Updated Balance Successfully")

    AddMoney = Button(frame, text="Add Balance", command=lambda: Add(custID)).grid(row=5, column=2)
    def RetBut():
        AddBalancePage.destroy()
        main_page(custID)
    RetButton = Button(frame, text="Return back", command =RetBut).grid(row=10, column=2, pady=10)

#RentPage
def RentPage(custID):

    RentPage = Tk()
    RentPage.title("®RentSpaces ●")
    frame = LabelFrame(RentPage, padx=100, pady=50)
    mycursor.execute('''SELECT status from customer where customerid = %s''',(custID,))
    print(custID)
    inf = mycursor.fetchall()[0][0]

    def RetBut():
        RentPage.destroy()
        main_page(custID)

    if(inf==1):
        messagebox.showinfo("Rentspaces","Sorry! You already have a Booking")
        RetBut()

    RetButton = Button(frame, text="Return back", command=RetBut).grid(row=7, column=4, pady=10)
    lable = Label(frame, text="Rent Your Favourite Roadie!!\n ", pady=30).grid(row=0, column=4)
    l1 = Label(RentPage, text="Select City")
    l1.pack()
    def show():
        myLabel = Label(RentPage, text = clicked1.get()).pack()

    clicked1 = StringVar()
    clicked1.set("Select City")
    # mycursor.execute('''SELECT office_city from office''')
    drop = OptionMenu(RentPage, clicked1, "Jaipur", "Delhi", "Pilani", "Goa", "Hyderabad", "Mumbai", "Kolkata")
    drop.pack()
    l1 = Label(RentPage, text="Select Car Type")
    city = clicked1.get()
    l1.pack()

    def show():
        myLabel = Label(RentPage, text = clicked2.get()).pack()

    clicked2 = StringVar()
    clicked2.set("Car Type")

    drop = OptionMenu(RentPage, clicked2, "Prime", "Sedan", "Sports", "Van", "Truck", "Mini")
    drop.pack()
    frame.pack()

    def show():
        frame1 = Frame(RentPage, padx=80, pady=10)
        city = clicked1.get()
        type = clicked2.get()
        mycursor.execute('''SELECT ct.car_type, c.car_name,ct.price_per_day, c.car_ID, c.status from car c
                            join carType ct on ct.type_ID = c.type_ID 
                            join office o on o.office_ID = ct.office_ID
                            where ct.car_type = %s and o.office_city = %s
                            ''',(type, city))
        info = mycursor.fetchall()

        ct = 0
        r = IntVar()
        for i in info:
            print(i)
            if(i[4]):
                availability = "Not - Available"
            else:
                availability = "Available"
            s = "Car-type = "+str(i[0])+"  Car-Name = "+str(i[1])+"  Price-per-Day = "+str(i[2])+ " Availability: "+availability
            Radiobutton(frame1,text=s,variable=r,value=i[3]).grid(row=ct, column=0)

            a = i[3]
            print(a*10)

            # if(i[4]):
            #     txt = "Request" + str(ct)
            #     Req = Button(frame1, text=txt, command = lambda name = txt: RequestBtn(txt, custID)).grid(row = ct, column = 1)
            # else:
            #     txt = "Book" + str(ct)
            #     Book = Button(frame1, text=txt, command = lambda name = txt: BookBtn(txt,custID)).grid(row = ct, column=1)

            ct = ct+1

        def clicked(car_ID, custID):
            mycursor.execute('''SELECT status from car where car_ID = %s''', (car_ID,))
            if (mycursor.fetchone()[0]):
                RequestBtn(car_ID, custID)
            else:
                BookBtn(car_ID, custID)

        def BookBtn(a, custID):
            RentPage.destroy()
            BookPage(a, custID)

        def RequestBtn(a, custID):
            res = messagebox.askyesno("Request", "Add Request for booking this car")
            print(res)
            if res:
                mycursor.execute('''SELECT count(request_ID) from listings where customer_ID=%s''', (custID,))
                if (mycursor.fetchone()[0] != 0):
                    messagebox.showinfo("Error", "You already have a request")
                    RetBut()

                mycursor.execute('''INSERT into listings(car_ID,customer_ID) values(%s,%s)''', (a, custID))
                mycursor.execute('''Select requests from car where car_ID = %s''', (a,))
                new_requests = mycursor.fetchone()[0]+1
                mycursor.execute('''Update car
                                    set requests = %s
                                    where car_ID = %s''', (new_requests, a))
                mydb.commit()
                messagebox.showinfo("Success!", "Request added for car. You will be informed when the car is free!")

        b = Button(text="Book/Request",font="50",command=lambda:clicked(r.get(),custID)).pack()
        frame1.pack()
        print(city)
        print(type)



    myButton = Button(RentPage, text="Proceed", command = show).pack()


def BookPage(a,custID):
    BookPage = Tk()
    BookPage.title("Booking Page")
    BookPage.geometry("500x800")
    frame = LabelFrame(BookPage, padx=100, pady=100).pack()
    # lable = Label(frame, text="Book Your Own Space\n ", pady=3)
    lable = Label(frame, text="Enter Booking Details\n ", pady=2)
    lable.pack()

    # l1 = Label(frame, text = "Enter Date", pady = 6)
    # l1.pack()
    cal = Calendar(BookPage, selectmode="day", date_pattern='yyyy-mm-dd',year=2022, month=4, day=10)
    cal.pack(pady=10)

    def grab_date():
        my_label.config(text=cal.get_date())

    myButton = Button(BookPage, text="Enter Date", command=grab_date)
    myButton.pack(pady=15)
    my_label = Label(BookPage, text="")
    my_label.pack(pady=20)

    my_label2 = Label(BookPage, text="Days Required: ")
    my_label2.pack(pady=25)

    e = Entry(BookPage)
    e.pack()

    def ConfirmBooking():
        days = e.get()
        date = cal.get_date()
        print(custID)
        print(a)
        print(date)

        mycursor.execute('''SELECT ct.price_per_day from carType ct
        join car c on c.type_ID = ct.type_ID
        where c.car_ID = %s''',(a,))

        adv = mycursor.fetchone()[0]*((int)(days))/2

        mycursor.execute('''SELECT balance from customer where customerid = %s''',(custID,))

        bal = mycursor.fetchone()[0]

        if(bal<adv):
            messagebox.showinfo("Error!", "Insufficient Balance to make advance Payments!!")
            RetBut()

        mycursor.execute('''SELECT car_id, customer_ID from listings where car_ID = %s
        order by date_time ''',(a,))
        ans = mycursor.fetchall()
        if(len(ans)!=0):
            mycursor.execute('''delete from listings where car_ID=%s''', (ans[0][0],))
            if(ans[0][1]==custID):
                mycursor.execute('''Update car
                set requests = requests - 1 where
                car_ID = %s''',(ans[0][0],))
                mydb.commit()

        mess = "Enjoy your Ride!"
        mycursor.execute('''UPDATE customer set messages = %s where customerid = %s''',(mess,custID))
        mycursor.execute('''insert into reservation (customerid,car_ID,issue_date,req_days) 
        values(%s,%s,%s,%s)''', (custID, a, date, days))
        mycursor.execute('''update car
        set status = 1 where car_ID = %s''', (a,))
        mycursor.execute('''update customer
        set status = 1 where customerid = %s''', (custID,))
        mydb.commit()
        ss = "Booking Confirmed.\n Advanced Payment=" + str(adv)
        messagebox.showinfo("Success", ss)
        BookPage.destroy()
        main_page(custID)

    ConfirmBook = Button(BookPage, text="Confirm Booking", command=ConfirmBooking)
    ConfirmBook.pack(pady=20)

    def RetBut():
        BookPage.destroy()
        main_page(custID)

    Ret = Button(frame,text="Return",command=RetBut).pack()


def ReturnPage(custID):
    ReturnPage = Tk()
    ReturnPage.title("®RentSpaces ●")
    ReturnPage.geometry("600x400")
    frame = LabelFrame(ReturnPage, padx=100, pady=100)
    frame.pack()
    mycursor.execute('''SELECT c.car_name,c.car_ID, r.issue_date, date_add(r.issue_date, INTERVAL r.req_days day) as 'due-date' from reservation r
                        join car c on c.car_ID=r.car_ID
                        where r.customerid = %s;''',(custID,))
    sql1_qry = mycursor.fetchall()
    print(sql1_qry)
    def generateBill():
        print("bill generated!")
        mycursor.execute('''SELECT ct.price_per_day,r.issue_date,ct.tank_Capacity,r.req_days from reservation r
                            join car c on c.car_ID=r.car_ID
                            join carType ct on ct.type_ID=c.type_ID 
                            where r.customerid = %s''', (custID,))
        sql_qry = mycursor.fetchall()

        def cost():
            mycursor.execute('''select current_date''')
            curr_date = mycursor.fetchone()[0]
            print(curr_date)

            # d1 = datetime.datetime.strptime(curr_date, '%Y-%m-%d')
            # d2 = datetime.datetime.strptime(sql_qry[0][0], '%Y:%m:%d:%H:%M:%S')
            # diff = (d2 - d1).total_seconds() / 60
            mycursor.execute('''select ((datediff(%s,%s)-%s/2) * %s) + ((%s-%s)*95)''',(curr_date, sql_qry[0][1], sql_qry[0][3], sql_qry[0][0], sql_qry[0][2], e1.get()))
            val = mycursor.fetchone()[0]
            print(val)
            sr = "Total  cost is: " + str(val)
            lab = Label(frame, text=sr).pack(pady=30)
            def payCharges(val):
                mycursor.execute('''SELECT balance from customer where customerid = %s''', (custID,))
                print(val)
                print("!!!")
                bal = mycursor.fetchone()[0]
                if (bal < val):
                    messagebox.showinfo("Error", "Insuffient Balance!'\n' Please add Balance")
                    ReturnBtn(custID)
                else:
                    new_bal = (bal - val)
                    mycursor.execute('''UPDATE customer set balance = %s
                                                        where customerid = %s
                                                        ''', (new_bal, custID))
                    mycursor.execute('''UPDATE customer set status = 0
                    where customerid = %s''',(custID, ))

                    ss = "Book Your Own Space!"
                    mycursor.execute('''UPDATE customer set messages = %s where customerid = %s''',(ss , custID))
                    mycursor.execute('''DELETE FROM reservation 
                                    where customerid = %s''',(custID,))
                    # set car status
                    mycursor.execute('''Update car
                    set status = 0 where car_ID=%s ''',(sql1_qry[0][1],))

                    #check for any earlier listing of the car
                    mycursor.execute('''select count(request_ID) from listings where car_ID=%s''',(sql1_qry[0][1],))
                    if(mycursor.fetchone()[0]!=0):
                        mycursor.execute('''SELECT customer_ID from listings where car_ID=%s order by date_time''',(sql1_qry[0][1],))
                        mesa = "Your Car is now available for booking,\n Order Now!!"
                        c_id = mycursor.fetchone()[0]
                        mycursor.execute('''UPDATE customer
                        set messages = %s where customerid = %s''',(mesa,c_id))

                    mydb.commit()
                    messagebox.showinfo("Success", "Transaction Successful!!")
                    ReturnBtn(custID)
            pay = Button(frame, text="Pay", command=lambda: payCharges(val)).pack()

        bill = Button(frame, text="Calculate Cost", command=cost).pack()
        #giving error when no query is there--fix
    lb1 = Label(frame, text="Enter Tank Gauge reading in Liters").pack()
    e1 = Entry(frame, width=10, borderwidth=5)
    e1.pack()
    if (len(sql1_qry)==0):
        messagebox.showinfo("Error", "No Booking Found! \n")
        ReturnPage.destroy()
        main_page(custID)
    else:
        s = "Car: "+str(sql1_qry[0][0])+"\nIssue-Date: "+str(sql1_qry[0][2])+"\nDue-Date: "+str(sql1_qry[0][3])
        l1 = Label(frame,text=s).pack(pady=10)
        btn2 = Button(ReturnPage,text="Confirm Return Advance to Payment", command=generateBill).pack(pady=30)

    def ReturnBtn(custID):
        ReturnPage.destroy()
        main_page(custID)
    btn1 = Button(ReturnPage, text="Return", command=lambda: ReturnBtn(custID)).pack(pady=20)


welcomePage()