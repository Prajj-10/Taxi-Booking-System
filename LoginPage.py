# importing Tkinter
import tkinter
from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image, ImageTk
from Registration import registerPage
from CustomerInterface import Customer_Interface
from DriverInterface import DriverInterfacePage
from AdminInterface import AdminInterface
from DriverRegistration import DriverRegisterPage

# connnection class for database
class connection:
    con = pymysql.connect(host="localhost", user="root", password="", database="taxibooking")
    cursor = con.cursor()

# class login for login functions
class login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")  # geometry for the window
        self.root.title("Login")
        # photoLabel = Image.open("C:\\Users\\LENOVO\\Downloads\\TaxiBooking2.jpg")
        self.test = ImageTk.PhotoImage(file="Images\\TaxiBooking2.jpg")

        Label1 = Canvas(self.root) # adds a label canvas to the frame
        Label1.create_image(450, 400, image=self.test)  # image adding

        # Transparent Labels

        Label1.create_text(1050, 50, text="LOGIN PAGE", fill="yellow", font=("Times New Roman", 30, "bold"))
        # taxi_lbl = Canvas(self.root)
        Label1.create_text(1050, 100, text="Welcome to Zee-Muu Taxi", fill="yellow",
                           font=("Times New Roman", 20, "bold"))

        Label1.create_text(900, 150, text="Email:", fill="yellow",
                           font=("Times New Roman", 20, "bold"))

        self.var_email = StringVar()  # text variable to store values
        self.email_txt = Entry(root, font=("times new roman", 20), textvariable=self.var_email)
        self.email_txt.place(x=950, y=130)

        Label1.create_text(880, 210, text="Password:", fill="yellow",
                           font=("Times New Roman", 20, "bold"))

        self.var_password = StringVar()  # text variable to store values
        self.password_txt = Entry(root, font=("times new roman", 20), show="*", textvariable=self.var_password)
        self.password_txt.place(x=950, y=190)

        Label1.pack(fill="both", expand=True)

        # Buttons
        self.login_btn = Button(root, text="Login", bg="black", fg="white", font=("times new roman", 20, "bold"),
                                cursor="hand2", command=self.login_fn)
        self.login_btn.place(x=800, y=270, width=200)

        self.register_btn = Button(root, text="New Customer ?", bg="black", fg="white",
                                   font=("times new roman", 20, "bold"),
                                   cursor="hand2", command=self.register)
        self.register_btn.place(x=800, y=340, width=200)

        self.registerDriver_btn = Button(root, text="New Driver ?", bg="black", fg="white",
                                         font=("times new roman", 20, "bold"),
                                         cursor="hand2", command=self.DriverReg)
        self.registerDriver_btn.place(x=1020, y=270, width=200)

        self.exit_btn = Button(root, text="EXIT", bg="black", fg="white",
                               font=("times new roman", 20, "bold"),
                               cursor="hand2", command=self.root.destroy)
        self.exit_btn.place(x=1020, y=340, width=200)

        # ---CheckBox---
        self.isChecked = IntVar()
        self.chk = Checkbutton(root, bg="black", onvalue=1, offvalue=0, font=("Times New Roman", 15),
                               variable=self.isChecked, command=self.hideUnhide)
        self.chk.place(x=1010, y=230)

        Label1.create_text(905, 245, text="Hide/Unhide", font=("Times New Roman", 20, "bold"), fill="yellow")

    # hide unhide password function

    def hideUnhide(self):
        if self.isChecked.get():
            self.password_txt.config(show="")
        else:
            self.password_txt.config(show="*")

    # opening different interfaces

    def login_fn(self):
        Customer_ID = self.RegID()
        # print(Customer_ID)
        Driver_ID = self.DriverRegID()
        conn = connection
        conn2 = connection
        if self.email_txt.get() == "" or self.password_txt.get() == "":
            messagebox.showerror("ERROR", "Please fill all the fields to Login.")
        else:
            query1 = conn.cursor.execute(
                "Select * from customer_data where Customer_Email = %s and Customer_Password = %s",
                (self.var_email.get(),
                 self.var_password.get()))
            customer_name = [i[1] for i in conn.cursor.fetchall()]
            # print(customer_name[0])

            query2 = conn.cursor.execute(
                "Select * from driver_information where Driver_Email = %s and Driver_Password = %s",
                (self.var_email.get(),
                 self.var_password.get()))
            driver_name = [i[1] for i in conn2.cursor.fetchall()]
            # print(driver_name[0])

            conn.con.commit()

            #  print(self.email_txt.get(), self.password_txt.get())

            if self.var_email.get() == "admin" and self.var_password.get() == "admin":
                self.root.destroy()
                # import AdminInterface
                root = Tk()
                obj1 = AdminInterface(root)
                root.mainloop()

            elif not driver_name and customer_name is not None:
                    # self.RegID()
                    self.root.destroy()
                    # import CustomerInterface
                    root = Tk()
                    Customer_Interface(root, customer_name[0], Customer_ID)
                    root.mainloop()
                    # messagebox.showerror("Error", "This account has not been registered."
                                                 #  "Please create an account to Login.")
            elif not customer_name and driver_name is not None:
                # self.DriverRegID()
                self.root.destroy()
                # import DriverInterface
                root = Tk()
                obj = DriverInterfacePage(root, driver_name[0], Driver_ID)
                root.mainloop()
            else:
                messagebox.showinfo("Information", "This account has not been registered."
                                                   "Please create an account to Login.")

    # getting Registration ID

    def RegID(self):
        conn = connection
        conn.cursor.execute("Select Customer_ID from customer_data where Customer_Email = %s and "
                            "Customer_Password = %s",
                            (self.var_email.get(),
                             self.var_password.get()))
        CustomerID = conn.cursor.fetchone()
        # print(CustomerID)
        return CustomerID

    # getting Driver ID

    def DriverRegID(self):
        conn = connection
        conn.cursor.execute(
            "Select Driver_ID from driver_information where Driver_Email = %s and Driver_Password = %s",
            (self.var_email.get(),
             self.var_password.get()))
        DriverID = conn.cursor.fetchone()
        # print(DriverID)
        return DriverID

    # opening customer registration

    def register(self):
        self.root.destroy()
        root = Tk()
        registerPage(root)
        root.mainloop()

    # opening Driver Registration

    def DriverReg(self):
        self.root.destroy()
        root = Tk()
        obj1 = DriverRegisterPage(root)
        root.mainloop()

    # fetching data to check values

    def fetchingData(self):
        print(self.var_email.get(), self.var_password.get())
        print()


root = Tk()
object1 = login(root)
root.mainloop()
