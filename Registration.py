# importing tkinter
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
# from LoginPage import login

# connection class to connect with database

class connection:
    con = pymysql.connect(host="localhost", user="root", password="", database="taxibooking")
    cursor = con.cursor()

# Register Page class

class registerPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080")  # Dimensions of the Window
        self.root.title("Customer Register Window")
        self.root.config(bg="green")
        # photoLabel = Image.open()
        self.test = ImageTk.PhotoImage(file="Images\\reg2.jpg")  # Image Load

        # Canvas to write transparent image

        Label1 = Canvas(self.root)
        Label1.create_image(930, 530, image=self.test)

        # Label1.place(x=0, y=-100)
        # ---------Creating Login Frame-----------
        # login_frame = Frame(self.root, bg="black")
        # login_frame.place(x=550, y=90, width=700, height=530)

        # --------Labeling-----------
        Label1.create_text(300, 410, text="CUSTOMER REGISTRATION", fill="yellow",
                           font=("times new roman", 30, "bold"))

        Label1.create_text(130, 450, text="NAME", fill="yellow",
                           font=("times new roman", 24, "bold"))

        # text varibale to store data

        self.var_name = StringVar()
        self.name_txt = Entry(root, font=("times new roman", 18), fg="black", bg="white",
                              textvariable=self.var_name)
        self.name_txt.place(x=20, y=470, width=220, height=30)

        Label1.create_text(360, 450, text="ADDRESS", fill="yellow",
                           font=("times new roman", 24, "bold"))

        # text varibale to store data

        self.var_address = StringVar()
        self.address_txt = Entry(root, font=("times new roman", 18), fg="black", bg="white",
                                 textvariable=self.var_address)
        self.address_txt.place(x=265, y=470, width=200, height=30)

        Label1.create_text(600, 450, text="TELEPHONE", fill="yellow",
                           font=("times new roman", 24, "bold"))

        # text varibale to store data

        self.var_telephone_no = StringVar()
        self.telephone_txt = Entry(root, font=("times new roman", 18), fg="black", bg="white",
                                   textvariable=self.var_telephone_no)
        self.telephone_txt.place(x=500, y=470, width=200, height=30)

        Label1.create_text(850, 450, text="EMAIL", fill="yellow",
                           font=("times new roman", 24, "bold"))

        # text varibale to store data

        self.var_email = StringVar()
        self.email_txt = Entry(root, font=("times new roman", 18), fg="black", bg="white",
                               textvariable=self.var_email)
        self.email_txt.place(x=720, y=470, width=330, height=30)

        Label1.create_text(360, 550, text="PASSWORD", fill="yellow",
                           font=("times new roman", 24, "bold"))

        # text varibale to store data

        self.var_pw = StringVar()
        self.password_txt = Entry(root, font=("times new roman", 18), fg="black", bg="white", show="*",
                                  textvariable=self.var_pw)
        self.password_txt.place(x=250, y=570, width=220, height=30)

        Label1.create_text(700, 550, text="CONFIRM PASSWORD", fill="yellow",
                           font=("times new roman", 24, "bold"))

        # text varibale to store data

        self.var_confirm_pw = StringVar()
        self.confirm_password_txt = Entry(root, font=("times new roman", 18), fg="black", bg="white", show="*",
                                          textvariable=self.var_confirm_pw)
        self.confirm_password_txt.place(x=590, y=570, width=220, height=30)

        # ----------Buttons---------------
        self.login_btn = Button(root, text="Back", bg="red", fg="white",
                                font=("times new roman", 20, "bold"), cursor="hand2", command=self.login_window)
        self.login_btn.place(x=1070, y=510, width=200)

        self.register_btn = Button(root, text="Register", bg="#32CD32", fg="white",
                                   font=("times new roman", 20, "bold"),
                                   cursor="hand2", command=self.data)
        self.register_btn.place(x=1070, y=580, width=200)

        # text varibale to store data

        self.isChecked = IntVar()

        # Check button for hide and unhide

        self.chk = Checkbutton(root, bg="black", onvalue=1, offvalue=0, font=("Times New Roman", 15),
                               variable=self.isChecked, command=self.hideUnhide)
        self.chk.place(x=820, y=600)

        Label1.create_text(950, 615, text="Hide/Unhide", font=("Times New Roman", 20, "bold"), fill="yellow")

        Label1.pack(fill="both", expand=True)

    # hide/ unhide function

    def hideUnhide(self):
        if self.isChecked.get():
            self.password_txt.config(show="")
            self.confirm_password_txt.config(show="")
        else:
            self.password_txt.config(show="*")
            self.confirm_password_txt.config(show="*")

    # back to Login Page

    def login_window(self):
        self.root.destroy()
        import LoginPage

    # inserts the values to the table

    def data(self):
        if self.email_txt.get() == "" or self.password_txt.get() == "" or self.name_txt == "" or self.var_telephone_no == "" or self.address_txt == "" or self.confirm_password_txt == "":
            messagebox.showerror("ERROR", "Please fill all the fields to Login.")
        elif self.password_txt.get() != self.confirm_password_txt.get():
            messagebox.showerror("ERROR", "The passwords don't match. Please enter the same passwords.")
        else:
            connection.cursor.execute("Insert into customer_data (Customer_Name,Customer_Address,Telephone_No,"
                                      "Customer_Email,Customer_Password) values (%s,%s,%s,%s,%s)",
                                      (self.var_name.get(),
                                       self.var_address.get(),
                                       self.var_telephone_no.get(),
                                       self.var_email.get(),
                                       self.var_pw.get()
                                       ))
            connection.con.commit()
            connection.con.close()
            messagebox.showinfo("Information", "Registration Successful !")

        # this clears the values after the user has been successfully registered.

        self.name_txt.delete(0, 'end')
        self.address_txt.delete(0, 'end')
        self.telephone_txt.delete(0, 'end')
        self.email_txt.delete(0, 'end')
        self.password_txt.delete(0, 'end')
        self.confirm_password_txt.delete(0, 'end')

'''
root = Tk()
obj1 = registerPage(root)
root.mainloop()
'''
