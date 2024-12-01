# importing tkinter
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import pymysql

# connection class to connect Database

class connection:
    con = pymysql.connect(host="localhost", user="root", password="", database="taxibooking")
    cursor = con.cursor()

# class Admin interface

class AdminInterface:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")  # Dimensions for the window
        self.root.title("Verify Drivers")
        self.test = ImageTk.PhotoImage(file="Images\\VerifyDrivers1.png") # Loading Image

        # Creating canvas for transparent image

        Label1 = Canvas(self.root)
        Label1.create_image(400, 0, image=self.test)
        Label1.create_text(550, 35, text="VERIFYING DRIVER TABLE", fill="#0045B2",
                           font=("times new roman", 24, "bold"))

        # creating an object of connection

        self.conn = connection
        status = StringVar()

        # ---TreeView---

        self.tv = ttk.Treeview(self.root, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show='headings', height=8)
        self.tv.place(x=30, y=70)

        self.tv.heading(1, text="Driver_ID")
        self.tv.column(1, width=60, anchor=CENTER)
        self.tv.heading(2, text="Driver Name")
        self.tv.column(2, width=120, anchor=CENTER)
        self.tv.heading(3, text="Driver Address")
        self.tv.column(3, width=90, anchor=CENTER)
        self.tv.heading(4, text="Driver Telephone")
        self.tv.column(4, width=100, anchor=CENTER)
        self.tv.heading(5, text="Driver Email")
        self.tv.column(5, width=190, anchor=CENTER)
        self.tv.heading(6, text="Driver Password")
        self.tv.column(6, width=100, anchor=CENTER)
        self.tv.heading(7, text="License Plate")
        self.tv.column(7, width=90, anchor=CENTER)
        self.tv.heading(8, text="Car Model")
        self.tv.column(8, width=90, anchor=CENTER)
        self.tv.heading(9, text="Status")
        self.tv.column(9, width=90, anchor=CENTER)

        self.insert_table()
        '''
        for ro in self.conn:
            # print(ro)
            self.tv.insert("", "end", iid=ro, values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8]))
        '''
        # ---- Drop Down Box---

        self.clicked = StringVar()

        self.clicked.set("Pending")

        self.drop = ttk.Combobox(root, textvariable=self.clicked)
        self.drop.config(font=("times new roman", 18, "bold"), width=15)
        self.drop['values'] = ("Pending",
                               "Active",
                               "Working",
                               "Inactive")
        self.drop.place(x=1050, y=70)



        # --- Buttons ----

        self.login_btn = Button(root, text="Update", bg="green", fg="white",
                                font=("times new roman", 20, "bold"), cursor="hand2", command=self.dropDownSelect)
        self.login_btn.place(x=1050, y=255, width=200)

        self.login_btn = Button(root, text="Back", bg="green", fg="white",
                                font=("times new roman", 20, "bold"), cursor="hand2", command=self.back)
        self.login_btn.place(x=1050, y=315, width=200)

        vertical_scrollbar = ttk.Scrollbar(self.tv, orient='vertical',
                                           command=self.tv.yview)
        vertical_scrollbar.place(x=915, y=21, height=164)
        self.tv.configure(yscrollcommand=vertical_scrollbar.set)

        Label1.pack(fill="both", expand=True)

    # returns the ID of selected TreeView

    def selectValues(self):
        item = self.tv.selection()[0]
        ID = self.tv.item(item)['values'][0]
        return ID

    # Goes back to Admin

    def back(self):
        self.root.destroy()
        import AdminInterface

    # Updates the value for driver verification

    def dropDownSelect(self):
        Driver_ID = self.selectValues()
        print(Driver_ID)
        variable = self.clicked.get()
        print(variable)
        self.conn.cursor.execute("Update driver_information Set Status = %s Where Driver_ID = %s",
                                 (variable, Driver_ID))
        self.conn.con.commit()
        # self.conn.cursor.close()

        messagebox.showinfo("Update", "Updated Successfully !")

        # self.tv.delete()
        self.clearTable()
        self.insert_table()

    # clears table from the tree view

    def clearTable(self):
        for item in self.tv.get_children():
            self.tv.delete(item)

    # inserts the value again

    def insert_table(self):
        self.conn.cursor.execute("select * from driver_information")
        value = [i[0:10] for i in self.conn.cursor.fetchall()]
        print(value)
        for ro in value:
            # print(ro)
            self.tv.insert("", "end", iid=ro, values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8]))


root = Tk()
obj1 = AdminInterface(root)
root.mainloop()
