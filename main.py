import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def new_customer(fname, lname, mobile):
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Hayman_Robyn577",
            database="customers")



        mySql_insert_query = "INSERT INTO info (first_name, last_name, mobile) VALUES (%s, %s, %s)"
        data = (fname, lname, mobile)

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

    def submit():
        fname = fname_var.get().strip().lower().capitalize()
        lname = lname_var.get().strip().lower().capitalize()
        mobile = mobile_var.get().strip()

        new_customer(fname, lname, mobile)

        messagebox.showinfo("Customer Registration", "{} has been successfully added".format(fname))

        new_pop.destroy()



    

    fname_label = Label(new_pop, text="First Name:")
    lname_label = Label(new_pop, text="Last Name:")
    mobile_label = Label(new_pop, text="Mobile:")

    fname_entry = Entry(new_pop, textvariable=fname_var)
    lname_entry = Entry(new_pop, textvariable=lname_var)
    mobile_entry = Entry(new_pop, textvariable=mobile_var)

    fname_label.grid(row=0, column=0, sticky="NSEW", padx=5, pady=5)
    fname_entry.grid(row=0, column=1, padx=5, pady=5)

    lname_label.grid(row=1, column=0, sticky="NSEW", padx=5, pady=5)
    lname_entry.grid(row=1, column=1, padx=5, pady=5)

    mobile_label.grid(row=2, column=0, sticky="NSEW", padx=5, pady=5)
    mobile_entry.grid(row=2, column=1, padx=5, pady=5)

    sub_btn = Button(new_pop, text="Submit", command=submit, width=10)
    sub_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    new_pop.mainloop()
    



window = Tk()
window.title("Home Page")
window.geometry("500x280")

window.columnconfigure([0,1,2], weight=1, minsize=75)
window.rowconfigure([0,1,2], weight=1, minsize=50)

cust_label_frame = LabelFrame(window, text="Customer Centre")

cust_tab = ttk.Notebook(cust_label_frame)

cust_tab_1 = Frame(cust_tab)
cust_tab_2 = Frame(cust_tab)

# product_tab_1 = Frame(product_tab)
# product_tab_2 = Frame(product_tab)

product_tab = ttk.Notebook(cust_tab_1)

cust_tab.add(cust_tab_1, text="Contact")
cust_tab.add(cust_tab_2, text="Details")

# product_tab.add(product_tab_1, text="Info")
# product_tab.add(product_tab_2, text="Details")

# label1 = Label(product_tab_1, text="label 1")
# label2 = Label(product_tab_2, text="label 2")
label3 = Label(cust_tab_1, text="label 3")
label4 = Label(cust_tab_2, text="label 4")

details_tab = ttk.Notebook(cust_tab_1)

details_tab_1 = Frame(details_tab)
details_tab_2 = Frame(details_tab)

details_tab.add(details_tab_1, text="Details")
details_tab.add(details_tab_2, text="Contacts")

cust_label_frame.grid(row=0, column=0, columnspan=2, sticky="NSEW")

# label1.grid(row=0, column=0)
# label2.grid(row=0, column=0)
label3.grid(row=0, column=0)
label4.grid(row=0, column=0)

product_tab.grid(row=0, column=0, sticky="NSEW")
details_tab.grid(row=0, column=0, sticky="NSEW")

cust_tab.grid(row=0, column=1, sticky="NSEW")


new_cust_but = Button(window, text="Create New Customer", command=new_customer_pop)

new_cust_but.grid(row=1, column=0, columnspan=2, sticky="NSEW", padx=10, pady=10)


window.mainloop()