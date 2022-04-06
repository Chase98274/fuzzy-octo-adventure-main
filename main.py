import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from numpy import product
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import csv

class Users():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
user_1 = Users("chase", "1234")

csv_data = []
csv_dictionary = {}

all_models = []
available_models =[]
unavailable_models = []
product_values = {}

def check_pricing():
    driver = webdriver.Chrome(
    executable_path="C://Users//chase//OneDrive//Documents//Coding//fuzzy-octo-adventure-main//chromedriver.exe")
    driver.get("https://www.100percent.co.nz/")

    for item in all_models:
        try:    
            driver.implicitly_wait(10)
            driver.maximize_window()

            searchElement = driver.find_element(By.ID, "searchterm")
            searchElement.send_keys(item)
            searchElement.send_keys(Keys.ENTER)

            model = driver.find_element(By.CSS_SELECTOR, "p.style-number").text
            price = driver.find_element(By.CSS_SELECTOR, "p.price").text.replace("$", "").replace(",", "")
            driver.find_element(By.ID, "searchterm").clear()

            product_values[model] = price
            available_models.append(model)
        
        except:
            driver.find_element(By.ID, "searchterm").clear()
            unavailable_models.append(item)
    
        model_code_write(model)
    print(all_models)
    print(available_models)
    print(unavailable_models)

def model_price_check_csv():
    with open("data\models.csv", mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        csv_clean_data = list(csv_reader)

        i = 0
        for row in csv_clean_data:
            csv_dictionary[csv_clean_data[i][0]] = csv_clean_data[i][1]
            i += 1
        print(csv_dictionary)
    
    csv_file.close()
            


def model_code_write(model):
    with open("data\models.csv", "a", newline="") as file:
        if model in csv_dictionary:
            pass

        if model not in csv_dictionary:
            writer = csv.writer(file)
            writer.writerow([model, product_values[model], datetime.datetime.now()])
            file.close()

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
        ttk.Radiobutton(search_par, text = text, variable = mode,
            value = value).grid(row=i, column=0, pady = 5)
        i += 1

    
    search_entry = ttk.Entry(search_frame, textvariable=search_var)
    search_entry.grid(row=0, column=0, padx=5, pady=5)

    search_btn_query = ttk.Button(search_frame, text="Search")
    search_btn_query.grid(row=0, column=1)
 
def home_page():
    model_price_check_csv()

    #Home page functions
    def kill(event=None):
        print(csv_data)
        window.destroy()

    def step_write(event=None):
        model_var.set(model_var.get().upper().strip())
        step_model = model_var.get()

        if step_model != "":
            all_models.append(model_var.get())
            model_var.set("")

        else:
            messagebox.showerror("Invalid Input", "You have not entered any models.")
            model_var.set("")

    def step_price():
        if len(all_models) > 0:
            check_pricing()
            show_results()
        else:
            messagebox.showerror("Invalid Input", "You have not entered any models.")

    def show_saved_models():
            pass


    def show_results():

        i = 0
        for (model, price) in product_values.items():
            ttk.Label(product_results_model, text="{}:".format(model)).grid(row=i, column=0, pady=5)
            ttk.Label(product_results_price, text="${}".format(price)).grid(row=i, column=0, pady=5)
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

    product_model_entry.bind("<Return>", step_write)
    product_model_entry.bind("<F1>", kill)

    model_sub_btn = ttk.Button(product_model_frame, text="Submit", command=step_write)
    model_sub_btn.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    check_btn = ttk.Button(product_model_frame, text="Check Price", command=step_price)
    check_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

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