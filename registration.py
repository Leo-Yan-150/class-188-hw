import hashlib 
from tkinter import *
from firebase import firebase

registration_window = Tk()
registration_window.geometry("400x400")
registration_window.config(bg="azure")

firebase = firebase.FirebaseApplication("https://homework-432f5-default-rtdb.firebaseio.com", None)
login_username_entry = ""
login_password_entry = ""

def login(): 
    print("give sandvich")
    
def register(): 
    username = username_entry.get()
    password = password_entry.get()
    passwordd = password.encode()
    bytes_password = hashlib.md5(passwordd)
    new_password = bytes_password.hexdigest()
    print(new_password)
    firebase.put("/",username,new_password)
    
def login_window():
    global login_username_entry
    global login_password_entry
    registration_window.destroy()
    
    login_window = Tk()
    login_window.geometry("400x400")
    login_window.config(bg="azure")
    
    log_heading_label = Label(login_window, text="Log In" , font = 'arial 18 bold', bg="azure")
    log_heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)
    
    login_username_label = Label(login_window, text="Username : " , font = 'arial 13', bg="azure")
    login_username_label.place(relx=0.3,rely=0.4, anchor=CENTER)
    
    login_username_entry = Entry(login_window)
    login_username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)
    
    login_password_label = Label(login_window, text="Password : " , font = 'arial 13', bg="azure")
    login_password_label.place(relx=0.3,rely=0.5, anchor=CENTER)
    
    login_password_entry = Entry(login_window)
    login_password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)
    
    btn_login = Button(login_window, text="Log In" , font = 'arial 13 bold' , command=login, relief=FLAT, bg="azure")
    btn_login.place(relx=0.5,rely=0.65, anchor=CENTER)
    
    login_window.mainloop()
  
    
heading_label = Label(registration_window, text="Register" , font = 'arial 18 bold', bg="azure")
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

username_label = Label(registration_window, text="Username : " , font = 'arial 13', bg="azure")
username_label.place(relx=0.3,rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

password_label = Label(registration_window, text="Password :  " , font = 'arial 13', bg="azure")
password_label.place(relx=0.3,rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window)
password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up" , font = 'arial 13 bold' ,command=register, relief=FLAT, padx=10, bg="azure")
btn_reg.place(relx=0.5,rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In" , font = 'arial 10 bold' ,  command=login_window, relief=FLAT, bg="azure")

btn_login_window.place(relx=0.9,rely=0.06, anchor=CENTER)
registration_window.mainloop()