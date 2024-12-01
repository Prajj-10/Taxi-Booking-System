# importing tkinter
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql

# Connection to database

class connection:
    con = pymysql.connect(host="localhost", user="root", password="", database="taxibooking")
    cursor = con.cursor()

# Registration page for driver class

class DriverRegisterPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+-10+0")  # Dimensions
        self.root.title("Driver Register Window")
        self.root.config(bg="green")
        # self.root.wm_attributes('-transparent-colour', 'red')
        # photoLabel = Image.open()
        self.test = ImageTk.PhotoImage(file="Images\\DriverReg.png") # loading image

        Label1 = Canvas(self.root)
        Label1.create_image(650, 400, image=self.test)

        # --------Labeling-----------

        Label1.create_text(1000, 20, text="DRIVER REGISTRATION", fill="black",
                           font=("times new roman", 30, "bold"))

        Label1.create_text(800, 100, text="NAME", fill="black",
                           font=("times new roman", 24, "bold"))

        # text variable to store data

        self.var_name = StringVar()
        self.name_txt = Entry(root, font=("times new roman", 18), fg="black", bg="white",
                              textvariable=self.var_name)
        self.name_txt.place(x=700, y=120, width=220, height=30)

        Label1.create_text(1100, 100, text="ADDRESS", fill="black",
                           font=("times new roman", 24, "bold"))

        # text variable to store data

        self.var_address = StringVar()
        self.address_txt = Entry(root, font=("times new roman", 18), fg="black", bg="white",
                                 textvariable=self.var_address)
        self.address_txt.place(x=1000, y=120, width=250, height=30)

        Label1.create_text(820, 200, text="TELEPHONE", fill="black",
                           font=("times new roman", 24, "bold"))

        # text variable to store data

        self.var_telephone_no = StringVar()
        self.telephone_txt = Entry(root, font=("times new roman", 18), fg="black", bg="white",
                                   textvariable=self.var_telephone_no)
        self.telephone_txt.place(x=700, y=220, width=220, height=30)

        Label1.create_text(1120, 200, text="EMAIL", fill="black",
                           font=("times new roman", 24, "bold"))

        # text variable to store data

        self.var_email = StringVar()
        self.email_txt = Entry(root, font=("times new roman", 18), fg="black", bg="white",
                               textvariable=self.var_email)
        self.email_txt.place(x=1000, y=220, width=250, height=30)

        Label1.create_text(810, 310, text="PASSWORD", fill="black",
                           font=("times new roman", 24, "bold"))

        # text variable to store data

        self.var_pw = StringVar()
        self.password_txt = Entry(root, font=("times new roman", 18), fg="black", bg="white", show="*",
                                  textvariable=self.var_pw)
        self.password_txt.place(x=700, y=330, width=220, height=30)

        Label1.create_text(1100, 310, text="CONFIRM PASSWORD", fill="black",
                           font=("times new roman", 24, "bold"))

        # text variable to store data

        self.var_confirm_pw = StringVar()
        self.confirm_password_txt = Entry(root, font=("times new roman", 18), fg="black", bg="white", show="*",
                                          textvariable=self.var_confirm_pw)
        self.confirm_password_txt.place(x=1000, y=330, width=250, height=30)

        Label1.create_text(810, 400, text="PLATE NO", fill="black",
                           font=("times new roman", 24, "bold"))

        # text variable to store data

        self.var_plateNo = StringVar()
        self.plateNo_txt = Entry(root, font=("times new roman", 18), fg="black", bg="white",
                                 textvariable=self.var_plateNo)
        self.plateNo_txt.place(x=700, y=420, width=220, height=30)

        Label1.create_text(1120, 400, text="CAR MODEL", fill="black",
                           font=("times new roman", 24, "bold"))

        # text variable to store data

        self.var_carModel = StringVar()
        self.carModel_txt = Entry(root, font=("times new roman", 18), fg="black", bg="white",
                                  textvariable=self.var_carModel)
        self.carModel_txt.place(x=1000, y=420, width=250, height=30)

        # ----------Buttons---------------
        self.login_btn = Button(root, text="Back", bg="red", fg="white",
                                font=("times new roman", 20, "bold"), cursor="hand2", command=self.Login)
        self.login_btn.place(x=1050, y=470, width=200)

        self.register_btn = Button(root, text="Register", bg="#32CD32", fg="white",
                                   font=("times new roman", 20, "bold"),
                                   cursor="hand2", command=self.data)
        self.register_btn.place(x=1050, y=550, width=200)

        # text variable to store data

        self.isChecked = IntVar()

        # Check Button to show and hide passwords

        self.chk = Checkbutton(root, bg="yellow", onvalue=1, offvalue=0, font=("Times New Roman", 15),
                               variable=self.isChecked, command=self.hideUnhide)
        self.chk.place(x=750, y=455)

        Label1.create_text(855, 470, text="Hide/Unhide", font=("Times New Roman", 20, "bold"), fill="black")

        Label1.pack(fill="both", expand=True)

    # hide unhide password function

    def hideUnhide(self):
        if self.isChecked.get():
            self.password_txt.config(show="")
            self.confirm_password_txt.config(show="")
        else:
            self.password_txt.config(show="*")
            self.confirm_password_txt.config(show="*")
    '''
    def login_window(self):
        self.root.destroy()
        import DriverRegistration
    '''

    # Login page back

    def Login(self):
        self.root.destroy()
        import LoginPage

    # inserting the data of Driver to Database function

    def data(self):
        if self.email_txt.get() == "" or self.password_txt.get() == "" or self.name_txt == "" or self.var_telephone_no == "" or self.address_txt == "" or self.confirm_password_txt == "":
            messagebox.showerror("ERROR", "Please fill all the fields to Login.")
        elif self.password_txt.get() != self.confirm_password_txt.get():
            messagebox.showerror("ERROR", "The passwords don't match. Please enter the same passwords.")
        else:
            connection.cursor.execute("Insert into driver_information (Driver_Name,Driver_Address,Driver_Telephone,"
                                      "Driver_Email,Driver_Password, License_Plate, Car_Model) values (%s,%s,%s,%s,"
                                      "%s,%s,%s)",
                                      (self.var_name.get(),
                                       self.var_address.get(),
                                       self.var_telephone_no.get(),
                                       self.var_email.get(),
                                       self.var_pw.get(),
                                       self.var_plateNo.get(),
                                       self.var_carModel.get()
                                       ))
            connection.con.commit()
            connection.con.close()
            messagebox.showinfo("Information", "Registration Successful !")

        # Prints values in the console

        self.name_txt.delete(0, 'end')
        self.address_txt.delete(0, 'end')
        self.telephone_txt.delete(0, 'end')
        self.email_txt.delete(0, 'end')
        self.password_txt.delete(0, 'end')
        self.confirm_password_txt.delete(0, 'end')
        self.plateNo_txt.delete(0, 'end')
        self.carModel_txt.delete(0, 'end')


'''
root = Tk()
obj1 = DriverRegisterPage(root)
root.mainloop()
'''