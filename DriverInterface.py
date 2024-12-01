# importing tkinter
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk

import pymysql

# Connection class for database connection

class connection:
    con = pymysql.connect(host="localhost", user="root", password="", database="taxibooking")
    cursor = con.cursor()

# Driver Interface class

class DriverInterfacePage:
    def __init__(self, root, email, Driver_Reg):
        self.root = root
        self.root.geometry("1920x1080+-10+0")  # dimension of the window
        self.root.title("Welcome Driver")
        self.root.config(bg="green")

        self.test = ImageTk.PhotoImage(file="Images\\DriInt.png")   # Loading Image

        # Connection to execute query

        conn = connection.cursor
        conn.execute("select b.Pickup_Location, b.Dropoff_Location, b.Date, b.Time, c.Customer_Name, c.Telephone_No "
                     "from booking_information b join customer_data c on b.Customer_ID = c.Customer_ID where "
                     "Driver_ID = %s ", Driver_Reg)
        allValues = [i[0:7] for i in conn.fetchall()]  # gets values in a list

        # Creating a canvas for transparent image

        Label1 = Canvas(self.root)
        Label1.create_image(650, 300, image=self.test)
        Label1.create_text(500, 30, text="WELCOME " + str(email), fill="#0045B2",
                           font=("times new roman", 24, "bold"))
        Label1.create_text(490, 60, text="Here are your bookings", fill="#0045B2",
                           font=("times new roman", 14, "bold"))

        # ---TreeView---

        self.tv = ttk.Treeview(self.root, columns=(1, 2, 3, 4, 5, 6), show='headings', height=8)
        self.tv.place(x=200, y=80)

        self.tv.heading(1, text="Pickup Location")
        self.tv.column(1, width=120, anchor=CENTER)

        self.tv.heading(2, text="Drop Off Location")
        self.tv.column(2, width=120, anchor=CENTER)

        self.tv.heading(3, text="Date")
        self.tv.column(3, width=120, anchor=CENTER)

        self.tv.heading(4, text="Time")
        self.tv.column(4, width=60, anchor=CENTER)

        self.tv.heading(5, text="Customer Name")
        self.tv.column(5, width=120, anchor=CENTER)

        self.tv.heading(6, text="Customer Telephone")
        self.tv.column(6, width=120, anchor=CENTER)

        for ro in allValues:
            # print(ro)
            self.tv.insert("", "end", iid=ro, values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]))

        self.login_btn = Button(root, text="Back", bg="red", fg="white",
                                font=("times new roman", 20, "bold"), cursor="hand2", command=self.back)
        self.login_btn.place(x=1050, y=205, width=200)

        Label1.pack(fill="both", expand=True)

    # back Button Function

    def back(self):
        self.root.destroy()
        import LoginPage

'''
root = Tk()
obj1 = DriverRegisterPage(root)
root.mainloop()

'''