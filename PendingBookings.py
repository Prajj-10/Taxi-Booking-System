# importing tkinter
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import pymysql

# connection class to connect to database

class connection:
    con = pymysql.connect(host="localhost", user="root", password="", database="taxibooking")
    cursor = con.cursor()


# Pending booking class

class PendingBookings:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")  # Dimensions of the window
        self.root.title("View Pending Bookings")
        self.root.config(bg="white")
        self.test = ImageTk.PhotoImage(file="Images\\Admin2.jpg")  # Loading Image
        Label1 = Canvas(self.root)
        Label1.create_image(650, 250, image=self.test)  # Adding Image

        # adding transparent texts

        Label1.create_text(700, 35, text="BOOKING TABLE", fill="#0045B2",
                           font=("times new roman", 24, "bold"))

        # creating an object of connection class

        self.conn = connection
        self.conn.cursor.execute("select * from booking_information where Driver_ID is null")

        status = StringVar()

        # --- TreeView ---

        self.tv = ttk.Treeview(self.root, columns=(1, 2, 3, 4, 5, 6, 7), show='headings', height=8)
        self.tv.place(x=400, y=60)

        self.tv.heading(1, text="Booking ID")
        self.tv.column(1, width=80, anchor=CENTER)

        self.tv.heading(2, text="Pickup Location")
        self.tv.column(2, width=120, anchor=CENTER)

        self.tv.heading(3, text="Drop Off Location")
        self.tv.column(3, width=120, anchor=CENTER)

        self.tv.heading(4, text="Date")
        self.tv.column(4, width=50, anchor=CENTER)

        self.tv.heading(5, text="Time")
        self.tv.column(5, width=60, anchor=CENTER)

        self.tv.heading(6, text="Customer ID")
        self.tv.column(6, width=80, anchor=CENTER)

        self.tv.heading(7, text="Driver ID")
        self.tv.column(7, width=80, anchor=CENTER)

        for ro in self.conn.cursor:
            # print(ro)
            self.tv.insert("", "end", iid=ro, values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6]))

        self.clicked = StringVar()

        Label1.create_text(1150, 70, text="DRIVER ID", fill="#0045B2",
                           font=("times new roman", 24, "bold"))

        # ---Combobox---

        self.drop = ttk.Combobox(root, textvariable=self.clicked)
        self.drop.config(font=("times new roman", 20, "bold"), width=10)
        self.drop.place(x=1070, y=100)

        self.conn.cursor.execute(
            "Select Driver_ID from driver_information where Status = \"Active\" ")
        # print(cursor.execute())
        self.drop['values'] = [i[0] for i in self.conn.cursor.fetchall()]
        # print(Options)
        # self.clicked.set(self.drop[0])
        self.drop.current(0)

        # self.CheckPendingBookings()

        # --- Buttons ---

        self.login_btn = Button(root, text="Update", bg="green", fg="white",
                                font=("times new roman", 20, "bold"), cursor="hand2", command=self.dropDownSelect)
        self.login_btn.place(x=1050, y=255, width=200)

        self.back_btn = Button(root, text="Back", bg="green", fg="white",
                               font=("times new roman", 20, "bold"), cursor="hand2", command=self.back)
        self.back_btn.place(x=1050, y=320, width=200)

        vertical_scrollbar = ttk.Scrollbar(self.tv, orient='vertical',
                                           command=self.tv.yview)
        vertical_scrollbar.place(x=575, y=21, height=164)
        self.tv.configure(yscrollcommand=vertical_scrollbar.set)

        Label1.pack(fill="both", expand=True)

    '''
    def CheckPendingBookings(self):
        if self.clicked(self.Options[0]) == IndexError:
            return True
        else:
            return False
    '''

    # back button function

    def back(self):
        self.root.destroy()
        import AdminInterface

    # selecting value from treeview

    def selectValues(self):
        item = self.tv.selection()[0]
        ID = self.tv.item(item)['values'][0]
        return ID

    # getting value and updating the value

    def dropDownSelect(self):
        Booking_ID = self.selectValues()
        print(Booking_ID)
        variable = self.clicked.get()
        print(variable)
        self.conn.cursor.execute("Update booking_information Set Driver_ID = %s Where Booking_ID = %s",
                                 (variable, Booking_ID))

        self.conn.con.commit()
        messagebox.showinfo("Update", "Updated Successfully !")
        self.clearTable()
        self.refresh_table()

    # Clears all the table

    def clearTable(self):
        for item in self.tv.get_children():
            self.tv.delete(item)

    # Adds value again in the table

    def refresh_table(self):
        self.conn.cursor.execute("select * from booking_information where Driver_ID is null")
        value = [i[0:8] for i in self.conn.cursor.fetchall()]
        print(value)
        for ro in value:
            # print(ro)
            self.tv.insert("", "end", iid=ro, values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6]))


'''
root = Tk()
obj1 = PendingBookings(root)
root.mainloop()
'''
