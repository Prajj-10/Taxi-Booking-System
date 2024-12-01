from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import pymysql

# creating a connection class to connect to database

class connection:
    con = pymysql.connect(host="localhost", user="root", password="", database="taxibooking")
    cursor = con.cursor()


class ViewDrivers:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")  # window dimensions
        self.root.title("View all Customers")
        self.root.config(bg="white")
        self.test = ImageTk.PhotoImage(file="Images\\ViewCustomer.jpg")  # Loading Image

        # creating a canvas for transparent text

        Label1 = Canvas(self.root)
        Label1.create_image(900, 150, image=self.test)

        Label1.create_text(700, 35, text="CUSTOMER TABLE", fill="#0045B2",
                           font=("times new roman", 24, "bold"))

        # Creating object of connection class

        self.conn = connection
        self.conn.cursor.execute("select * from customer_data")

        status = StringVar()

        # ---TreeView---

        self.tv = ttk.Treeview(self.root, columns=(1, 2, 3, 4, 5, 6), show='headings', height=8)
        self.tv.place(x=300, y=60, width=770)

        self.tv.heading(1, text="Customer ID")
        self.tv.column(1, width=70, anchor=CENTER)

        self.tv.heading(2, text="Name")
        self.tv.column(2, width=120, anchor=CENTER)

        self.tv.heading(3, text="Address")
        self.tv.column(3, width=120, anchor=CENTER)

        self.tv.heading(4, text="Telephone Number")
        self.tv.column(4, width=120, anchor=CENTER)

        self.tv.heading(5, text="Email")
        self.tv.column(5, width=150, anchor=CENTER)

        self.tv.heading(6, text="Password")
        self.tv.column(6, width=80, anchor=CENTER)

        # inserting values

        for ro in self.conn.cursor:
            # print(ro)
            self.tv.insert("", "end", iid=ro, values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]))

        self.back_btn = Button(root, text="Back", bg="green", fg="white",
                               font=("times new roman", 20, "bold"), cursor="hand2", command=self.backToAdmin)
        self.back_btn.place(x=1050, y=320, width=200)

        # Vertical Scrollbar for the table

        vertical_scrollbar = ttk.Scrollbar(self.tv, orient='vertical',
                                           command=self.tv.yview)
        vertical_scrollbar.place(x=750, y=21, height=164)
        self.tv.configure(yscrollcommand=vertical_scrollbar.set)

        Label1.pack(fill="both", expand=True)

    # goes back to the admin interface

    def backToAdmin(self):
        self.root.destroy()
        import AdminInterface



root = Tk()
obj1 = ViewDrivers(root)
root.mainloop()
