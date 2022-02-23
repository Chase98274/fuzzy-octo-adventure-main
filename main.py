import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial

def new_customer(fname, lname, mobile, email):
    """This function creates a connection to the database then runs a query to insert the new customer"""
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Hayman_Robyn577",
            database="customers")

        mySql_insert_query = "INSERT INTO info (first_name, last_name, mobile, email) VALUES (%s, %s, %s, %s)"
        data = (fname, lname, mobile, email)

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, data)
        connection.commit()
        print(cursor.rowcount, "Record inserted successfully into info table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into info table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

def new_customer_pop():

    new_pop = Tk()
    new_pop.title("New Customer Registration")

    fname_var=StringVar(new_pop)
    lname_var=StringVar(new_pop)
    mobile_var=StringVar(new_pop)
    email_var=StringVar(new_pop)

    def submit():
        fname = fname_var.get().strip().lower().capitalize()
        lname = lname_var.get().strip().lower().capitalize()
        mobile = mobile_var.get().strip()
        email = email_var.get().strip()

        new_customer(fname, lname, mobile, email)

        messagebox.showinfo("Customer Registration", "{} has been successfully added".format(fname))

        new_pop.destroy()



    

    fname_label = Label(new_pop, text="First Name:")
    lname_label = Label(new_pop, text="Last Name:")
    mobile_label = Label(new_pop, text="Mobile:")
    email_label = Label(new_pop, text="Email: ")

    fname_entry = Entry(new_pop, textvariable=fname_var)
    lname_entry = Entry(new_pop, textvariable=lname_var)
    mobile_entry = Entry(new_pop, textvariable=mobile_var)
    email_entry = Entry(new_pop, textvariable=email_var)

    fname_label.grid(row=0, column=0, sticky="NSEW", padx=5, pady=5)
    fname_entry.grid(row=0, column=1, padx=5, pady=5)

    lname_label.grid(row=1, column=0, sticky="NSEW", padx=5, pady=5)
    lname_entry.grid(row=1, column=1, padx=5, pady=5)

    mobile_label.grid(row=2, column=0, sticky="NSEW", padx=5, pady=5)
    mobile_entry.grid(row=2, column=1, padx=5, pady=5)

    email_label.grid(row=3, column=0, sticky="NSEW", padx=5, pady=5)
    email_entry.grid(row=3, column=1, padx=5, pady=5)


    sub_btn = Button(new_pop, text="Submit", command=submit, width=10)
    sub_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    new_pop.mainloop()
    
def query():

    

    def search_submit():
        mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Hayman_Robyn577",
        database="customers")

        mycursor = mydb.cursor()

        if mode.get() == "1":
            mycursor.execute("SELECT * FROM customers.info WHERE first_name = \"{}\";".format(search_var.get().strip().lower().capitalize()))
            myresult = mycursor.fetchall()
            for x in myresult:
                messagebox.showinfo("Results", x)

        elif mode.get() == "2":
            mycursor.execute("SELECT * FROM customers.info WHERE last_name = \"{}\";".format(search_var.get().strip().lower().capitalize()))
            myresult = mycursor.fetchall()
            for x in myresult:
                messagebox.showinfo("Results", x)

        elif mode.get() == "3":
            
            mycursor.execute("SELECT * FROM customers.info WHERE mobile = \"{}\";".format(search_var.get().strip()))
            myresult = mycursor.fetchall()
            for x in myresult:
                messagebox.showinfo("Results", x)

        elif mode.get() == "4":
            
            mycursor.execute("SELECT * FROM customers.info WHERE email = \"{}\";".format(search_var.get().strip().lower()))
            myresult = mycursor.fetchall()
            for x in myresult:
                messagebox.showinfo("Results", x)

        else:
            print("Sorry that was a bad option!")
            print(mode.get())


    

        
        search_pop.destroy()
    def sel():
        selection = "You selected the option " + str(mode.get())
        print(selection)
    
    search_pop = Tk()
    search_pop.title("Search")

    search_frame = Frame(search_pop)
    search_frame.grid(row=1, column=0, padx=5, pady=5)

    search_par = LabelFrame(search_pop, text="Search by:")
    search_par.grid(row=0, column=0, padx=5, pady=5)

    search_var = StringVar(search_pop)
    mode = StringVar(search_pop, "1")

    # Dictionary to create multiple buttons
    values = {"First Name" : "1",
              "Last Name" : "2",
              "Mobile" : "3",
              "Email" : "4"}
    i = 1
    for (text, value) in values.items():
        Radiobutton(search_par, text = text, variable = mode,
            value = value, command=sel).grid(row=i, column=0, pady = 5)
        i += 1

    
    search_entry = Entry(search_frame, textvariable=search_var)
    search_entry.grid(row=0, column=0, padx=5, pady=5)

    search_btn_query = Button(search_frame, text="Search", command=search_submit)
    search_btn_query.grid(row=0, column=1)

    

    


    



def home_page():
    window = Tk()
    window.title("Home Page")
    window.geometry("500x500")

    window.columnconfigure([0,1,2], weight=1, minsize=75)
    window.rowconfigure([0,1,2], weight=1, minsize=50)

    

    #Creating main Notebook
    details_tab = ttk.Notebook(window)
    
    details_tab_1 = Frame(details_tab)
    details_tab_2 = Frame(details_tab)

    #detail tabs 1 & 2 are added to the main Notebook
    details_tab.add(details_tab_1, text="Customers")
    details_tab.add(details_tab_2, text="Contacts")   

    #Label frame called "Customer Centre" created
    cust_label_frame = LabelFrame(details_tab_1, text="Customer Centre")
    cust_label_frame.grid(row=5, column=0, padx=5, pady=5, sticky="NSEW")

    #New customer button
    new_cust_but = Button(details_tab_1, text="Create New Customer", command=new_customer_pop)
    new_cust_but.grid(row=0, column=0, sticky="NSEW", padx=10, pady=10)

    search_btn = Button(details_tab_1, text="Search", command=query)
    search_btn.grid(row=0, column=1)  

    info_frame = Frame(details_tab_1)
    info_frame.grid(row=1, column=0, padx=5, pady=5)

    #Customer first name label
    display_fname = Label(info_frame, text="First name: ")
    display_fname.grid(row=0, column=0, padx=5, pady=5)

    #Label for last name
    display_lname = Label(info_frame, text="Last name: ")
    display_lname.grid(row=1, column=0, padx=5, pady=5)

    #Label for mobile number
    display_mobile =Label(info_frame, text="Mobile: ")
    display_mobile.grid(row=2, column=0, padx=5, pady=5)

    #Label for email
    display_email =Label(info_frame, text="Email: ")
    display_email.grid(row=3, column=0, padx=5, pady=5)

    details_tab.grid(row=1, column=0, sticky="NSEW", padx=5, pady=5)

    window.mainloop()


def login():

    def validateLogin(username, password):

        if username.get() == "chase" and password.get() == "1234":
            tkWindow.destroy()
            home_page()
        else:
            messagebox.showerror("Incorrect details", "The username or password is incorrect. Please try again.")
            username.set("")
            password.set("")

    #window
    tkWindow = Tk()
    tkWindow.title('Login Form - Customer Database')

    #username label and text entry box
    usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0, padx=5, pady=5)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username,).grid(row=0, column=1, padx=5, pady=5)  

    #password label and password entry box
    passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0, padx=5, pady=5)  
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1, padx=5, pady=5)  

    validateLogin = partial(validateLogin, username, password)

    #login button
    loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    tkWindow.mainloop()

login()