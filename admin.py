from tkinter import *
import mysql.connector
from tkinter import messagebox

mydb = mysql.connector.connect(host="blymopi5ojrr9mnzhwzg-mysql.services.clever-cloud.com", user="urvbarszie8v9emk", passwd="yEg3905cdju8VaG2D94g")
mycursor = mydb.cursor(buffered=True)
mycursor.execute("use blymopi5ojrr9mnzhwzg")

def welcomePage():
    root = Tk()
    root.title("Welcome to RentSpaces")
    frame = LabelFrame(root, padx=100, pady=100)
    frame.pack()

    def addOffice():
        root.destroy()
        OfficePage()

    def addCarType():
        root.destroy()
        CarTypePage()

    def addCar():
        root.destroy()
        CarPage()

    l1 = Label(frame, text="Admin Page").grid(row = 3,column=5, pady = 40)
    Off = Button(frame, text="Add new Office", command=addOffice).grid(row=5, column=0,padx=10,pady=10)
    Ct = Button(frame, text="Add new Car-type", command=addCarType).grid(row=5, column=5,padx=10,pady=10)
    Cr = Button(frame, text="Add New Car", command = addCar).grid(row=5, column=10,padx=10,pady=10)
    root.mainloop()

#add a new office
def OfficePage():
    off = Tk()
    off.title("Add New Office")
    frame = LabelFrame(off, padx=100,pady = 50)
    frame.pack()

    e1 = Entry(frame, width=35, borderwidth=5)
    e1.grid(row=2, column=3, columnspan=3, padx=10, pady=15)
    e1.insert(0, "Enter Office City")

    def callchk1():
        city_name = e1.get()
        mycursor.execute('''select case when exists(select office_city from office where office_city=%s)
                                    then 0 else 1 end as val''', (city_name,))
        sql_query = mycursor.fetchall()
        sql_query = sql_query[0][0]

        if (sql_query == 0):
            messagebox.showinfo("Error", "This Office already exists\n")

        else:
            mycursor.execute('''insert into office(office_city) values(%s)''', (city_name,))
            mydb.commit()
            messagebox.showinfo("Success", "Office Added Successfuly!")
        off.destroy()
        welcomePage()

    def ret():
        off.destroy()
        welcomePage()

    add = Button(off, text="add", command=callchk1)
    add.pack(pady=10)
    back = Button(off, text="Return", command=ret)
    back.pack()

# add a new Car Type
def CarTypePage():
    ctp = Tk()
    ctp.title("Car Type")
    frame = LabelFrame(ctp, padx=100,pady=100 )
    frame.pack()
    l1 = Label(frame,text="Add A new Car Type!").grid(row = 0,column=5,pady=20)

    # select city
    l1 = Label(frame, text="Select City")
    l1.grid(row=2,column = 4,pady=10)

    clicked1 = StringVar()
    clicked1.set("Select City")
    # mycursor.execute('''SELECT office_city from office''')
    drop = OptionMenu(frame, clicked1, "Jaipur", "Delhi", "Pilani", "Goa", "Hyderabad", "Mumbai", "Kolkata")
    drop.grid(row = 2,column=6,pady=10)

    # enter car Type Name
    e1 = Entry(frame,width=35,borderwidth=5)
    e1.grid(row=4,column=5,columnspan=3,padx=10,pady=15)
    e1.insert(0,"Car-type Name")

    e2 = Entry(frame, width=35, borderwidth=5)
    e2.grid(row=6, column=5, columnspan=3, pady=15)
    e2.insert(0,"Price-Per-day")

    e3 = Entry(frame, width=35, borderwidth=5)
    e3.grid(row=8, column=5, columnspan=3, pady=15)
    e3.insert(0,"Tank-Capacity")

    def ret():
        ctp.destroy()
        welcomePage()

    def callchk1():
        # complete
        mycursor.execute('''select office_id from office where office_city=%s''',(clicked1.get(),))
        oid = mycursor.fetchall()[0][0]
        mycursor.execute('''insert into carType(office_id,car_type,price_per_day,tank_capacity) values(%s,%s,%s,%s)''',(oid, e1.get(),e2.get() ,e3.get()))
        Label(frame, text="Inserting...").grid(row = 12,column=3)
        mydb.commit()
        ctp.destroy()
        welcomePage()

    add = Button(frame,text="add",command=callchk1)
    add.grid(row=14,column = 5)

    back = Button(frame,text="Return",command=ret)
    back.grid(row = 16,column = 5, pady = 10)

# add new Car
def CarPage():
    cr = Tk()
    cr.title("Add Car")
    frame = LabelFrame(cr, padx=50, pady=50)
    frame.pack()

    l1 = Label(cr, text="Select City")
    l1.pack()

    clicked1 = StringVar()
    clicked1.set("Select City")
    # mycursor.execute('''SELECT office_city from office''')
    # this field is still static
    drop = OptionMenu(cr, clicked1, "Jaipur", "Delhi", "Pilani", "Goa", "Hyderabad", "Mumbai", "Kolkata")
    drop.pack()
    l1 = Label(cr, text="Select Car Type")
    l1.pack(pady=10)
    city = clicked1.get()

    def show():
        myLabel = Label(cr, text=clicked2.get()).pack()

    clicked2 = StringVar()
    clicked2.set("Car Type")

    drop = OptionMenu(cr, clicked2, "Prime", "Sedan", "Sports", "Van", "Truck", "Mini")
    drop.pack()
    carT = clicked2.get()
    frame.pack()
    ## select office and Type
    e1 = Entry(frame, width=35, borderwidth=5)
    e1.grid(row=2, column=3, columnspan=3, padx=10, pady=15)
    e1.insert(0,"Name")

    def ret():
        cr.destroy()
        welcomePage()

    def callchk1():
        name = e1.get()
        mycursor.execute('''SELECT ct.type_ID from carType ct 
        join office o on o.office_ID = ct.office_ID
        where o.office_city = %s and ct.car_Type = %s''',(clicked1.get(),clicked2.get()))
        print(clicked1.get())
        tid = mycursor.fetchone()[0]
        mycursor.execute('''insert into car(car_name,type_ID) values(%s,%s)''',(e1.get(),tid))
        Label(cr, text="Inserting...").pack()
        mydb.commit()
        cr.destroy()
        welcomePage()

    add = Button(cr,text="add",command=callchk1)
    add.pack(pady = 10)
    back = Button(cr,text="Return",command = ret)
    back.pack(pady = 10)

welcomePage()