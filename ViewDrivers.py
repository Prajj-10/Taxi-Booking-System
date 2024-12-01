from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import pymysql

# Connection class to connect to database

class connection:
    con = pymysql.connect(host="localhost", user="root", password="", database="taxibooking")
    cursor = con.cursor()

# Viewing Drivers class

class ViewDrivers:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")  # window dimensions
        self.root.title("View Driver Table")
        self.test = ImageTk.PhotoImage(file="Images\\ViewDriver.jpg")  # loading image

        # creating a canvas to load image and writing transparent texts

        Label1 = Canvas(self.root)
        Label1.create_image(900, 600, image=self.test)
        Label1.create_text(700, 35, text="DRIVER TABLE", fill="#0045B2",
                           font=("times new roman", 24, "bold"))

        # creating object of connection class

        self.conn = connection
        self.conn.cursor.execute("select * from driver_information")

        status = StringVar()

        # --- TreeView ---

        self.tv = ttk.Treeview(self.root, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show='headings', height=8)
        self.tv.place(x=300, y=60)

        self.tv.heading(1, text="Driver ID")
        self.tv.column(1, width=60, anchor=CENTER)

        self.tv.heading(2, text="Driver Name")
        self.tv.column(2, width=120, anchor=CENTER)

        self.tv.heading(3, text="Driver Address")
        self.tv.column(3, width=120, anchor=CENTER)

        self.tv.heading(4, text="Telephone Number")
        self.tv.column(4, width=120, anchor=CENTER)

        self.tv.heading(5, text="Email")
        self.tv.column(5, width=150, anchor=CENTER)

        self.tv.heading(6, text="Password")
        self.tv.column(6, width=80, anchor=CENTER)

        self.tv.heading(7, text="License Plate")
        self.tv.column(7, width=80, anchor=CENTER)

        self.tv.heading(8, text="Car Model")
        self.tv.column(8, width=80, anchor=CENTER)

        self.tv.heading(9, text="Status")
        self.tv.column(9, width=80, anchor=CENTER)

        # inserting values

        for ro in self.conn.cursor:
            # print(ro)
            self.tv.insert("", "end", iid=ro, values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8]))

        # --- Buttons ---

        self.back_btn = Button(root, text="Back", bg="green", fg="white",
                               font=("times new roman", 20, "bold"), cursor="hand2", command=self.backToAdmin)
        self.back_btn.place(x=1050, y=320, width=200)

        # Vertical Scrollbar for tables

        vertical_scrollbar = ttk.Scrollbar(self.tv, orient='vertical',
                                           command=self.tv.yview)
        vertical_scrollbar.place(x=875, y=21, height=164)
        self.tv.configure(yscrollcommand=vertical_scrollbar.set)

        Label1.pack(fill="both", expand=True)

    # back button function to go back to admin page

    def backToAdmin(self):
        self.root.destroy()
        import AdminInterface



root = Tk()
obj1 = ViewDrivers(root)
root.mainloop()
