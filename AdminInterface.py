# importing tkinter
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import pymysql
from PendingBookings import PendingBookings

# Connection for database class

class connection:
    con = pymysql.connect(host="localhost", user="root", password="", database="taxibooking")
    cursor = con.cursor()

# Admin Class

class AdminInterface:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x500+300+100")  # Dimensions for Admin
        self.root.title("Welcome Admin")
        self.root.config(bg="green")

        # Adding Image

        self.test = ImageTk.PhotoImage(file="Images\\Admin2.jpg")

        # Creating Canvas to put transparent texts

        Label1 = Canvas(self.root)
        Label1.create_image(650, 250, image=self.test)
        Label1.create_text(250, 150, text="WELCOME ADMIN", fill="#0045B2",
                           font=("times new roman", 24, "bold"))
        Label1.create_text(250, 180, text="What would you like to do?", fill="#0045B2",
                           font=("times new roman", 18, "bold"))

        # ---Buttons for use---

        self.driverVerify_btn = Button(root, width=20, text="VERIFY DRIVERS", bg="#32CD32", fg="white",
                                       font=("times new roman", 14, "bold"), cursor="hand2",
                                       command=self.OpenDriverBooking)
        self.driverVerify_btn.place(x=110, y=200, width=300)

        self.pending = Button(root, text="VIEW PENDING BOOKINGS", bg="#32CD32", fg="white",
                              font=("times new roman", 14, "bold"), cursor="hand2", command=self.OpenPendingBookings)
        self.pending.place(x=110, y=250, width=300)

        self.driver = Button(root, text="VIEW ALL DRIVERS", bg="#32CD32", fg="white",
                             font=("times new roman", 14, "bold"), cursor="hand2", command=self.ViewingDrivers)
        self.driver.place(x=110, y=300, width=300)

        self.customer = Button(root, text="VIEW ALL CUSTOMERS", bg="#32CD32", fg="white",
                               font=("times new roman", 14, "bold"), cursor="hand2", command=self.OpenAllCustomer)
        self.customer.place(x=110, y=350, width=300)

        self.booking = Button(root, text="VIEW ALL BOOKINGS", bg="#32CD32", fg="white",
                              font=("times new roman", 14, "bold"), cursor="hand2", command=self.View_allBookings)
        self.booking.place(x=110, y=400, width=300)

        self.back = Button(root, text="BACK", bg="red", fg="white",
                           font=("times new roman", 14, "bold"), cursor="hand2", command=self.backCommand)
        self.back.place(x=110, y=450, width=300)

        Label1.pack(fill="both", expand=True) # Packing all the image and text in a frame

    # Opens Booking Table

    def View_allBookings(self):
        self.root.destroy()
        import ViewBookings

    # Opens Driver table

    def ViewingDrivers(self):
        self.root.destroy()
        import ViewDrivers

    #  back to login

    def backCommand(self):
        self.root.destroy()
        import LoginPage

    # Opens Customer Table

    def OpenAllCustomer(self):
        self.root.destroy()
        import ViewCustomers

    # Opens Driver Verification

    def OpenDriverBooking(self):
        self.root.destroy()
        import VerifyDrivers

    # Opens Pending Bookings

    def OpenPendingBookings(self):
        self.root.destroy()
        # import PendingBookings
        root = Tk()
        obj1 = PendingBookings(root)
        root.mainloop()


'''
root = Tk()
obj1 = AdminInterface(root)
root.mainloop()
'''


