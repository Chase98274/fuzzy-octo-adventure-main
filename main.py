from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv

class Users():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
user_1 = Users("chase", "1234")

model = []

def model_code_write(event=None):
    with open("data\models.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(model)
    
    messagebox.showinfo("Models", "{} has been added successfully".format(model))


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

        messagebox.showinfo("Customer Registration", "{} has been successfully added".format(fname))

        new_pop.destroy()

    fname_label = ttk.Label(new_pop, text="First Name:")
    lname_label = ttk.Label(new_pop, text="Last Name:")
    mobile_label = ttk.Label(new_pop, text="Mobile:")
    email_label = ttk.Label(new_pop, text="Email: ")

    fname_entry = ttk.Entry(new_pop, textvariable=fname_var)
    lname_entry = ttk.Entry(new_pop, textvariable=lname_var)
    mobile_entry = ttk.Entry(new_pop, textvariable=mobile_var)
    email_entry = ttk.Entry(new_pop, textvariable=email_var)

    fname_label.grid(row=0, column=0, sticky="NSEW", padx=5, pady=5)
    fname_entry.grid(row=0, column=1, padx=5, pady=5)

    lname_label.grid(row=1, column=0, sticky="NSEW", padx=5, pady=5)
    lname_entry.grid(row=1, column=1, padx=5, pady=5)

    mobile_label.grid(row=2, column=0, sticky="NSEW", padx=5, pady=5)
    mobile_entry.grid(row=2, column=1, padx=5, pady=5)

    email_label.grid(row=3, column=0, sticky="NSEW", padx=5, pady=5)
    email_entry.grid(row=3, column=1, padx=5, pady=5)


    sub_btn = ttk.Button(new_pop, text="Submit", command=submit, width=10)
    sub_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    new_pop.mainloop()
    
    
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
            value = value).grid(row=i, column=0, pady = 5)
        i += 1

    
    search_entry = Entry(search_frame, textvariable=search_var)
    search_entry.grid(row=0, column=0, padx=5, pady=5)

    search_btn_query = Button(search_frame, text="Search")
    search_btn_query.grid(row=0, column=1)
 



def home_page():
    #Home page functions
    def kill(event=None):
        check_pricing()
        model_code_write()
        window.destroy()

    def step():
        print_results()
        model_code_write()

    def check_pricing(event=None):
        model.append(model_var.get())
        model_var.set("")
        
    
    def print_results():
        i = 0

        for item in model:
            result_label = Label(product_results_model, text=item, padx=5, pady=5)
            result_label.grid(row=i, column=0)

            i += 1

    window = Tk()
    window.title("Home Page")
    window.geometry("500x500")
    

    window.columnconfigure(0, weight=1, minsize=75)
    window.rowconfigure(1, weight=1, minsize=50)
  
    #Frame of all widgets on home page
    main_frame = ttk.Frame(window)
    main_frame.grid(row=1, column=0, columnspan=3, sticky="NSEW")

    main_frame.columnconfigure(0, weight=1, minsize=50)
    main_frame.rowconfigure(1, weight=1, minsize=50)

    #Creating main Notebook
    home_notebook = ttk.Notebook(main_frame)
    home_notebook.grid(row=1, column=0, sticky="NSEW")
  
    #Creating tabs for Notebooks
    tab_1 = ttk.Frame(home_notebook)
    tab_2 = ttk.Frame(home_notebook)

    

    home_notebook.add(tab_1, text="Products")    
    home_notebook.add(tab_2, text="Customers")

    #Products tab frames
    product_frame_1 = ttk.Frame(tab_1)
    product_frame_1.grid(row=0, column=0, padx=5, pady=5)

    #Product tab info
    product_model_frame = ttk.Labelframe(product_frame_1, text="Input")
    product_model_frame.grid(row=0, column=0, padx=5, pady=5)

    product_results_frame = ttk.Labelframe(product_frame_1, text="Results")
    product_results_frame.grid(row=0, column=1, padx=5, pady=5)

    product_results_model = ttk.Frame(product_results_frame)
    product_results_model.grid(row=0, column=0, padx=5, pady=5)

    product_results_price = ttk.Frame(product_results_frame)
    product_results_price.grid(row=0, column=1, padx=5, pady=5)


    product_model_label = ttk.Label(product_model_frame, text="Model")
    product_model_label.grid(row=0, column=0, padx=5, pady=5)

    #Model variable
    model_var = StringVar()

    product_model_entry = ttk.Entry(product_model_frame, textvariable=model_var)
    product_model_entry.grid(row=0, column=1, padx=5, pady=5)

    product_model_entry.bind("<Return>", check_pricing)
    product_model_entry.bind("<F4>", model_code_write)
    product_model_entry.bind("<F1>", kill)

    model_sub_btn = ttk.Button(product_model_frame, text="Submit", command=check_pricing)
    model_sub_btn.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    run_btn = ttk.Button(product_frame_1, text="Run", command=step)
    run_btn.grid(row=2, column=0, padx=5, pady=5)

    #detail tabs 1 & 2 are added to the main Notebook
    

    #On tab_1
    #New customer button
    new_cust_but = ttk.Button(tab_2, text="Create New Customer", command=new_customer_pop)
    new_cust_but.grid(row=0, column=0, sticky="NSEW", padx=10, pady=10)

    search_btn = ttk.Button(tab_2, text="Search")
    search_btn.grid(row=0, column=1)  

    info_frame = ttk.Frame(tab_2)
    info_frame.grid(row=1, column=0, padx=5, pady=5)

    #Customer first name label
    display_fname = ttk.Label(info_frame, text="First name: ")
    display_fname.grid(row=0, column=0, padx=5, pady=5)

    #Label for last name
    display_lname = ttk.Label(info_frame, text="Last name: ")
    display_lname.grid(row=1, column=0, padx=5, pady=5)

    #Label for mobile number
    display_mobile =ttk.Label(info_frame, text="Mobile: ")
    display_mobile.grid(row=2, column=0, padx=5, pady=5)

    #Label for email
    display_email =ttk.Label(info_frame, text="Email: ")
    display_email.grid(row=3, column=0, padx=5, pady=5)

    window.mainloop()

home_page()