# importing tkinter
import datetime
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

from PIL import Image, ImageTk
import pymysql
from tkcalendar import *
from datetime import *

# Class connection to connect with database

class connection:
    con = pymysql.connect(host="localhost", user="root", password="", database="taxibooking")
    cursor = con.cursor()

# Customer Interface class

class Customer_Interface:
    def __init__(self, root, name, Reg_ID):
        self.root = root
        self.root.geometry("1920x1080")  # Dimensions
        self.root.title("Welcome Customer")
        self.test = ImageTk.PhotoImage(file="Images\\CustomerWin.png") # Image Load

        # Current Date from Date Time

        now = datetime.now()
        self.current_year = now.year
        self.current_month = now.month
        self.current_day = now.day
        self.Customer_ID = Reg_ID

        # Creating Canvas to write transparent texts

        Label1 = Canvas(self.root)
        Label1.create_image(650, 300, image=self.test)
        Label1.create_text(1000, 50, text="WELCOME " + str(name), fill="yellow", font=("times new roman", 29, "bold"))
        Label1.create_text(1000, 80, text="Please Enter the following details for taxi booking", fill="Yellow",
                           font=("times new roman", 18, "bold"))
        # Label1.create_text()

        Label1.create_text(830, 120, text="Pickup Location", fill="yellow",
                           font=("times new roman", 24, "bold"))

        # Text variable to store data

        self.var_pickup = StringVar()
        self.pickup_txt = Entry(root, font=("times new roman", 18), fg="black", bg="white",
                                textvariable=self.var_pickup)
        self.pickup_txt.place(x=955, y=105, width=220, height=30)

        Label1.create_text(800, 160, text="Destination Location", fill="yellow",
                           font=("times new roman", 24, "bold"))

        # Text variable to store data

        self.var_destination = StringVar()
        self.destination_txt = Entry(root, font=("times new roman", 18), fg="black", bg="white",
                                     textvariable=self.var_destination)
        self.destination_txt.place(x=955, y=145, width=220, height=30)

        Label1.create_text(860, 200, text="Choose Date", fill="yellow",
                           font=("times new roman", 24, "bold"))

        # Text variable to store data

        self.var_cal2 = StringVar()
        self.cal2 = DateEntry(root, width=25, year=self.current_year, month=self.current_month, day=self.current_day,
                              height=400,
                              background='yellow', foreground='black', borderwidth=2,
                              font=("times new roman", 12, "bold"), textvariable=self.var_cal2)
        self.cal2.place(x=955, y=190)

        Label1.create_text(860, 240, text="Choose Time", fill="yellow",
                           font=("times new roman", 24, "bold"))

        value = str(datetime.today().strftime("%I:%M %p")) # Shows Current Time

        # self.current_hour = now.hour
        # print(self.current_hour)
        self.current_hour = value[0:2]
        self.current_time = value[6:8]
        print(self.current_time)
        print(type(self.current_time))
        self.var_hour = StringVar()
        self.var_hour.set(self.current_hour)  # Sets the current time to Spinbox
        self.spinbox = tkinter.Spinbox(root, from_=1, to=12, width=3, font=("times new roman", 14, "bold"),
                                       textvariable=self.var_hour)
        self.spinbox.place(x=955, y=230)

        self.current_minute = now.minute
        print(self.current_minute)
        # print(type(current_minute))
        self.var_minutes = StringVar()
        self.var_minutes.set(self.current_minute)
        self.spinbox2 = tkinter.Spinbox(root, from_=0, to=59, width=3, font=("times new roman", 14, "bold"),
                                        textvariable=self.var_minutes)
        self.spinbox2.place(x=1020, y=230)

        # x = datetime
        # AM_PM = str(x.strftime("%p"))
        # print(AM_PM)
        Label1.create_text(1010, 240, text=":", fill="yellow",
                           font=("times new roman", 24, "bold"))
        am_pm = ["AM", "PM"]

        # Text variable to store data

        self.var_time = StringVar()
        self.var_time.set(str(self.current_time))
        self.spinbox3 = tkinter.Spinbox(root, values=am_pm, width=3, font=("times new roman", 14, "bold"),
                                        textvariable=self.var_time)
        self.spinbox3.place(x=1080, y=230)

        # ---Buttons---

        self.book_btn = Button(root, text="BOOK", bg="#32CD32", fg="white",
                               font=("times new roman", 15, "bold"), cursor="hand2", command=self.insertData)
        self.book_btn.place(x=1050, y=270, width=200)

        self.check_booking_btn = Button(root, text="VIEW BOOKING", bg="#32CD32", fg="white",
                                        font=("times new roman", 15, "bold"), cursor="hand2",
                                        command=self.CheckingBooking)
        self.check_booking_btn.place(x=1050, y=320, width=200)

        self.login_btn = Button(root, text="Back", bg="red", fg="white",
                                font=("times new roman", 15, "bold"), cursor="hand2", command=self.back)
        self.login_btn.place(x=1050, y=420, width=200)

        self.login_btn = Button(root, text="CANCEL BOOKING", bg="red", fg="white",
                                font=("times new roman", 15, "bold"), cursor="hand2", command=self.selectValues)
        self.login_btn.place(x=1050, y=370, width=200)

        Label1.pack(fill="both", expand=True)  # Packing values

    def CheckingBooking(self):

        # This code would take value from two different tables and insert in treeview
        # by creating two lists. This was unnecessary as a simple SQL code could have been
        # written. Hence it is commented.

        '''
        conn = connection.cursor
        conn.execute("select * from booking_information where Customer_ID = %s", self.Customer_ID)
        value = [i[0:7] for i in conn.fetchall()]
        Driver_ID = []
        Booking_Details = []
        for i in value:
            Booking_Details.append(i[1:5])
            # Booking_Details.append(i[1])
            # Booking_Details.append(i[2])
            # Booking_Details.append(i[3])
            # Booking_Details.append(i[4])
            # print(i[1:5])
            Driver_ID.append(i[6])
        # print(Driver_ID)
        print(Booking_Details)
        conn2 = connection.cursor
        value2 = []
        for j in Driver_ID:
            conn2.execute(
                "select Driver_Name, Driver_Telephone, License_Plate, Car_Model from driver_information where "
                "Driver_ID = %s", j)
            value2.append([i[0:4] for i in conn.fetchall()])
        print(value2)
        new_list = (','.join(str(a)for a in value2))
        print(new_list)
        '''
        # getting value from the SQL Query
        self.conn = connection
        self.conn.cursor.execute(
            "select bi.Date, bi.Time , bi.Pickup_Location,bi.Dropoff_Location, di.Driver_Name, "
            "di.Driver_Telephone, "
            "di.License_Plate, di.Car_Model from booking_information bi join driver_information di on "
            "bi.Driver_ID = "
            "di.Driver_ID where bi.Customer_ID = %s",
            self.Customer_ID)
        value = [i[0:8] for i in self.conn.cursor.fetchall()]
        print(value)
        # Total_Information = Booking_Details + value2
        # print(Total_Information

        # Creating tree View

        self.tv = Treeview(self.root, columns=(1, 2, 3, 4, 5, 6, 7, 8), show='headings', height=8)
        self.tv.place(x=280, y=450)

        self.tv.heading(1, text="Date")
        self.tv.column(1, width=60, anchor=CENTER)

        self.tv.heading(2, text="Time")
        self.tv.column(2, width=60, anchor=CENTER)

        self.tv.heading(3, text="Pickup Location ")
        self.tv.column(3, width=120, anchor=CENTER)

        self.tv.heading(4, text="Drop Off  Location ")
        self.tv.column(4, width=120, anchor=CENTER)

        self.tv.heading(5, text="Driver Name")
        self.tv.column(5, width=120, anchor=CENTER)

        self.tv.heading(6, text="Driver Number")
        self.tv.column(6, width=120, anchor=CENTER)

        self.tv.heading(7, text="License Plate")
        self.tv.column(7, width=80, anchor=CENTER)

        self.tv.heading(8, text="Car Model")
        self.tv.column(8, width=80, anchor=CENTER)

        for ro in value:
            self.tv.insert("", "end", iid=ro, values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7]))
        # for ro2 in value2:
        # self.tv.insert("", "end", iid=ro2, values=(ro2[0]))

    # getting Necessary details from selected item in tree view

    def getBooking_ID(self):
        item = self.tv.selection()[0]
        Date = self.tv.item(item)['values'][0]
        Time = self.tv.item(item)['values'][1]
        Pickup = self.tv.item(item)['values'][2]
        Dropoff = self.tv.item(item)['values'][3]
        Name = self.tv.item(item)['values'][4]
        number = self.tv.item(item)['values'][5]
        Plate = self.tv.item(item)['values'][6]
        Model = self.tv.item(item)['values'][7]

        self.conn.cursor.execute(
            "select Booking_ID from booking_information where Pickup_Location = %s and Dropoff_Location = %s and Date = %s and Time = %s",
            (Pickup, Dropoff, Date, Time))
        value = [self.conn.cursor.fetchone()]
        print(value[0])
        return value

    # Get values from tree view and delete

    def selectValues(self):
        booking_ID = self.getBooking_ID()
        self.conn.cursor.execute("delete from booking_information where booking_ID = %s", booking_ID)
        self.conn.con.commit()
        selected_items = self.tv.selection()
        for selected_item in selected_items:
            self.tv.delete(selected_item)
        messagebox.showinfo("Information", "You have successfully cancelled your booking !")

    def getDriver_Name(self):
        conn2 = connection.cursor
        conn2.execute("select Driver_Name from driver_information where booking_information.Driver_ID = ")

    def back(self):
        self.root.destroy()
        import LoginPage

    # inserting data in database for booking

    def insertData(self):
        if self.pickup_txt.get() == "" or self.destination_txt.get() == "":
            messagebox.showerror("ERROR", "Please fill all the fields to Book a Taxi.")
        else:
            connection.cursor.execute("Insert into Booking_Information (Pickup_Location,DropOff_Location,"
                                      "Date, Time, Customer_ID) values (%s,%s,%s,%s,%s)",
                                      (self.var_pickup.get(),
                                       self.var_destination.get(),
                                       self.var_cal2.get(),
                                       self.spinbox.get() + ":" + self.spinbox2.get() + " " + self.spinbox3.get(),
                                       self.Customer_ID
                                       ))
            connection.con.commit()
            connection.con.close()
            messagebox.showinfo("Information", " Successful !")
            print(self.var_pickup.get())
            print(self.var_destination.get())
            print(self.var_cal2.get())
            print(self.spinbox.get() + ":" + self.spinbox2.get() + " " + self.spinbox3.get())


'''
root = Tk()
obj1 = Customer_Interface(root)
root.mainloop()
'''
